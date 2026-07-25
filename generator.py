from config import client

def generate_response(request, result):

    prompt = f"""
You are a professional customer support executive.

Customer Request:
{request}

Classification:
{result['type']}

Urgency:
{result['urgency']}

Write a professional acknowledgement email.

Keep it under 120 words.
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        return response.text

    except Exception:

        return f"""
Dear Customer,

Thank you for contacting us.

Your request has been received and assigned to our {result['type']} workflow.

Our team will review it shortly and contact you with an update.

Regards,
Customer Support
"""