import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access your API key using os.environ
openai.api_key = os.environ.get("OPENAI_API_KEY")

content = open('*Path to txt file*', 'r').read()

# Generate response based on Text File - GPT4
def generate_content_response(input_text):
    # Generate an response based on file
    response = openai.ChatCompletion.create(
        model="gpt-4",  # You can also use GPT-3.5-turbo if preferred.
        messages=[
      {
        "role": "system",
        "content": f"'{content}' \n*Give Necessary Prompts*"
      },
      {
        "role": "user",
        "content": f"*Give Necessary Prompts* '{input_text}' "
      }],
        max_tokens=1000,
    )

    return response.choices[0].message.content
