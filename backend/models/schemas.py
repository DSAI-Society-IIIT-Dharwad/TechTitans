"""
Pydantic models for request/response validation
"""

from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from datetime import datetime


class ChatMessage(BaseModel):
    """Chat message model"""
    role: str = Field(..., description="Role: 'user' or 'assistant'")
    content: str = Field(..., description="Message content")
    timestamp: Optional[datetime] = Field(default_factory=datetime.now)


class ChatRequest(BaseModel):
    """Request model for chat endpoint"""
    message: str = Field(..., min_length=1, max_length=2000, description="User's legal query")
    conversation_id: Optional[str] = Field(None, description="Conversation ID for context")
    
    class Config:
        json_schema_extra = {
            "example": {
                "message": "What are the fundamental rights under the Indian Constitution?",
                "conversation_id": "conv_123"
            }
        }


class ChatResponse(BaseModel):
    """Response model for chat endpoint"""
    response: str = Field(..., description="AI-generated response")
    conversation_id: str = Field(..., description="Conversation ID")
    sources: Optional[List[Dict]] = Field(None, description="Source documents used")
    confidence: Optional[float] = Field(None, description="Confidence score")
    
    class Config:
        json_schema_extra = {
            "example": {
                "response": "The fundamental rights are enshrined in Part III of the Indian Constitution...",
                "conversation_id": "conv_123",
                "sources": [{"title": "Article 14", "relevance": 0.95}],
                "confidence": 0.92
            }
        }


class SourceDocument(BaseModel):
    """Model for source document metadata"""
    title: str
    content: str
    url: Optional[str] = None
    relevance_score: Optional[float] = None


class HealthResponse(BaseModel):
    """Health check response"""
    status: str
    message: str
    timestamp: datetime = Field(default_factory=datetime.now)
    vectorstore_loaded: bool = False
    documents_count: int = 0


class ScrapeRequest(BaseModel):
    """Request to trigger scraping"""
    urls: List[str] = Field(..., description="URLs to scrape")
    
    class Config:
        json_schema_extra = {
            "example": {
                "urls": ["https://www.kaanoon.com/494607/house-registration-after-parents-demise"]
            }
        }


class ScrapeResponse(BaseModel):
    """Response from scraping operation"""
    status: str
    pages_scraped: int
    message: str

