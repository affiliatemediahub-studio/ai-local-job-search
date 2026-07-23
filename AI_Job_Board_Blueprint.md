# AI-Powered Local Job Board: Strategic Blueprint

## 1. Product Concept
The platform solves the "Trust Gap" in hiring by using AI to verify that local job listings are authentic, active, and scam-free.

## 2. Core Feature: The "Realness Score"
A composite index (0-100) calculated for every listing:
- **Temporal Freshness (30%)**: Survival analysis of how long the job has been posted vs. company history.
- **Linguistic Quality (25%)**: Detection of generic "pipeline" language or vague role requirements.
- **Company Signals (20%)**: Verification of headcount trends and funding status.
- **Scam Probability (15%)**: Real-time classification of "get rich quick" patterns and non-corporate domains.
- **Community Signal (10%)**: Crowdsourced reporting from candidates.

## 3. Technical Stack
| Layer | Recommendation |
|---|---|
| **Frontend** | Next.js 14 (App Router) + Tailwind CSS |
| **Backend** | Node.js (TypeScript) / Python (FastAPI for ML) |
| **Database** | PostgreSQL (Metadata) + Pinecone (Semantic Search) |
| **Job Data** | Adzuna API, JSearch (RapidAPI) |
| **AI Models** | DistilBERT (Scam Detection), spaCy (NER Extraction) |

## 4. AI Agent Workflow & Automation
### 4.1 Candidate Onboarding
- **Public Sign-in**: Secure authentication via Clerk or NextAuth.
- **Resume Parsing**: AI (using LLMs like GPT-4o) extracts skills, experience, and contact details.

### 4.2 Automated Job Search & Delivery
- **Skill-Based Search**: For each identified skill, the agent searches the internet (via Adzuna/JSearch) for 10 relevant local jobs.
- **Job Matching**: Jobs are scored for "Realness" and relevance before delivery.

### 4.3 Application & Follow-up Loop
- **Custom Assets**: On user interest, the AI agent generates a tailored Resume and Cover Letter for the specific job description.
- **Submission**: Agent sends the application to the hiring company's email address.
- **User Notification**: Automatic email to the candidate confirming successful submission.
- **Smart Follow-up**: If no response, the agent sends a follow-up email to the company every **7 days** to check status.

### 4.5 Human-Style Resume Optimization
- **The 45-Second Rule**: Layout optimized for rapid scanning by human managers.
- **Experience Truncation**: Automatic filtering to show only the most relevant **10-15 years** of work history.
- **Anti-AI Detection**: LLM prompts are specifically tuned to avoid "robotic" buzzwords and use "Human-Style" phrasing to pass recruiter screening.
- **Page Limit**: Hard constraint of **1-2 pages** per document.
- **Format**: Clean, standard layouts that avoid "over-designed" elements that trigger AI detection filters.

## 5. Subscription Model & Quotas
| Tier | Price | Daily Resume Limit | Practice Interviews | Features |
|---|---|---|---|---|
| **Free** | $0 | 2 Job Offers | 1 | Standard Search |
| **Pro** | $9.97/mo | 5 Resumes | 2 | Application Tracking & Verification |
| **Expert** | $19.97/mo | 30 Resumes | 5 | Priority Support + Advanced Tracking |

## 6. Development Roadmap
### Phase 1: MVP (Months 1-3)
- Global job feed via APIs.
- Basic red-flag filtering (domain age, email check).
- Local proximity search.

### Phase 2: The Verification Engine (Months 4-9)
- Deploy the AI Realness Score.
- Semantic matching for resumes.
- Community reporting system.

### Phase 3: Scale (Months 10+)
- Direct employer posting platform.
- AI-validated salary benchmarking.
- Monetization (Verified badge for employers).

---
*Generated for the job board project, July 2026.*
