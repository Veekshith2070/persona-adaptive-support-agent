import os
from sentence_transformers import SentenceTransformer
import chromadb


class RAGPipeline:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        self.client = chromadb.PersistentClient(path="./chroma_db")

        self.collection = self.client.get_or_create_collection(
            name="support_docs"
        )

    def ingest_documents(self, folder_path="data"):

        doc_id = 0

        for filename in os.listdir(folder_path):

            if filename.endswith(".md"):

                filepath = os.path.join(folder_path, filename)

                with open(filepath, "r", encoding="utf-8") as f:
                    text = f.read()

                chunks = self.chunk_text(text)

                for chunk in chunks:

                    embedding = self.model.encode(chunk).tolist()

                    self.collection.add(
                        ids=[str(doc_id)],
                        embeddings=[embedding],
                        documents=[chunk],
                        metadatas=[{"source": filename}]
                    )

                    doc_id += 1

    def chunk_text(self, text, chunk_size=500):

        chunks = []

        for i in range(0, len(text), chunk_size):
            chunks.append(text[i:i + chunk_size])

        return chunks

    def retrieve(self, query, top_k=3):

        query_embedding = self.model.encode(query).tolist()

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        return results