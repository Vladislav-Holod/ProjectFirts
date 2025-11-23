import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

Model=genai.GenerativeModel('gemini-2.5-flash')
Promt=Model.start_chat(history=[])

