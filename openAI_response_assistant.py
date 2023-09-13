import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access your API key using os.environ
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Summarization tool
def generate_summary(query):
    
    # Generate assistant's response
    assistant_response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=f"Please provide a concise summary of the following text:  '{query}'",
    max_tokens=250,  # You can adjust max_tokens to control the length of the summary.
)

    return assistant_response.choices[0].text

# Elaboration tool
def generate_elaboration(input_text):
    # Generate an elaborate response
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can also use GPT-3.5-turbo if preferred.
        prompt=f"Elaborate on the following: '{input_text}'",
        max_tokens=1000,
    )

    return response.choices[0].text

# Techno Savvy 
def generate_response_techno(input_text):
    # Generate assistant's response
    assistant_response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=f"'{input_text}'\n Provide response as a techno savvy person will answer",
    max_tokens=1000,  # You can adjust max_tokens to control the length of the summary.
)

    return assistant_response.choices[0].text

# Salesy 
def generate_response_salesy(input_text):
    # Generate assistant's response
    assistant_response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=f"'{input_text}'\n Provide response as a sales-minded person will answer",
    max_tokens=1000,  # You can adjust max_tokens to control the length of the summary.
)

    return assistant_response.choices[0].text

# Factual
def generate_response_factual(input_text):
    # Generate assistant's response
    assistant_response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=f"'{input_text}'\n Provide response as a facts-oriented person will answer",
    max_tokens=1000,  # You can adjust max_tokens to control the length of the summary.
)

    return assistant_response.choices[0].text

# Bullet Points
def generate_bullet_list(input_text):
    # Generate assistant's response
    assistant_response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=f"Please provide a response of the following text in bullet list/bullet points:  '{input_text}'",
    max_tokens=250,  # You can adjust max_tokens to control the length of the summary.
)

    return assistant_response.choices[0].text