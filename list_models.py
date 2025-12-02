import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY not found in .env file.")

# Configure
genai.configure(api_key=api_key)

# Fetch models
models = genai.list_models()

print("Available Gemini models:")
for model in models:
    # Only show models that support text generation
    if "generateContent" in model.supported_generation_methods:
        print("-", model.name)
