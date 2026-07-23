import json
import re

def mock_parse_resume(resume_text):
    """
    A prototype function to simulate AI resume parsing.
    In production, this would call an LLM API (like GPT-4o) to extract entities.
    """
    # Simulate extraction of key fields
    skills = ["Python", "JavaScript", "SQL", "React", "Node.js", "Project Management"]
    
    # Mocking extraction using basic regex for the prototype
    email_match = re.search(r'[\w\.-]+@[\w\.-]+', resume_text)
    email = email_match.group(0) if email_match else "unknown@example.com"
    
    parsed_data = {
        "candidate_info": {
            "name": "Sample Candidate",
            "email": email,
            "location": "Local Area"
        },
        "skills_identified": skills,
        "experience_summary": "5+ years in full-stack development and team leadership.",
        "search_queries": [f"{skill} jobs in Local Area" for skill in skills[:3]] # Example search terms
    }
    
    return parsed_data

if __name__ == "__main__":
    # Sample resume content
    sample_resume = """
    John Doe
    Full Stack Developer
    Email: john.doe@example.com
    Skills: Python, JavaScript, SQL, React, Node.js, Project Management.
    Experience: Developed several AI-powered web applications...
    """
    
    result = mock_parse_resume(sample_resume)
    print(json.dumps(result, indent=2))
