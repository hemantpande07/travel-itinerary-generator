# import google.generativeai as palm
# import os
# from dotenv import load_dotenv

# # Load the environment variables
# load_dotenv()
# palm_api_key = os.environ.get("PALM_API_KEY")


# # Create a config.
# palm.configure(api_key=palm_api_key)
# model = palm.GenerativeModel(model_name="gemini-1.5-flash-8b-exp-0924")
# # print(list(palm.list_models()))


# # Generate some text.
# def generate_itinerary(source, destination, start_date, end_date, no_of_day):
#     prompt = f"Generate a personalized trip itinerary for a {no_of_day}-day trip from {source} to {destination} on {start_date} to {end_date}, with an optimum budget (Currency:INR)."
#     response = model.generate_content(prompt)
#     return(response.text)
import google.generativeai as palm
import os
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()
palm_api_key = os.environ.get("PALM_API_KEY")

if not palm_api_key:
    raise RuntimeError("PALM_API_KEY not set. Please add it to your .env file.")

# Configure PaLM API
palm.configure(api_key=palm_api_key)

# Initialize the model
model = palm.GenerativeModel(model_name="gemini-1.5-flash-8b-exp-0924")

def generate_itinerary(source, destination, start_date, end_date, no_of_day):
    """
    Generate a personalized trip itinerary using PaLM API.
    """
    prompt = (
        f"Generate a personalized trip itinerary for a {no_of_day}-day trip "
        f"from {source} to {destination} from {start_date} to {end_date}, "
        f"with an optimum budget (Currency: INR)."
    )
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # Print the real error to the terminal for debugging
        print("Error generating itinerary:", e)
        # Optionally, return a fallback message instead of crashing
        return "Unable to generate itinerary at the moment."
