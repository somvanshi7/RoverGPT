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

    try:
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

        # Ollama success case
        if "response" in data:
            return data["response"].strip()

        # Ollama error case
        if "error" in data:
            return f"Ollama error: {data['error']}"

        # Unknown case
        return "LLM returned an unexpected response format."

    except Exception as e:
        return f"LLM failed: {str(e)}"
