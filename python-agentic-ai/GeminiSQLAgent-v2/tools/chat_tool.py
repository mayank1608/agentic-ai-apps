from services.gemini_service import GeminiService

class ChatTool:

    name = "chat_tool"

    def __init__(self):
        self.gemini = GeminiService()

    def execute(self, question):

        return self.gemini.ask(question)