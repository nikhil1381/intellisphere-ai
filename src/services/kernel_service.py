import os

from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from src.config.settings import Settings


def create_kernel():

    print("Endpoint:", Settings.OPENAI_ENDPOINT)
    print("Deployment:", Settings.OPENAI_DEPLOYMENT)

    kernel = Kernel()

    kernel.add_service(
        AzureChatCompletion(
            deployment_name=Settings.OPENAI_DEPLOYMENT,
            endpoint=Settings.OPENAI_ENDPOINT,
            api_key=Settings.OPENAI_API_KEY,
            api_version="2024-12-01-preview"
        )
    )

    return kernel