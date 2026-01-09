import os
import pickle
import faiss
from sentence_transformers import SentenceTransformer
import numpy as np

STORE_DIR = "faiss_store"
INDEX_PATH = os.path.join(STORE_DIR, "index.faiss")
DOCS_PATH = os.path.join(STORE_DIR, "docs.pkl")

class Retriever:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        os.makedirs(STORE_DIR, exist_ok=True)

        if os.path.exists(INDEX_PATH) and os.path.exists(DOCS_PATH):
            self.index = faiss.read_index(INDEX_PATH)
            with open(DOCS_PATH, "rb") as f:
                self.documents = pickle.load(f)
        else:
            self.index = faiss.IndexFlatL2(384)
            self.documents = []

    def add_documents(self, docs):
        embeddings = self.model.encode(docs)
        embeddings = np.array(embeddings).astype("float32")

        self.index.add(embeddings)
        self.documents.extend(docs)

        faiss.write_index(self.index, INDEX_PATH)
        with open(DOCS_PATH, "wb") as f:
            pickle.dump(self.documents, f)

    def retrieve(self, query, top_k=3):
        query_vec = self.model.encode([query]).astype("float32")
        distances, indices = self.index.search(query_vec, top_k)

        results = []
        for idx in indices[0]:
            if idx < len(self.documents):
                results.append(self.documents[idx])

        return results
