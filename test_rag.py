from src.rag_pipeline import RAGPipeline

rag = RAGPipeline()

rag.ingest_documents()

results = rag.retrieve("I need a refund immediately")

print(results)