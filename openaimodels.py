import os
import openai

from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
models = openai.Model.list()

if __name__ == "__main__":
    print("Accessible model names:")
    print([model.id for model in models["data"]])