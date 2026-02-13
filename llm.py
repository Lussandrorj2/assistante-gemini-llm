import os
from dotenv import load_dotenv
from google import genai
import streamlit as st


def get_api_key():
    if "GEMINI_API_KEY" in st.secrets:
        return st.secrets["GEMINI_API_KEY"]
    return os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=get_api_key())



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


