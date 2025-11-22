from dotenv import load_dotenv
from google import genai
from google.genai import types
import os

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def start_response(message):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"{message}",
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0) # Disables thinking
        ),
    )
    return response.text
