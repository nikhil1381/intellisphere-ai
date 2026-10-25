from openai import AzureOpenAI
from dotenv import load_dotenv
from src.config.settings import Settings
import os

load_dotenv()

client = AzureOpenAI(
    api_key=Settings.OPENAI_API_KEY,
    api_version="2024-12-01-preview",
    azure_endpoint=Settings.OPENAI_ENDPOINT
)

response = client.chat.completions.create(
    model=Settings.OPENAI_DEPLOYMENT,
    messages=[
        {
            "role": "system",
            "content": "You are IntelliSphere AI."
        },
        {
            "role": "user",
            "content": "Introduce yourself."
        }
    ]
)

print("\n=== IntelliSphere AI ===\n")
print(response.choices[0].message.content)