# claRA
Insurance claim Review Agent


## Architechture

- Uses **FastAPI** for backend, **LangGraph** for agent orchestration, and **OpenAI GPT** for all LLM operations.
- Upload claim-related PDFs, and `/process-claim` endpoint orchestrates classification, extraction, validation, and claim decision.

## AI Tool Usage

- Used **ChatGPT** for design, code, and prompt crafting.
- **Cursor** for code scaffolding and editing.

## Sample Prompts Used

1. **Document Classification**  
   "You are a medical document classifier. Given the filename and content, output ONLY ONE of these types: bill, discharge_summary, id_card, or unknown."

2. **Bill Extraction**  
   "Extract the following fields from the hospital bill (as JSON): hospital_name, total_amount, date_of_service. Return ONLY a valid JSON object with those keys..."

3. **Validation**  
   "Given these structured claim documents (JSON array), identify missing required document types (must have bill and discharge_summary), and any discrepancies in patient or date fields. Return a JSON object with two arrays: missing_documents, discrepancies."

## Running Locally

1. `pip install -r requirements.txt`
2. Set your OpenAI key:  
   `export OPENAI_API_KEY=sk-...`
3. `uvicorn main:app --reload`
4. POST PDF files to `/process-claim`

## Notes

- Plug in actual PDF files (sample link in assignment).
- Extend with more agents or fields as needed.