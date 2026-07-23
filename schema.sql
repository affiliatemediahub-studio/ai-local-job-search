-- AI Local Job Search Platform Database Schema

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Users Table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email TEXT UNIQUE NOT NULL,
    full_name TEXT,
    subscription_tier TEXT DEFAULT 'FREE' CHECK (subscription_tier IN ('FREE', 'PRO', 'EXPERT')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Resumes Table
CREATE TABLE resumes (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    file_path TEXT NOT NULL,
    skills_json JSONB, -- Stores identified skills as an array
    parsed_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Jobs Cache Table (with Realness Scores)
CREATE TABLE jobs_cache (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    external_id TEXT UNIQUE,
    title TEXT NOT NULL,
    company TEXT NOT NULL,
    location TEXT NOT NULL,
    description TEXT,
    realness_score INTEGER CHECK (realness_score BETWEEN 0 AND 100),
    first_seen TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_verified TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Applications & Quota Tracking
CREATE TABLE applications (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id),
    job_id UUID REFERENCES jobs_cache(id),
    status TEXT DEFAULT 'SENT', -- SENT, READ, INTERVIEW_OFFERED
    applied_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    follow_up_count INTEGER DEFAULT 0,
    last_follow_up TIMESTAMP WITH TIME ZONE
);

-- Daily Usage Counters (to enforce subscription limits)
CREATE TABLE daily_usage (
    user_id UUID REFERENCES users(id),
    usage_date DATE DEFAULT CURRENT_DATE,
    count INTEGER DEFAULT 0,
    PRIMARY KEY (user_id, usage_date)
);

-- Indexing for performance
CREATE INDEX idx_user_email ON users(email);
CREATE INDEX idx_usage_date ON daily_usage(usage_date);
CREATE INDEX idx_jobs_realness ON jobs_cache(realness_score);
