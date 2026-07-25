import json

from config import client
from prompts import CLASSIFICATION_PROMPT


def classify_request(request):

    prompt = CLASSIFICATION_PROMPT.format(
        request=request
    )

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    text = response.text.strip()

    if text.startswith("```"):
        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

    return json.loads(text)