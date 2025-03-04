import google.generativeai as genai
from environs import Env

env = Env()
env.read_env()

genai.configure(api_key=env('GEMINI_KEY'))
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_text(text: str) -> str:
    response = model.generate_content(text)
    return response.text