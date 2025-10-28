"""
Training Script for AI Legal Chatbot
Scrapes legal data and builds/updates the vectorstore
"""

import sys
import os
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent / "backend"))

from scraper.scrape_legal_data import LegalDataScraper
from services.rag_service import RAGService


def main():
    """Main training pipeline"""
    
    print("="*80)
    print("AI LEGAL CHATBOT - TRAINING PIPELINE")
    print("="*80)
    print()
    
    # Step 1: Check if data exists
    print("STEP 1: Checking Legal Data")
    print("-"*80)
    
    data_path = Path('data/raw/legal_data.json')
    
    if data_path.exists():
        import json
        with open(data_path, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
        print(f"[OK] Found existing data with {len(existing_data)} documents")
        print("[SKIP] Skipping scraping step (data already exists)")
    else:
        print("No existing data found. Scraping...")
        scraper = LegalDataScraper()
        
        urls = [
            "https://www.kaanoon.com/494607/house-registration-after-parents-demise",
        ]
        
        print(f"Scraping {len(urls)} URL(s)...")
        scraped_data = scraper.scrape_multiple_urls(urls)
        
        if not scraped_data:
            print("[ERROR] No data was scraped. Please run: python add_legal_knowledge.py")
            return
        
        scraper.save_to_json(scraped_data, 'data/raw/legal_data.json')
        scraper.save_to_text(scraped_data, 'data/raw/legal_data.txt')
        print(f"[OK] Successfully scraped {len(scraped_data)} page(s)")
    
    print()
    
    # Step 2: Build vectorstore
    print("STEP 2: Building Vector Store")
    print("-"*80)
    
    # Initialize RAG service
    rag_service = RAGService(vectorstore_path="./vectorstore")
    
    # Load documents from JSON
    documents = rag_service.load_documents_from_json('data/raw/legal_data.json')
    
    if not documents:
        print("[ERROR] No documents loaded")
        return
    
    print(f"Loaded {len(documents)} documents")
    
    # Create vectorstore
    rag_service.create_vectorstore(
        documents=documents,
        chunk_size=500,
        chunk_overlap=50
    )
    
    print("[OK] Vector store created successfully")
    print()
    
    # Step 3: Verify
    print("STEP 3: Verification")
    print("-"*80)
    
    stats = rag_service.get_vectorstore_stats()
    print(f"[OK] Vectorstore loaded: {stats['loaded']}")
    print(f"[OK] Document count: {stats['count']}")
    print(f"[OK] Storage path: {stats['path']}")
    print()
    
    print("="*80)
    print("TRAINING COMPLETE!")
    print("="*80)
    print()
    print("Next steps:")
    print("1. Start the backend: python start_backend_simple.py")
    print("2. Start the frontend: cd frontend && npm start")
    print("3. Visit http://localhost:3000")
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[ERROR] Training interrupted by user")
    except Exception as e:
        print(f"\n\n[ERROR] Error during training: {str(e)}")
        import traceback
        traceback.print_exc()

