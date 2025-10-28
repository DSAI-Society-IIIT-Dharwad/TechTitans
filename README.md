# 🏛️ AI Legal Chatbot for Indian Constitution and Cases

An intelligent AI-powered chatbot that provides legal advice and guidance related to the Indian Constitution and legal cases using advanced NLP and RAG (Retrieval-Augmented Generation) techniques.

## 🌟 Features

- **Intelligent Legal Assistant**: Conversational AI that understands and responds to legal queries
- **RAG System**: Retrieval-Augmented Generation for accurate, context-aware responses
- **Web Scraping**: Automated data collection from legal resources
- **Semantic Search**: Vector-based search for finding relevant legal information
- **Modern UI**: Beautiful, responsive chat interface
- **Real-time Responses**: Fast and accurate legal guidance

## 🏗️ Architecture

```
ai-legal-chatbot/
├── backend/                 # FastAPI backend
│   ├── scraper/            # Web scraping module
│   ├── models/             # Data models
│   ├── services/           # Business logic (RAG, embeddings)
│   ├── api/                # API endpoints
│   └── main.py             # FastAPI application
├── frontend/               # React frontend
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── services/       # API services
│   │   └── App.jsx         # Main application
│   └── package.json
├── data/                   # Scraped legal data
├── vectorstore/            # Vector database storage
└── requirements.txt        # Python dependencies
```

## 🚀 Tech Stack

### Backend
- **FastAPI**: High-performance async API framework
- **LangChain**: LLM orchestration and RAG implementation
- **ChromaDB**: Vector database for semantic search
- **BeautifulSoup4**: Web scraping
- **Sentence Transformers**: Text embeddings
- **OpenAI API** (optional): For enhanced responses

### Frontend
- **React**: Modern UI library
- **Tailwind CSS**: Utility-first styling
- **Axios**: HTTP client
- **React Markdown**: Render formatted responses

## 📦 Installation

### Prerequisites
- Python 3.9+
- Node.js 16+
- npm or yarn

### Backend Setup

1. Navigate to the project directory:
```bash
cd UDBHAV
```

2. Create a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. (Optional) Set up environment variables:
```bash
# Create .env file
echo OPENAI_API_KEY=your_api_key_here > .env
```

5. Run the scraper to collect legal data:
```bash
python backend/scraper/scrape_legal_data.py
```

6. Start the backend server:
```bash
python backend/main.py
```

Backend will run on `http://localhost:8000`

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

Frontend will run on `http://localhost:3000`

## 🎯 Usage

1. Open your browser and go to `http://localhost:3000`
2. Type your legal question in the chat input
3. Get instant, AI-powered legal guidance based on Indian Constitution and cases
4. Continue the conversation for follow-up questions

### Example Queries:
- "What are the fundamental rights under the Indian Constitution?"
- "Explain Article 21 of the Indian Constitution"
- "What is the process for house registration after parents' demise?"
- "What are the legal requirements for property inheritance?"

## 🔧 Configuration

### Using Different LLM Models

The chatbot supports multiple LLM backends:

1. **OpenAI GPT** (Recommended for best results):
   - Set `OPENAI_API_KEY` in `.env`
   - Modify `backend/services/rag_service.py` to use OpenAI

2. **Local LLM** (Hugging Face):
   - Uses open-source models (default)
   - No API key required

3. **Ollama** (Optional):
   - Install Ollama locally
   - Update configuration in `rag_service.py`

## 📊 Data Sources

- Primary source: https://www.kaanoon.com/494607/house-registration-after-parents-demise
- Extensible to add more legal resources
- Supports manual addition of legal documents

## 🎨 Key Implementation Details

### RAG Pipeline:
1. **Document Loading**: Scrape and load legal documents
2. **Text Chunking**: Split documents into manageable chunks
3. **Embedding Generation**: Create vector embeddings using sentence-transformers
4. **Vector Storage**: Store in ChromaDB for fast retrieval
5. **Query Processing**: Convert user queries to embeddings
6. **Semantic Search**: Find relevant legal context
7. **Response Generation**: LLM generates response using retrieved context

### NLP Techniques:
- Text preprocessing and cleaning
- Semantic embeddings for similarity search
- Context-aware response generation
- Conversational memory for follow-up questions

## 🏆 Hackathon Highlights

- ✅ Complete web scraping implementation
- ✅ Advanced RAG system for accurate responses
- ✅ Beautiful, modern UI/UX
- ✅ Production-ready code structure
- ✅ Comprehensive documentation
- ✅ Scalable architecture
- ✅ Real-time conversational AI

## 🔐 Important Notes

- This chatbot provides general legal information and guidance
- **NOT a substitute for professional legal advice**
- Always consult with a qualified lawyer for specific legal matters

## 📝 Future Enhancements

- [ ] Multi-language support (Hindi, Tamil, etc.)
- [ ] Voice input/output
- [ ] Integration with more legal databases
- [ ] User authentication and chat history
- [ ] PDF export of conversations
- [ ] Case law citation system

## 👥 Team

Built with ❤️ for the hackathon

## 📄 License

MIT License - Free to use and modify

---

**Made with cutting-edge AI technology to revolutionize legal assistance in India** 🇮🇳

