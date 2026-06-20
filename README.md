# Persona Adaptive Customer Support Agent

## Overview

An AI-powered customer support system that adapts responses based on customer persona, retrieves relevant information from a knowledge base using Retrieval-Augmented Generation (RAG), and escalates unresolved or sensitive issues to a human support agent.

## Features

* Persona Detection

  * Technical Expert
  * Frustrated User
  * Business Executive

* Knowledge Base Retrieval

  * ChromaDB Vector Database
  * Sentence Transformers Embeddings

* Adaptive Response Generation

  * Persona-specific response styles

* Escalation Logic

  * Billing Issues
  * Refund Requests
  * Sensitive Cases
  * Low Confidence Retrieval

* Human Handoff Summary

* Streamlit User Interface

## Tech Stack

* Python 3.13
* Streamlit
* ChromaDB
* Sentence Transformers
* HuggingFace Embeddings

## Architecture

User Query
→ Persona Detection
→ Knowledge Retrieval
→ Adaptive Response Generation
→ Escalation Check
→ Human Handoff Summary

## Knowledge Base

Support documents include:

* Password Reset
* API Authentication
* Billing Policy
* Refund Policy
* Account Lockout
* Service Outage
* Email Verification
* Database Errors
* Subscription Management
* User Permissions

## Setup

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Example Queries

* API authentication failure
* I forgot my password
* How does this impact operations?
* I need a refund immediately
* Database connection timeout

## Future Improvements

* Multi-turn memory
* Real LLM integration
* Confidence scoring
* Analytics dashboard
* Human approval workflow
