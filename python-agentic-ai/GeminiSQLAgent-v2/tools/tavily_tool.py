
from tavily import TavilyClient
from config.settings import Settings

class TavilyTool:

    name = "tavily_tool"

    def __init__(self):

        self.client = TavilyClient(
            api_key=Settings.TAVILY_API_KEY
        )

    def execute(self, query):

        response = self.client.search(
            query=query,
            max_results=5
        )

        return response