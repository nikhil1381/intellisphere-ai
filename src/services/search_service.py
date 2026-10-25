import os

from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient
from src.config.settings import Settings

def get_search_client():

    endpoint = Settings.SEARCH_ENDPOINT

    credential = AzureKeyCredential(
        Settings.SEARCH_API_KEY
    )

    client = SearchIndexClient(
        endpoint=endpoint,
        credential=credential
    )

    return client