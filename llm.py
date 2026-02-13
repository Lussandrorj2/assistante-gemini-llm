import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def ask_llm(messages):
    conversation = ""
    for msg in messages:
        conversation += f"{msg['role'].upper()}: {msg['content']}\n"

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=conversation,
    )

    return response.text
