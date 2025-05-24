import os
import requests
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def get_gemini_response(prompt: str) -> str:
    if not GEMINI_API_KEY:
        return "Gemini API key not found."
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    headers = {"Content-Type": "application/json"}
    params = {"key": GEMINI_API_KEY}
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    try:
        response = requests.post(url, headers=headers, params=params, json=data)
        response.raise_for_status()
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"Gemini API error: {e}"

def classify_query(query: str) -> str:
    if any(word in query.lower() for word in ["solve", "calculate", "equation", "+", "-", "*", "/", "math"]):
        return "math"
    elif any(word in query.lower() for word in ["physics", "force", "gravity", "speed", "mass", "velocity"]):
        return "physics"
    else:
        return "unknown"
