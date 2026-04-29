"""
ClawdBot - Phase 3: AI-Driven Candidate Matching
-----------------------------------------------
Description: 
This module implements In-Context Learning to evaluate CVs. Instead of 
hardcoded keyword matching, it prepares a high-context prompt for an LLM 
to perform semantic analysis, scoring, and justification based on specific 
job requirements provided in the context.

Input: 
- Raw text from the CV (Phase 1 output).
- Specific job criteria provided as context.

Output: 
- A structured prompt intended for an LLM to generate a match score and explanation.

"""

import json
import sys
import os

def create_matching_context(cv_text, job_description):
    """
    Wraps the candidate's data and the job's specific needs into an 
    In-Context Learning template for the LLM.
    
    Args:
        cv_text (str): The raw extracted text from the CV.
        job_description (dict): The target profile and technical requirements.
        
    Returns:
        str: A comprehensive prompt for AI decision making.
    """
    
    # Standard output schema to ensure the LLM returns data in a predictable way
    response_schema = {
        "candidate_name": "string",
        "overall_match_score": "integer (0-100)",
        "technical_alignment": "string (brief analysis)",
        "missing_critical_skills": ["list"],
        "hiring_recommendation": "Strongly Recommend / Consider / Reject",
        "explanation": "Detailed reasoning for the score"
    }

    prompt = f"""
    ### ROLE:
    You are an expert Technical Recruiter and Hiring Manager.
    
    ### CONTEXT / JOB REQUIREMENTS:
    Domain/Role: {job_description.get('domain')}
    Essential Tools & Skills: {", ".join(job_description.get('essential_tools', []))}
    Experience Level: {job_description.get('experience_level')}
    Additional Criteria: {job_description.get('special_notes')}

    ### CANDIDATE DATA:
    ---
    {cv_text}
    ---

    ### TASK:
    Perform a deep semantic analysis of the candidate based on the provided data. 
    Do not rely solely on exact keyword matching. Infer the candidate's proficiency 
    and expertise based on their project history, responsibilities, and context.

    ### OUTPUT INSTRUCTIONS:
    Return ONLY a valid JSON object following this schema:
    {json.dumps(response_schema, indent=2)}
    """
    return prompt

if __name__ == "__main__":
    print("--- ClawdBot Matcher: Preparing In-Context Analysis ---")
    
    if len(sys.argv) < 2:
        print("Usage: python3 src/matcher.py <cv_text_file>")
        sys.exit(1)

    # Generic Job Criteria Example
    # This dictionary provides the 'Context' for the In-Context Learning process.
    target_job_criteria = {
        "domain": "Software Engineering & Systems Integration",
        "essential_tools": ["Python", "SQL", "Git"],
        "experience_level": "Junior to Mid-Level",
        "special_notes": "Prioritize candidates with strong problem-solving skills and project documentation."
    }

    input_file = sys.argv[1]
    if os.path.exists(input_file):
        with open(input_file, 'r', encoding='utf-8') as f:
            raw_cv_content = f.read()
        
        # Generate the thinking template for the LLM
        final_prompt = create_matching_context(raw_cv_content, target_job_criteria)
        
        print("\n--- IN-CONTEXT PROMPT READY ---")
        print(final_prompt)
    else:
        print(f"Error: File {input_file} not found.")
