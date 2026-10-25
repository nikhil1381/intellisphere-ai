import os


class Settings:

    OPENAI_ENDPOINT = os.getenv(
        "AZURE_OPENAI_ENDPOINT"
    )

    OPENAI_DEPLOYMENT = os.getenv(
        "MODEL_DEPLOYMENT_NAME"
    )

    SEARCH_ENDPOINT = os.getenv(
        "SEARCH_ENDPOINT"
    )