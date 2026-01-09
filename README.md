# RoverGPT 🤖

RoverGPT is an offline Retrieval-Augmented Generation (RAG) system that allows users to ask questions from PDF documents using a local LLM.

## Features
- PDF ingestion and chunking
- Semantic search using FAISS
- Local LLaMA-3 inference via Ollama
- FastAPI backend
- Streamlit-based chat UI
- Fully offline, no API keys or quotas

## Tech Stack
- Python
- FastAPI
- FAISS
- SentenceTransformers
- Ollama (LLaMA-3)
- Streamlit

## How to Run

### 1. Ingest PDF
```bash
python ingest.py
````

### 2. Start backend

```bash
uvicorn main:app --reload
```

### 3. Start UI

```bash
streamlit run ui.py
```

## Usage

Ask questions like:

* "Summarize this document"
* "What is this document about?"
* Any factual question from the PDF

## Notes

This project runs completely offline and avoids hallucinations by answering strictly from retrieved context.

```

---
