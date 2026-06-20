import streamlit as st

from src.classifier import classify_persona
from src.rag_pipeline import RAGPipeline
from src.generator import generate_response
from src.escalator import should_escalate, generate_handoff

st.title("Persona Adaptive Customer Support Agent")

query = st.text_input("Enter your issue")

if query:

    st.write("Processing...")

    # Persona Detection
    persona = classify_persona(query)

    # RAG Pipeline
    rag = RAGPipeline()

    try:
        rag.ingest_documents()
    except:
        pass

    results = rag.retrieve(query)

    # Context Extraction
    context = "\n".join(results["documents"][0])

    # Gemini Response
    response = generate_response(
        query,
        persona,
        context
    )

    # Persona
    st.subheader("Detected Persona")
    st.write(persona)

    # Generated Response
    st.subheader("Generated Response")
    st.write(response)

    # Sources
    st.subheader("Retrieved Sources")

    sources = []

    if results["metadatas"]:

        for meta in results["metadatas"][0]:
            sources.append(meta["source"])
            st.write(meta["source"])

    # Context
    st.subheader("Retrieved Context")

    if results["documents"]:

        for doc in results["documents"][0]:
            st.write(doc)

    # Escalation Logic
    score = results["distances"][0][0]

    st.subheader("Escalation Status")

    if should_escalate(query, score):

        st.error("Escalated to Human Agent")

        handoff = generate_handoff(
            persona,
            query,
            sources
        )

        st.subheader("Human Handoff Summary")
        st.json(handoff)

    else:

        st.success("Resolved by AI Agent")