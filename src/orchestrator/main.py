from importlib import import_module

try:
    load_dotenv = import_module("dotenv").load_dotenv
except ModuleNotFoundError:
    def load_dotenv(*args, **kwargs):
        return False

import os

load_dotenv()

endpoint = os.getenv("AZURE_AI_FOUNDRY_ENDPOINT")
model = os.getenv("MODEL_DEPLOYMENT_NAME")

print("IntelliSphere AI")
print(f"Endpoint: {endpoint}")
print(f"Model: {model}")