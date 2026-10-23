from src.plugins.search_plugin import SearchPlugin


class HRAgent:

    def __init__(self):
        self.search_plugin = SearchPlugin()

    def answer(self, question):
        return self.search_plugin.search_documents(question)