# CV-Organizer (OpenClaw / ClawdBot)
### HSB Solutions - Action Assistant Workflow Automation

CV-Organizer is the foundational module of the **OpenClaw (ClawdBot)** ecosystem developed by **HSB Solutions**. It is designed as an "Action Assistant" to automate the management of unstructured curriculum vitae (CV) files, transforming them into a structured digital archive.

---

## Vision & Use Case: HSB CV Organizer
The system acts as a "Digital Archive Officer" for Human Resources (HR) and recruitment managers. It eliminates manual sorting by analyzing CV content, auto-tagging candidates, and building a searchable SQL-based archive. This allows users to filter and find candidates using natural language queries.

---

## Technical Roadmap

### Phase 1: File Handling & Parsing (Completed)
- **Scope:** Support for PDF/DOCX ingestion and raw text extraction.
- **Outcome:** Cleaned, normalized raw text files prepared for analysis.

### Phase 2: Basic Information Extraction (In Progress)
- **Scope:** Extracting core entities (Name, Email, Phone) and sections (Skills, Experience, Education).
- **Outcome:** Structured data in standardized **JSON** format.

### Phase 3: Criteria Matching
- **Scope:** Implementation of skill matching algorithms and candidate scoring (% match) with automated explanations.

### Phase 4: Output Generation
- **Scope:** Exporting results to CSV and integration with Google Sheets API for HR reporting.

### Phase 5: Clawdbot Integration Layer
- **Scope:** Deployment of the `analyze_cvs(folder, criteria)` command with secure logging and authorization.

---

## Standard Data Schema
The system maps each CV to the following standardized JSON structure:

```json
{
  "name": "",
  "skills": [],
  "experience": [],
  "education": []
}
