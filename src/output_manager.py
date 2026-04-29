"""
ClawdBot - Phase 4: Output Generation (Reporting Layer)
------------------------------------------------------
Description: 
This module converts processed AI analysis results into human-readable 
formats. It manages file I/O for reports and handles terminal-based 
data visualization.

Input: 
- Structured list of dictionaries containing candidate scores and notes.

Output: 
- A formatted CSV file in the 'outputs/' directory.
- A clean, professional table printed to the terminal.
"""

import csv
import os

def save_to_csv(data_list, filename="evaluation_results.csv"):
    """
    PURPOSE: Saves analyzed candidate data into a permanent CSV format in the 'outputs' folder.
    INPUT: data_list (List) -> Dictionaries containing candidate information.
    OUTPUT: Full path of the saved file (String).
    """
    
    # 1. Project Configuration: Ensure output directory exists to keep root clean
    fieldnames = ['Name', 'Skills', 'Score', 'Notes']
    output_dir = "outputs"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir) # Create directory if it doesn't exist
    
    file_path = os.path.join(output_dir, filename)
    
    try:
        # 2. Recording Strategy: Use 'Append' mode to add new data to existing file
        file_exists = os.path.isfile(file_path)
        with open(file_path, mode='a', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            
            # Write column headers only if the file is being created for the first time
            if not file_exists:
                writer.writeheader()
                
            for row in data_list:
                writer.writerow(row)
        
        # 3. Terminal Visualization: Print the table to screen immediately after saving
        display_results_as_table(data_list)
        
        return file_path
        
    except Exception as e:
        print(f"❌ ERROR: An issue occurred during the saving process: {e}")
        return None

def display_results_as_table(data_list):
    """
    PURPOSE: Presents analysis results in a professional table layout on the terminal.
    INPUT: data_list (List) -> Candidate data to be displayed.
    """
    
    # Visual Separator and Header Row
    print("\n" + "="*95)
    print(f"{'FULL NAME':<25} | {'SKILLS':<30} | {'SCORE':<6} | {'NOTES'}")
    print("-" * 95)
    
    # Processing Data Rows
    for item in data_list:
        # Limit text lengths to maintain table symmetry
        name = str(item.get('Name', 'N/A'))[:25]
        skills = str(item.get('Skills', 'N/A'))[:30]
        score = str(item.get('Score', '0'))
        notes = str(item.get('Notes', 'No notes available.'))
        
        # Professional left-aligned formatting
        print(f"{name:<25} | {skills:<30} | {score:<6} | {notes}")
    
    print("="*95 + "\n")

if __name__ == "__main__":
    # --- Module Independent Test ---
    print("--- ClawdBot Output Manager: Test Mode Started ---")
    
    test_data = [{
        "Name": "System Test User",
        "Skills": "Python, Linux, CSV Export",
        "Score": 100,
        "Notes": "Output manager module verified successfully."
    }]
    
    save_to_csv(test_data)
