import pdfplumber
from retriever import Retriever

CHUNK_SIZE = 400
OVERLAP = 50

def chunk_text(text):
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunks.append(" ".join(words[i:i+CHUNK_SIZE]))
        i += CHUNK_SIZE - OVERLAP
    return chunks

def ingest_pdf(path):
    retriever = Retriever()
    chunks = []

    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                chunks.extend(chunk_text(text))

    retriever.add_documents(chunks)
    print(f"✅ Ingested {len(chunks)} chunks.")

if __name__ == "__main__":
    ingest_pdf("sample.pdf")
