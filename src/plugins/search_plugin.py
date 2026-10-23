from src.services.search_query_service import get_search_client


class SearchPlugin:

    def search_documents(self, query: str) -> str:

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