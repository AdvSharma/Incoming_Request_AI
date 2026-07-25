CLASSIFICATION_PROMPT = """
You are an intelligent request classifier.

Classify the following customer request.

Possible request types:
- Complaint
- Service Request
- General Enquiry

Possible urgency:
- Low
- Medium
- High
- Critical

Return ONLY valid JSON.

Example:

{{
    "type": "Complaint",
    "urgency": "High",
    "confidence": 0.98,
    "reason": "Customer reports duplicate payment."
}}

Customer Request:

{request}
"""