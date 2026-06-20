def classify_persona(query):
    query = query.lower()

    technical_keywords = [
        "api",
        "token",
        "authentication",
        "database",
        "logs",
        "server",
        "configuration",
        "error"
    ]

    executive_keywords = [
        "business",
        "impact",
        "operations",
        "timeline",
        "revenue"
    ]

    if any(word in query for word in technical_keywords):
        return "Technical Expert"

    if any(word in query for word in executive_keywords):
        return "Business Executive"

    return "Frustrated User"