import json
import random

def calculate_realness_score(job_data):
    """
    Calculates a 'Realness Score' (0-100) based on verified signals.
    - Freshness: 30%
    - Linguistic Quality: 25%
    - Company Legitimacy: 25%
    - Response Rate: 20%
    """
    # Mock scoring logic for the prototype
    freshness = random.randint(60, 100)  # Simulated: days since posted
    linguistic = random.randint(50, 95)   # Simulated: specific vs generic language
    company_legit = random.randint(70, 100) # Simulated: verified domain/headcount
    response_rate = random.randint(20, 80)  # Simulated: interview activity

    score = (0.30 * freshness) + (0.25 * linguistic) + (0.25 * company_legit) + (0.20 * response_rate)
    return round(score)

def search_jobs_for_skills(skills, location="Local Area"):
    """
    Simulates searching the internet for 10 jobs per skill.
    In production, this calls APIs like Adzuna or JSearch.
    """
    all_results = []
    
    for skill in skills:
        # Simulate finding 10 jobs for each skill
        for i in range(1, 11):
            job_id = f"{skill.lower()}-{i}"
            job_title = f"Senior {skill} Engineer"
            company = f"TechCorp {random.randint(1, 50)}"
            
            job_entry = {
                "id": job_id,
                "title": job_title,
                "company": company,
                "location": location,
                "skill_tag": skill,
                "description": f"Join {company} to work on cutting-edge {skill} projects.",
                "days_active": random.randint(1, 45)
            }
            
            # Calculate the Realness Score
            job_entry["realness_score"] = calculate_realness_score(job_entry)
            
            # Filter: only keep jobs with a score above a certain threshold (e.g., 50)
            if job_entry["realness_score"] >= 40:
                all_results.append(job_entry)
                
    return all_results

if __name__ == "__main__":
    # Test with sample skills from the parser
    user_skills = ["Python", "JavaScript", "SQL"]
    found_jobs = search_jobs_for_skills(user_skills)
    
    print(f"Total jobs found: {len(found_jobs)}")
    # Print a sample job with its score
    if found_jobs:
        print("\nSample Verified Job Entry:")
        print(json.dumps(found_jobs[0], indent=2))
