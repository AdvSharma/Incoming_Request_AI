import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

try:
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="Reply with exactly the word SUCCESS"
    )

    print("\n===== RESPONSE =====")
    print(response.text)
    print("====================")

except Exception as e:
    print("\n===== ERROR =====")
    print(type(e).__name__)
    print(e)
    print("=================")