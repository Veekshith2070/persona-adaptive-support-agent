def should_escalate(query, score):

    sensitive_topics = [
        "refund",
        "billing",
        "legal",
        "account deletion",
        "duplicate charge"
    ]

    query = query.lower()

    if score < 0.45:
        return True

    if any(topic in query for topic in sensitive_topics):
        return True

    return False


def generate_handoff(persona, issue, documents):

    return {
        "persona": persona,
        "issue": issue,
        "documents_used": documents,
        "attempted_steps": [],
        "recommendation": "Human support review required"
    }