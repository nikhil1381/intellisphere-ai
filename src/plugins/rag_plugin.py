from src.plugins.search_plugin import SearchPlugin

from openai import AzureOpenAI
from dotenv import load_dotenv
from src.config.settings import Settings
import os

load_dotenv()


class RAGPlugin:

    def __init__(self):

        self.search_plugin = SearchPlugin()

        self.client = AzureOpenAI(
            api_key=Settings.OPENAI_API_KEY,
            api_version="2024-12-01-preview",
            azure_endpoint=Settings.OPENAI_ENDPOINT
        )

    def answer(self, question):

        context = self.search_plugin.search_documents(
            question
        )

        response = self.client.chat.completions.create(
            model=Settings.OPENAI_DEPLOYMENT,
            messages=[
                {
                    "role": "system",
                    "content": """
                    Answer ONLY using the provided context.
                    If the answer is not present,
                    say that it was not found.
                    """
                },
                {
                    "role": "user",
                    "content": f"""
                    Context:

                    {context}

                    Question:

                    {question}
                    """
                }
            ]
        )

        return response.choices[0].message.content