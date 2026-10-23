from src.plugins.search_plugin import SearchPlugin


class ITAgent:

    def __init__(self):
        self.search_plugin = SearchPlugin()

    def answer(self, question):
        return self.search_plugin.search_documents(question)