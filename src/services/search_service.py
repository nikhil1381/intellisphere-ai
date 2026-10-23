import os

from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient

def get_search_client():

    endpoint = os.getenv("SEARCH_ENDPOINT")

    credential = AzureKeyCredential(
        os.getenv("SEARCH_API_KEY")
    )

    client = SearchIndexClient(
        endpoint=endpoint,
        credential=credential
    )

    return client