"""
Simple backend starter to see any errors
"""
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

print("=" * 80)
print("Starting AI Legal Chatbot Backend...")
print("=" * 80)

try:
    print("\n1. Importing FastAPI...")
    from fastapi import FastAPI
    print("   [OK] FastAPI imported successfully")
    
    print("\n2. Importing CORS middleware...")
    from fastapi.middleware.cors import CORSMiddleware
    print("   [OK] CORS imported successfully")
    
    print("\n3. Creating FastAPI app...")
    app = FastAPI(title="AI Legal Chatbot API")
    print("   [OK] App created successfully")
    
    print("\n4. Configuring CORS...")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000", "http://localhost:5173"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    print("   [OK] CORS configured successfully")
    
    print("\n5. Creating simple routes...")
    @app.get("/")
    async def root():
        return {"message": "AI Legal Chatbot API", "status": "running"}
    
    @app.get("/api/health")
    async def health():
        return {"status": "healthy", "message": "Backend is running"}
    
    print("   [OK] Routes created successfully")
    
    print("\n6. Starting Uvicorn server...")
    print("=" * 80)
    print(">> Backend will start at http://localhost:8000")
    print(">> Press Ctrl+C to stop")
    print("=" * 80)
    
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
    
except Exception as e:
    print(f"\n[ERROR] {str(e)}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

