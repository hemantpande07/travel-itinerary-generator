import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY not set in .env file")

# Configure Gemini API
genai.configure(api_key=api_key)

# Use new Gemini flash model
model = genai.GenerativeModel("models/gemini-flash-latest")

def generate_itinerary(source, destination, start_date, end_date, no_of_day):
    prompt = f"""
    Generate a detailed and practical day-by-day itinerary.
    From: {source}
    To: {destination}
    Dates: {start_date} to {end_date}
    Total days: {no_of_day}

    Include:
    - Transportation
    - Best sightseeing spots
    - Food recommendations
    - Budget (INR)
    - Travel tips
    - Weather considerations

    Format clearly in markdown.
    """

    try:
        response = model.generate_content(prompt)

        if not response or not response.text:
            print("⚠️ Empty Gemini response")
            return "Unable to generate itinerary at the moment."

        return response.text

    except Exception as e:
        print("❌ Gemini Error:", e)
        return "Unable to generate itinerary at the moment."
