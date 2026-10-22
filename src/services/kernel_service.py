import os

from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion


def create_kernel():

    print("Endpoint:", os.getenv("AZURE_OPENAI_ENDPOINT"))
    print("Deployment:", os.getenv("MODEL_DEPLOYMENT_NAME"))

    kernel = Kernel()

    kernel.add_service(
        AzureChatCompletion(
            deployment_name=os.getenv("MODEL_DEPLOYMENT_NAME"),
            endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version="2024-12-01-preview"
        )
    )

    return kernel