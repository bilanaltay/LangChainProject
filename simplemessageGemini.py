import base64
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types


def generate():

    load_dotenv()
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    # Basit mesaj gönder
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="AI nasıl çalışır?"
    )

    print("Gemini:", response.text)

if __name__ == "__main__":
    generate()
