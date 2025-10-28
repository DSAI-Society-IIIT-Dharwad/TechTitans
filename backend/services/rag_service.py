"""
RAG (Retrieval-Augmented Generation) Service
Handles document retrieval and response generation
"""

import os
from typing import List, Dict, Optional, Tuple
from pathlib import Path
import json
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.docstore.document import Document
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_community.llms import HuggingFacePipeline


class RAGService:
    """RAG service for legal chatbot"""
    
    def __init__(self, vectorstore_path: str = "./vectorstore", use_openai: bool = False):
        """
        Initialize RAG service
        
        Args:
            vectorstore_path: Path to store vector database
            use_openai: Whether to use OpenAI API (requires OPENAI_API_KEY)
        """
        self.vectorstore_path = vectorstore_path
        self.use_openai = use_openai
        self.embeddings = None
        self.vectorstore = None
        self.qa_chain = None
        self.conversation_history = {}
        
        # Initialize embeddings
        self._initialize_embeddings()
    
    def _initialize_embeddings(self):
        """Initialize embedding model"""
        print("Loading embedding model...")
        
        # Use sentence-transformers for embeddings
        model_name = "sentence-transformers/all-MiniLM-L6-v2"
        self.embeddings = HuggingFaceEmbeddings(
            model_name=model_name,
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': True}
        )
        
        print("[OK] Embedding model loaded")
    
    def load_documents_from_json(self, json_path: str) -> List[Document]:
        """
        Load documents from scraped JSON data
        
        Args:
            json_path: Path to JSON file
            
        Returns:
            List of LangChain Documents
        """
        documents = []
        
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            for item in data:
                # Main content document
                doc = Document(
                    page_content=item.get('content', ''),
                    metadata={
                        'source': item.get('url', 'unknown'),
                        'title': item.get('title', 'Legal Document'),
                        'type': 'main_content'
                    }
                )
                documents.append(doc)
                
                # Q&A pairs as separate documents
                for qa in item.get('qa_pairs', []):
                    qa_doc = Document(
                        page_content=f"Question: {qa['question']}\n\nAnswer: {qa['answer']}",
                        metadata={
                            'source': item.get('url', 'unknown'),
                            'title': item.get('title', 'Legal Document'),
                            'type': 'qa_pair'
                        }
                    )
                    documents.append(qa_doc)
            
            print(f"[OK] Loaded {len(documents)} documents from {json_path}")
            return documents
            
        except Exception as e:
            print(f"[ERROR] Error loading documents: {str(e)}")
            return []
    
    def create_vectorstore(self, documents: List[Document], chunk_size: int = 800, chunk_overlap: int = 100):
        """
        Create vector store from documents with optimized chunking
        
        Args:
            documents: List of documents
            chunk_size: Size of text chunks (increased for better context)
            chunk_overlap: Overlap between chunks (increased to preserve context)
        """
        print("Creating vector store with optimized chunking...")
        
        # Split documents into chunks with better separators
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            # Better separators for legal text
            separators=["\n\n", "\n", ". ", "• ", "- ", " ", ""]
        )
        
        chunks = text_splitter.split_documents(documents)
        print(f"Split into {len(chunks)} chunks")
        
        # Create vector store
        Path(self.vectorstore_path).mkdir(parents=True, exist_ok=True)
        
        self.vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings,
            persist_directory=self.vectorstore_path,
            collection_name="legal_documents"
        )
        
        self.vectorstore.persist()
        print(f"[OK] Vector store created with {len(chunks)} chunks")
    
    def load_vectorstore(self):
        """Load existing vector store"""
        try:
            self.vectorstore = Chroma(
                persist_directory=self.vectorstore_path,
                embedding_function=self.embeddings,
                collection_name="legal_documents"
            )
            
            # Check if vectorstore has documents
            collection = self.vectorstore._collection
            count = collection.count()
            
            if count > 0:
                print(f"[OK] Vector store loaded with {count} documents")
                return True
            else:
                print("[WARNING] Vector store is empty")
                return False
                
        except Exception as e:
            print(f"[ERROR] Error loading vector store: {str(e)}")
            return False
    
    def initialize_qa_chain(self):
        """Initialize the QA chain with LLM"""
        if not self.vectorstore:
            raise ValueError("Vector store not loaded. Please load or create vector store first.")
        
        print("Initializing QA chain...")
        
        # For demo purposes, we'll create a simple retrieval-based system
        # In production, you'd use a proper LLM here
        
        retriever = self.vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 5}  # Retrieve top 5 most relevant chunks for better context
        )
        
        self.retriever = retriever
        print("[OK] QA chain initialized")
    
    def generate_response(self, query: str, conversation_id: Optional[str] = None) -> Tuple[str, List[Dict]]:
        """
        Generate response to user query
        
        Args:
            query: User's question
            conversation_id: Optional conversation ID for context
            
        Returns:
            Tuple of (response, sources)
        """
        if not self.vectorstore:
            return "I'm not ready yet. Please load the knowledge base first.", []
        
        # Retrieve relevant documents with better filtering
        relevant_docs = self.retriever.get_relevant_documents(query)
        
        if not relevant_docs:
            return "I couldn't find specific information about that in my knowledge base. Could you rephrase your question or ask about Indian Constitution, fundamental rights, criminal law (IPC sections), consumer rights, or legal procedures?", []
        
        # Get unique content with better deduplication
        seen_content = set()
        unique_docs = []
        
        # First pass: get highly relevant unique documents
        for doc in relevant_docs:
            content = doc.page_content.strip()
            # Check if content is unique enough (not just substring)
            is_unique = True
            for seen in seen_content:
                # If this content is very similar to something we've seen, skip it
                if len(content) > 100 and (content in seen or seen in content):
                    is_unique = False
                    break
            
            if is_unique and len(content) > 50:
                seen_content.add(content)
                unique_docs.append(doc)
                # Get top 3 most relevant unique documents
                if len(unique_docs) >= 3:
                    break
        
        # If we didn't get enough, relax criteria
        if len(unique_docs) < 2:
            for doc in relevant_docs[:3]:
                if doc not in unique_docs:
                    unique_docs.append(doc)
                if len(unique_docs) >= 2:
                    break
        
        # Prepare context from unique documents
        context = "\n\n---\n\n".join([doc.page_content for doc in unique_docs])
        
        # Create sources list
        sources = []
        for doc in unique_docs:
            sources.append({
                'title': doc.metadata.get('title', 'Legal Document'),
                'source': doc.metadata.get('source', 'Unknown'),
                'type': doc.metadata.get('type', 'document')
            })
        
        # Generate response using the context
        response = self._create_response_from_context(query, context)
        
        return response, sources
    
    def _create_response_from_context(self, query: str, context: str) -> str:
        """
        Create an intelligent response from context with user-desired formatting
        """
        # Extract and clean context
        lines = []
        seen_content = set()
        for line in context.split('\n'):
            line = line.strip()
            if line and line not in seen_content and len(line) > 15:
                seen_content.add(line)
                lines.append(line)
        
        # Take substantial content
        clean_context = '\n\n'.join(lines[:25])  # More content for comprehensive answers
        
        # Limit total length reasonably
        if len(clean_context) > 3500:
            clean_context = clean_context[:3500]
            last_period = clean_context.rfind('.')
            if last_period > 3000:
                clean_context = clean_context[:last_period + 1]
        
        # Format exactly as user desires
        response = f"""**Detailed Explanation:**

{clean_context}

---

**Related Legal Information:**

1. **Applicable Laws and Acts**
   The above information is based on current Indian laws including the Constitution of India, Indian Penal Code (IPC), Code of Criminal Procedure (CrPC), and various special acts as applicable to your query.

2. **Legal Procedures**
   Follow the procedures outlined above. Ensure you collect all necessary documents and evidence. Approach the appropriate authorities or courts as specified.

3. **Your Rights**
   You have fundamental and legal rights under Indian law. These rights are protected by the Constitution and can be enforced through legal mechanisms including filing complaints, FIRs, or approaching consumer forums and courts.

4. **Remedies Available**
   Various remedies are available depending on the nature of your issue - criminal prosecution, civil suits, consumer complaints, writ petitions, or administrative complaints to concerned authorities.

5. **Important Contacts**
   • Police: 100
   • Women Helpline: 1091 / 181
   • Child Helpline: 1098
   • Cyber Crime: 1930
   • Legal Aid: Contact District Legal Services Authority

---

**⚠ Important Disclaimer:**

This information is provided for general educational purposes only. It should not be considered as legal advice. Laws and regulations may change over time. For specific legal matters and personalized guidance, please consult a qualified lawyer or legal expert.

---

**💡 Please Note:** 
This is general legal information for educational purposes only. For advice specific to your situation, please consult a qualified lawyer."""
        
        return response
    
    def get_vectorstore_stats(self) -> Dict:
        """Get statistics about the vector store"""
        if not self.vectorstore:
            return {"loaded": False, "count": 0}
        
        try:
            collection = self.vectorstore._collection
            count = collection.count()
            return {
                "loaded": True,
                "count": count,
                "path": self.vectorstore_path
            }
        except:
            return {"loaded": False, "count": 0}


# Global RAG service instance
rag_service = None


def get_rag_service() -> RAGService:
    """Get or create RAG service instance"""
    global rag_service
    if rag_service is None:
        rag_service = RAGService()
    return rag_service

