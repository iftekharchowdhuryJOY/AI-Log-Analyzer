# 🤖 AI Log Analyzer

**AI Log Analyzer** is a lightweight, intelligent tool that helps DevOps engineers automatically detect and explain problems hidden inside log files.  
It combines traditional regex-based pattern detection with Hugging Face transformers to give quick, readable insights about what went wrong — no training data needed.

Built with **FastAPI**, **Gradio**, and **Transformers**, this project shows how AI and DevOps can blend beautifully.

---

## 🚀 Features

- 🔍 **Automatic Log Classification** – Detects common issues like network errors, timeouts, auth failures, and configuration mistakes.  
- 🧠 **AI-Powered Reasoning** – Uses a zero-shot model (`facebook/bart-large-mnli`) to infer unseen or ambiguous problems.  
- ⚙️ **Hybrid Detection** – Combines regex (for known patterns) + transformers (for new ones).  
- ✨ **Summarization** – Optional T5-small model to summarize large log chunks into readable English.  
- 🖥️ **Dual Mode** – Run as a FastAPI backend or a Gradio web app.  
- 🐳 **Docker-Ready** – One build command, deploy anywhere.

---

## 🧩 Architecture Overview

```text
[User Input or Uploaded Log]
        ↓
[Regex Scan → AI Model]
        ↓
[Issue Classification + Confidence Score]
        ↓
[Readable Summary via API or Gradio UI]
```

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **FastAPI** — API layer  
- **Gradio** — Web UI  
- **Transformers (Hugging Face)** — AI inference  
- **Torch** — Model backend  
- **Regex** — Deterministic rule engine  
- **Docker** — Containerization (optional)

---

## 🧰 Installation

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/ai-log-analyzer.git
cd ai-log-analyzer
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

*(Tip: Use a virtual environment to keep things clean.)*

---

## ⚡ Usage

### ▶️ Run in Gradio (UI Mode)
```bash
python app/main.py
```
It’ll open a local web interface at **http://127.0.0.1:7860**  
Paste log lines and get AI-generated insights instantly.

---

### 🧠 Run as API (FastAPI Mode)
```bash
python app/main.py --mode api
```

Now visit **http://127.0.0.1:8000/docs** for Swagger UI.

Endpoints:
- `GET /` → Health check  
- `POST /analyze/` → Analyze log file  
- `POST /summarize/` → Summarize logs (optional)

---

## 🧪 Example Input

```
[ERROR] Connection refused: host unreachable at 10.0.0.12
```

### Output
```json
{
  "summary": "Detected pattern: network issue (via regex)"
}
```

---

## 🧩 Regex + AI in Action

| Example Log | Detected Issue |
|--------------|----------------|
| `Database connection failed: timeout expired` | Database Error / Timeout |
| `Unauthorized access attempt from IP 172.16.2.45` | Authentication Failure |
| `Missing environment variable: AWS_SECRET_ACCESS_KEY` | Configuration Error |
| `CrashLoopBackOff` | Server / Performance Issue |

---

## 🐳 Docker

### Build Image
```bash
docker build -t ai-log-analyzer .
```

### Run Container
```bash
docker run -p 8000:8000 ai-log-analyzer
```

Access at `http://localhost:8000` or use `--mode ui` for Gradio.

---

## 🧭 Future Enhancements

- [ ] Stream & analyze large (GB-sized) log files in chunks  
- [ ] Slack or Prometheus integration for live alerts  
- [ ] Visualization dashboard (error frequency, trend graphs)  
- [ ] JWT authentication for production API  
- [ ] Model fine-tuning on real DevOps data  

---

## 🧡 Why I Built This

I built this project to explore how **AI can make DevOps smarter** — not by replacing engineers, but by *amplifying* their awareness.  
Logs tell stories, and this analyzer helps you read them faster.

---

## ⚖️ License
MIT License — free for personal or commercial use.  
Just keep the credit if you share or improve it. 🙏

---

## 👤 Author

**Iftekhar Joy**  
DevOps & AI Engineer  
🔗 [imjoy.me](https://imjoy.me) | [GitHub](https://github.com/iftekharchowdhuryJOY) | [LinkedIn](https://www.linkedin.com/in/iftekharul-islam/)
