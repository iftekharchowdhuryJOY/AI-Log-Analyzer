from fastapi import FastAPI, UploadFile, File
from transformers import pipeline
import re
import gradio as gr

app = FastAPI(title="AI Log Analyzer – Smart Edition")

# --- Initialize AI Pipelines ---
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
summarizer = pipeline("summarization", model="t5-small")

# --- Label candidates for classification ---
LABELS = [
    "network issue",
    "server error",
    "authentication failure",
    "performance issue",
    "configuration error",
    "timeout",
    "database error",
    "system healthy",
    "other"
]

# --- Common regex patterns for known issues ---
PATTERNS = {
    "network issue": r"(connection\s*refused|host\s*unreachable|dns\s*error|network\s*down)",
    "server error": r"(internal\s*server\s*error|http\s*500|service\s*unavailable)",
    "authentication failure": r"(unauthorized|forbidden|invalid\s*credentials|auth\s*failed)",
    "configuration error": r"(missing\s*(config|env|key)|invalid\s*(path|argument))",
    "timeout": r"(timeout|timed\s*out|took\s*too\s*long)",
    "database error": r"(sql\s*error|database\s*connection\s*failed|query\s*failed)",
    "permission denied": r"(permission\s*denied|access\s*refused)"
}


# --- Utility: Scan for known patterns ---
def regex_scan(text: str):
    for label, pattern in PATTERNS.items():
        if re.search(pattern, text, re.IGNORECASE):
            return label
    return None


@app.get("/")
def root():
    return {"message": "AI Log Analyzer is running 🚀"}


# --- Main Analysis Endpoint ---
@app.post("/analyze/")
async def analyze_log(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8")[:1500]

    # Step 1: Try regex-based detection
    regex_result = regex_scan(text)
    if regex_result:
        return {
            "summary": f"Detected pattern: {regex_result} (via regex)",
            "method": "regex"
        }

    # Step 2: Fall back to AI classification
    result = classifier(text, candidate_labels=LABELS)
    top_label = result["labels"][0]
    confidence = round(result["scores"][0] * 100, 2)

    return {
        "summary": f"Likely issue: {top_label} ({confidence}% confidence)",
        "method": "AI classification",
        "details": result
    }


# --- Optional: Summarization Endpoint ---
@app.post("/summarize/")
async def summarize_log(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8")[:2000]
    summary = summarizer(text, max_length=80, min_length=25, do_sample=False)
    return {"summary": summary[0]["summary_text"]}


# --- Gradio Web Interface ---
def analyze_text(text):
    if not text.strip():
        return "Please enter log text."

    # Try regex first
    regex_result = regex_scan(text)
    if regex_result:
        return f"Pattern matched: {regex_result}"

    # Otherwise use AI
    result = classifier(text, candidate_labels=LABELS)
    label = result["labels"][0]
    conf = round(result["scores"][0]*100, 2)
    return f"AI detected: {label} ({conf}%)"


demo = gr.Interface(
    fn=analyze_text,
    inputs="textbox",
    outputs="text",
    title="AI Log Analyzer – Smart Edition",
    description="Detects log problems using Regex + AI (Hugging Face)"
)


# --- Run Either API or UI ---
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["api", "ui"], default="ui",
                        help="Choose run mode: ui (Gradio) or api (FastAPI)")
    args = parser.parse_args()

    if args.mode == "api":
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=8000)
    else:
        demo.launch()
