import os

from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient


def get_search_client():

    return SearchClient(
        endpoint=os.getenv("SEARCH_ENDPOINT"),
        index_name="ks-intellisphere-corpdocs-index",
        credential=AzureKeyCredential(
            os.getenv("SEARCH_API_KEY")
        )
    )