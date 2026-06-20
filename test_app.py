from src.classifier import classify_persona
from src.rag_pipeline import RAGPipeline

print(classify_persona("API authentication failure"))

rag = RAGPipeline()

print("success")