# AI Assistant — Local Chat UI

A simple chat interface for running **Granite 4.1** locally via Ollama, served through a FastAPI backend.

Built as a personal project to explore local LLMs without sending data to any external API.

---

## Stack

- [Ollama](https://ollama.com) — runs the model locally
- [FastAPI](https://fastapi.tiangolo.com) — Python backend
- Vanilla HTML/CSS/JS — no frontend framework
- GOV.UK Design System — for styling

---

## Setup

**1. Install dependencies**
```bash
pip install fastapi uvicorn ollama
```

**2. Pull the model**
```bash
ollama pull granite4.1:3b
```

**3. Run**
```bash
python main.py
```

Then open `http://localhost:8000` in your browser.

---

## Features

- Stream or full response mode
- Markdown rendering with syntax-highlighted code blocks
- Conversation memory within a session
- New chat resets context entirely

---

## Project Structure

```
project/
├── main.py       # FastAPI backend
└── index.html    # Frontend (served by FastAPI)
```

---

## Notes

- Model runs fully offline — no data leaves your machine
- Tested on Windows with Python 3.11
- Ctrl + Enter to send a message

---

**Developed by Mihir Panchal**  
Master of Applied Computer Science — Concordia University
