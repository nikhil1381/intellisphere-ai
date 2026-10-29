import os
from dotenv import load_dotenv

load_dotenv()

class Settings:

    OPENAI_ENDPOINT = os.getenv(
        "AZURE_OPENAI_ENDPOINT"
    )

    OPENAI_API_KEY = os.getenv(
        "AZURE_OPENAI_API_KEY"
    )

    OPENAI_DEPLOYMENT = os.getenv(
        "MODEL_DEPLOYMENT_NAME"
    )

    SEARCH_ENDPOINT = os.getenv(
        "SEARCH_ENDPOINT"
    )

    SEARCH_API_KEY = os.getenv(
        "SEARCH_API_KEY"
    )