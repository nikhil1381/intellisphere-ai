from openai import AzureOpenAI
from dotenv import load_dotenv

import os

load_dotenv()


class RouterAgent:

    def __init__(self):

        self.client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version="2024-12-01-preview",
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )

    def determine_agent(self, question):

        response = self.client.chat.completions.create(
            model=os.getenv("MODEL_DEPLOYMENT_NAME"),
            messages=[
                {
                    "role": "system",
                    "content": """
                    You are an intelligent router.

                    Return only one value:

                    HR
                    IT
                    FINANCE

                    No explanation.
                    """
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        return response.choices[0].message.content.strip()