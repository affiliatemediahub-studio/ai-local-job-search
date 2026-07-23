from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
import sys

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Debug: Print environment info to help find issues
print("--- Starting AI Agent ---")
print(f"Current Working Directory: {os.getcwd()}")
print(f"Files in root: {os.listdir('.')}")
print(f"Python Version: {sys.version}")

# Safe imports
try:
    import resume_parser
    import search_agent
    import subscription_manager
    import interview_coach
    modules_loaded = True
except ImportError as e:
    print(f"CRITICAL: Could not load module: {e}")
    modules_loaded = False

@app.get("/")
async def health_check():
    return {
        "status": "online",
        "agent": "active" if modules_loaded else "partial",
        "message": "AI Agent is awake and listening!",
        "port": os.environ.get("PORT", "not set")
    }

if __name__ == "__main__":
    import uvicorn
    # Railway provides the PORT variable automatically
    port = int(os.environ.get("PORT", 8080))
    print(f"Attempting to start on Port: {port}")
    uvicorn.run(app, host="0.0.0.0", port=port)
