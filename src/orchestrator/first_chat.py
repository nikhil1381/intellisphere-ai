from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-12-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

response = client.chat.completions.create(
    model=os.getenv("MODEL_DEPLOYMENT_NAME"),
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