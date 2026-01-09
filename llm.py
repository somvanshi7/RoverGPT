import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_answer(context: str, question: str) -> str:
    prompt = f"""
Answer using ONLY the provided context.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{question}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    data = response.json()
    return data["response"].strip()
