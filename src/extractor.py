"""
ClawdBot - Phase 2: LLM-Based Information Extraction
---------------------------------------------------
Description: 
This module acts as a bridge between raw CV text and a Large Language Model.
Instead of using hardcoded keywords, it prepares a structured prompt for 
an LLM to perform intelligent Entity Recognition and Categorization.

Input: 
- Raw CV text from parser.py.

Output: 
- A refined prompt for LLM or a structured JSON response (when API is connected).

"""

import json
import sys
import os

def generate_llm_prompt(raw_text):
    """
    Constructs a specialized prompt that instructs an LLM to parse CV data.
    """
    schema = {
        "name": "Full Name",
        "email": "Email Address",
        "phone": "Phone Number (Universal format)",
        "skills": ["List of technical and soft skills"],
        "experience": [{"title": "", "company": "", "duration": "", "description": ""}],
        "education": [{"degree": "", "school": "", "year": ""}]
    }

    prompt = f"""
    TASK: Extract professional information from the following raw CV text.
    FORMAT: Return ONLY a valid JSON object following the schema below.
    SCHEMA: {json.dumps(schema)}
    
    RAW TEXT:
    ---
    {raw_text}
    ---
    """
    return prompt

def extract_details_llm_stub(text):
    """
    Initial logic to prepare data for LLM processing. 
    In Phase 3, this will call the OpenClaw/Gemini/GPT API.
    """
    # For now, we simulate the LLM's 'thinking' by cleaning 
    # and preparing the prompt that will be sent to the API.
    llm_prompt = generate_llm_prompt(text)
    
    # This return represents what we will send to the LLM
    return llm_prompt

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 src/extractor.py <file_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    with open(input_path, 'r', encoding='utf-8') as f:
        raw_content = f.read()
        
    print("--- ClawdBot LLM Prompt Generator Started ---")
    final_prompt = extract_details_llm_stub(raw_content)
    
    # In a real scenario, we would send 'final_prompt' to the API here.
    # For Phase 2, we display the prompt to verify the LLM will have the right context.
    print("\n[PROMPT PREPARED FOR LLM]:\n")
    print(final_prompt)
