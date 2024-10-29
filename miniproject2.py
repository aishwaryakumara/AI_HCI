# Import necessary modules
from openai import OpenAI         # Import OpenAI API
from dotenv import load_dotenv    # Import load_dotenv to load environment variables from .env file
import os                         # Import os to access environment variables

# Load environment variables from the .env file
load_dotenv()

# Initialize OpenAI client with the API key stored in .env file
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")  # Retrieve the API key from the environment
)

# Request to the OpenAI API to generate a creative response in a response variable
response = client.chat.completions.create(
    model="gpt-4o-mini",  # Specify the model to use
    messages=[  # Define the conversation context for the API
        {"role": "system", "content": "You are a creative writer who talks like Dumbledore from Harry Potter. Give me 5 sentences"},
        {"role": "user", "content": "Generate a creative Hello World message"}
    ],
    # max_tokens=100  # (Optional) Specify the maximum number of tokens in the response
)

# Print the generated response to the console
print(response.choices[0].message.content)