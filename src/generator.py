def generate_response(query, persona, context):

    if persona == "Technical Expert":
        return f"""
Technical Support Response

Relevant Information:
{context}

Suggested Root Cause:
Configuration, authentication, or system-level issue.

Troubleshooting Steps:
1. Verify credentials
2. Check logs
3. Validate configuration
4. Retry the operation
"""

    elif persona == "Business Executive":
        return f"""
Business Summary

Issue may affect business operations.

Recommended Action:
Review the documented resolution steps and assign support resources if needed.

Reference:
{context[:300]}
"""

    else:
        return f"""
I understand this issue is frustrating.

Please follow these steps:

{context}

If the issue continues, we can escalate it to a human support representative.
"""