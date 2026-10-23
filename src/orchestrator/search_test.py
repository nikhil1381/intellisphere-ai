from dotenv import load_dotenv

load_dotenv()

from src.services.search_service import get_search_client

client = get_search_client()

print("\n=== Azure AI Search Indexes ===\n")

for index in client.list_indexes():
    print(index.name)