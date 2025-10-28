"""
API Routes for Legal Chatbot
"""

from fastapi import APIRouter, HTTPException, BackgroundTasks
from typing import Dict
import uuid
from backend.models.schemas import (
    ChatRequest, ChatResponse, HealthResponse, 
    ScrapeRequest, ScrapeResponse
)
from backend.services.rag_service import get_rag_service


router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    rag_service = get_rag_service()
    stats = rag_service.get_vectorstore_stats()
    
    return HealthResponse(
        status="healthy",
        message="AI Legal Chatbot is running",
        vectorstore_loaded=stats.get("loaded", False),
        documents_count=stats.get("count", 0)
    )


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Main chat endpoint
    Processes user queries and returns AI-generated responses
    """
    try:
        rag_service = get_rag_service()
        
        # Generate conversation ID if not provided
        conversation_id = request.conversation_id or f"conv_{uuid.uuid4().hex[:8]}"
        
        # Generate response using RAG
        response_text, sources = rag_service.generate_response(
            query=request.message,
            conversation_id=conversation_id
        )
        
        return ChatResponse(
            response=response_text,
            conversation_id=conversation_id,
            sources=sources,
            confidence=0.85  # Placeholder confidence score
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating response: {str(e)}")


@router.post("/initialize")
async def initialize_vectorstore(background_tasks: BackgroundTasks):
    """
    Initialize or reload the vector store
    """
    try:
        rag_service = get_rag_service()
        
        # Try to load existing vectorstore
        loaded = rag_service.load_vectorstore()
        
        if loaded:
            rag_service.initialize_qa_chain()
            return {
                "status": "success",
                "message": "Vector store loaded successfully",
                "stats": rag_service.get_vectorstore_stats()
            }
        else:
            # If no vectorstore exists, try to create from scraped data
            import os
            data_path = "data/raw/legal_data.json"
            
            if os.path.exists(data_path):
                documents = rag_service.load_documents_from_json(data_path)
                if documents:
                    rag_service.create_vectorstore(documents)
                    rag_service.initialize_qa_chain()
                    return {
                        "status": "success",
                        "message": "Vector store created successfully",
                        "stats": rag_service.get_vectorstore_stats()
                    }
            
            return {
                "status": "warning",
                "message": "No scraped data found. Please run the scraper first.",
                "stats": rag_service.get_vectorstore_stats()
            }
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error initializing vectorstore: {str(e)}")


@router.get("/stats")
async def get_stats():
    """Get chatbot statistics"""
    rag_service = get_rag_service()
    stats = rag_service.get_vectorstore_stats()
    
    return {
        "vectorstore": stats,
        "status": "operational" if stats.get("loaded") else "not_initialized"
    }

