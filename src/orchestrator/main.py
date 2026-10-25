from importlib import import_module
from src.config.settings import Settings

try:
    load_dotenv = import_module("dotenv").load_dotenv
except ModuleNotFoundError:
    def load_dotenv(*args, **kwargs):
        return False

import os

load_dotenv()

endpoint = Settings.OPENAI_ENDPOINT
model = Settings.OPENAI_DEPLOYMENT

print("IntelliSphere AI")
print(f"Endpoint: {endpoint}")
print(f"Model: {model}")