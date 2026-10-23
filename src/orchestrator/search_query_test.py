from dotenv import load_dotenv

load_dotenv()

from src.services.search_query_service import get_search_client

client = get_search_client()

results = client.search(
    search_text="vacation"
)

print("\n=== Search Results ===\n")

for result in results:

    print("=" * 50)

    for key, value in result.items():

        if "vector" not in key.lower():
            print(f"{key}: {value}")