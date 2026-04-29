"""
ClawdBot - Phase 5: Integration Layer (The Orchestrator)
------------------------------------------------------
Description: 
This is the main entry point of the CV-Organizer system. It coordinates 
the data flow between the Parser, Matcher, and Output Manager modules 
to provide an end-to-end CV analysis pipeline.

Workflow:
1. Scan 'data/' folder for CV text files.
2. Send each file to 'matcher.py' for AI-based analysis.
3. Collect all results into a list.
4. Use 'output_manager.py' to generate the final CSV report and terminal table.
"""

import os
import sys
from src.matcher import match_cv_to_job
from src.output_manager import save_to_csv

def analyze_cvs(folder_path="data"):
    """
    PURPOSE: Automatically processes all extracted CV texts in a folder and generates a report.
    INPUT: folder_path (String) -> Path to the folder containing .txt files.
    """
    print(f"--- 🚀 ClawdBot CV Analysis Pipeline Started ---")
    print(f"--- Scanning folder: {folder_path} ---\n")

    # 1. Identify Target Files: Look for extracted text files
    try:
        cv_files = [f for f in os.listdir(folder_path) if f.startswith("extracted_") and f.endswith(".txt")]
    except FileNotFoundError:
        print(f"❌ ERROR: Folder '{folder_path}' not found.")
        return

    if not cv_files:
        print("⚠️ WARNING: No extracted_*.txt files found in the data folder.")
        return

    all_results = []

    # 2. Processing Loop: Analyze each CV one by one
    for filename in cv_files:
        file_path = os.path.join(folder_path, filename)
        
        print(f"🔍 Analyzing: {filename}...")
        
        # Read the content of the extracted CV text
        with open(file_path, 'r', encoding='utf-8') as f:
            cv_text = f.read()
        
        # Call the Matcher (Phase 3 logic)
        analysis = match_cv_to_job(cv_text)
        
        # Format the name for the table (removes 'extracted_' and '.txt')
        clean_name = filename.replace("extracted_", "").replace(".txt", "").replace("_", " ")

        # 3. Data Aggregation: Prepare the entry for the final report
        entry = {
            "Name": clean_name.upper(),
            "Skills": ", ".join(analysis.get("strengths", ["N/A"])),
            "Score": analysis.get("score", 0),
            "Notes": analysis.get("reason", "No detailed notes.")
        }
        all_results.append(entry)

    # 4. Final Output: Generate CSV and Display Terminal Table (Phase 4 logic)
    if all_results:
        save_to_csv(all_results)
        print(f"--- ✅ Successfully processed {len(all_results)} CV(s) ---")
    else:
        print("❌ No data to save.")

if __name__ == "__main__":
    # Define ClawdBot command behavior
    # Usage: python3 main.py
    analyze_cvs()
