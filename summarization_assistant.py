import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access your API key using os.environ
openai.api_key = os.environ.get("OPENAI_API_KEY")


def generate_response(query):
    
    # Generate assistant's response
    assistant_response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=f"Please provide a concise summary of the following text:  '{query}'",
    max_tokens=250,  # You can adjust max_tokens to control the length of the summary.
)

    return assistant_response.choices[0].text