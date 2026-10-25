from dotenv import load_dotenv

load_dotenv()

from src.config.settings import Settings

print("OpenAI Endpoint:")
print(Settings.OPENAI_ENDPOINT)

print("\nDeployment:")
print(Settings.OPENAI_DEPLOYMENT)

print("\nSearch Endpoint:")
print(Settings.SEARCH_ENDPOINT)