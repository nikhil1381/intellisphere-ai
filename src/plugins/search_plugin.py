from src.services.search_query_service import get_search_client
from src.services.logger_service import LoggerService

class SearchPlugin:
    
    def search_documents(self, query: str) -> str:
        LoggerService.log(
            f"Searching for: {query}"
        )
        client = get_search_client()

        results = client.search(
            search_text=query,
            top=1
        )

        for result in results:

            if "snippet" in result:
                return result["snippet"]

            return str(result)

        return "No results found."