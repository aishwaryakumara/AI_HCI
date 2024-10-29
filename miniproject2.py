from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()

client = OpenAI(
  api_key= os.getenv("OPENAI_API_KEY")
)

# Make a simple API call
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "system", "content": "You are a creative writer who talks like Dumbledore from Harry Potter. Give me 5 sentences"},
              {"role": "user", "content": "Generate a creative Hello World message"}],
    # max_tokens=100
)
print(response.choices[0].message.content)



