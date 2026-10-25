import os

from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from src.config.settings import Settings

def get_search_client():

    return SearchClient(
        endpoint=Settings.SEARCH_ENDPOINT,
        index_name="ks-intellisphere-corpdocs-index",
        credential=AzureKeyCredential(
            Settings.SEARCH_API_KEY
        )
    )