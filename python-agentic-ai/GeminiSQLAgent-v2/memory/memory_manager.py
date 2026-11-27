import json

class MemoryManager:

    FILE = "memory/chat_memory.json"

    def save(self, user, assistant):

        data = self.load()

        data.append({
            "user": user,
            "assistant": assistant
        })

        with open(self.FILE, "w") as f:
            json.dump(data, f, indent=4)

    def load(self):

        try:
            with open(self.FILE, "r") as f:
                return json.load(f)

        except:
            return []