# 🚀 HSB Solutions - Action Assistant: CV-Organizer

**CV-Organizer** is the foundational module of the **OpenClaw (ClawdBot)** ecosystem. Designed as an "Action Assistant," it automates the management of unstructured curriculum vitae (CV) files, transforming raw data into actionable HR insights.

---

## 🎯 Vision & Use Case
The system acts as a **Digital Archive Officer** for recruitment managers and HR teams. It eliminates manual sorting by analyzing CV content, auto-tagging candidates, and building a searchable data structure. This aligns with HSB Solutions' goal of optimizing business workflows through intelligent automation.

---

## 🛠️ Technical Roadmap

* **Phase 1: File Handling & Parsing (Completed)** - PDF/DOCX text extraction.
* **Phase 2: Information Extraction (Completed)** - LLM-based entity recognition and prompt engineering.
* **Phase 3: Criteria Matching (Completed)** - Scoring algorithms and candidate-job fit analysis.
* **Phase 4: Output Generation (Completed)** - Professional CSV reporting and terminal-based table visualization.
* **Phase 5: Clawdbot Integration (In Progress)** - Unified command-line interface and automation layer.

---

## 💻 Getting Started (Quick Start Guide)

Follow these steps to set up the environment and run the analysis pipeline on your local machine.

### 1. Repository Setup
Clone the project and navigate to the directory:
```bash
git clone <repository-url>
cd CV-Organizer

### 2. Environment Configuration
Create a virtual environment to keep dependencies isolated:

# Create virtual environment
```bash
python3 -m venv venv

# Activate the environment
```bash
source venv/bin/activate

# Install required dependencies
```bash
pip install requests websocket-client

###3. Usage & Command Sequence
The project processes CVs in a specific pipeline. Follow these commands to run each stage:

Step A: Parse PDF/Docx to Text

```bash
python3 src/parser.py data/your_cv_file.pdf

Step B: Generate AI Analysis & Scoring

```bash
python3 src/matcher.py data/extracted_cv_text.txt

Step C: Generate Final Reports (Table & CSV)

# This generates a terminal table and updates outputs/evaluation_results.csv
```bash
python3 src/output_manager.py

📊 Data & Project Structure
Standard Output Schema
The system standardizes each candidate's data into the following format:

Name: Full name of the candidate.

Skills: Extracted technical and soft skills.

Score: Match percentage based on job criteria.

Notes: Automated AI feedback on candidate's background.

Folder Structure


CV-Organizer/
├── data/       # Input CVs and extracted .txt files
├── src/        # Core source code (parser, matcher, output_manager)
├── outputs/    # Generated CSV reports and evaluations
└── venv/       # Python virtual environment


