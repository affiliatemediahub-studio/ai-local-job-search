import json

class InterviewCoach:
    """
    AI-powered practice interview agent.
    Generates questions based on job descriptions and provides feedback.
    """
    
    def generate_questions(self, job_title, skills):
        """
        Simulates AI-generated interview questions.
        In production, this would use a prompt like:
        'Act as a hiring manager for [Job Title]. Ask 5 questions based on [Skills].'
        """
        questions = [
            f"Tell me about a time you used {skills[0]} to solve a complex problem.",
            f"What is your experience level with {skills[1]} in a production environment?",
            f"How do you handle tight deadlines when working with a {job_title} team?",
            f"Why are you the best fit for this local position at our company?",
            f"Describe a situation where you had to learn a new technology, like {skills[-1]}, quickly."
        ]
        return questions

    def evaluate_response(self, question, user_answer):
        """
        Simulates AI feedback on a user's answer.
        """
        # Logic would check for keyword density, length, and sentiment
        if len(user_answer) < 20:
            return "Your answer is a bit short. Try to use the STAR method (Situation, Task, Action, Result) to provide more detail."
        
        return "Great response! You clearly demonstrated your expertise. Consider mentioning a specific metric or outcome to make it even stronger."

if __name__ == "__main__":
    coach = InterviewCoach()
    job = "Senior Python Developer"
    skills = ["Python", "AWS", "FastAPI"]
    
    print(f"--- Practice Interview for: {job} ---\n")
    questions = coach.generate_questions(job, skills)
    
    for i, q in enumerate(questions[:2]): # Just show first 2 for demo
        print(f"Q{i+1}: {q}")
        sample_ans = "I used Python to automate our data pipelines which saved us 10 hours a week."
        feedback = coach.evaluate_response(q, sample_ans)
        print(f"Feedback: {feedback}\n")
