from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys
import os

# Add local directories to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from backend.parsing.resume_parser import mock_parse_resume
from backend.search.search_agent import search_jobs_for_skills
from backend.payments.subscription_manager import SubscriptionManager
from backend.interviews.interview_coach import InterviewCoach

app = FastAPI()

# Enable CORS for the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

sub_manager = SubscriptionManager()
coach = InterviewCoach()

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    # In a real app, we'd read the file content
    # For now, we simulate with our parser
    content = await file.read()
    resume_text = content.decode("utf-8", errors="ignore")
    
    parsed_data = mock_parse_resume(resume_text)
    return {
        "status": "success",
        "parsed_data": parsed_data
    }

@app.get("/search-jobs")
async def search_jobs(user_id: str, skills: str):
    skill_list = skills.split(",")
    jobs = search_jobs_for_skills(skill_list)
    return {"jobs": jobs}

@app.post("/apply")
async def apply_to_job(user_id: str, job_id: str):
    allowed, remaining = sub_manager.record_application(user_id)
    if not allowed:
        raise HTTPException(status_code=403, detail="Daily limit reached. Please upgrade.")
    
    return {
        "status": "applied",
        "message": f"AI Agent applied to {job_id}. Tracking number: verified_{hash(job_id)}",
        "remaining_applications": remaining
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
