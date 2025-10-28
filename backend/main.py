"""
FastAPI Backend for AI Legal Chatbot
Main application entry point
"""

import sys
from pathlib import Path

# Add project root to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.routes import router
import uvicorn


# Create FastAPI app
app = FastAPI(
    title="AI Legal Chatbot API",
    description="Intelligent chatbot for Indian Constitution and Legal Cases",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],  # React default ports
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(router, prefix="/api", tags=["chatbot"])


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "🏛️ AI Legal Chatbot API",
        "version": "1.0.0",
        "docs": "/docs",
        "status": "running"
    }


@app.on_event("startup")
async def startup_event():
    """Initialize services on startup"""
    print("=" * 80)
    print(">> Starting AI Legal Chatbot Backend")
    print("=" * 80)
    
    from backend.services.rag_service import get_rag_service
    
    # Initialize RAG service
    rag_service = get_rag_service()
    
    # Try to load existing vectorstore
    try:
        loaded = rag_service.load_vectorstore()
        if loaded:
            rag_service.initialize_qa_chain()
            print("[OK] Vector store loaded successfully")
        else:
            print("[WARNING] No vector store found. Please run the scraper and initialize.")
            print("   Run: python backend/scraper/scrape_legal_data.py")
            print("   Then call: POST /api/initialize")
    except Exception as e:
        print(f"[WARNING] Could not load vector store: {str(e)}")
        print("   The chatbot will have limited functionality until initialized.")
    
    print("=" * 80)
    print(">> API Server ready at http://localhost:8000")
    print(">> API Docs available at http://localhost:8000/docs")
    print("=" * 80)


if __name__ == "__main__":
    uvicorn.run(
        "backend.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

