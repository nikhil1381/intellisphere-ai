from dotenv import load_dotenv

load_dotenv()

from src.plugins.search_plugin import SearchPlugin

plugin = SearchPlugin()

response = plugin.search_documents(
    "vacation policy"
)

print("\n=== Search Plugin Response ===\n")
print(response)
