import json
import os

class SimpleMemory:
    def __init__(self, path="memory.json"):
        self.path = path
        self.history = self.load()

    def add(self, user, bot):
        self.history.append({"role": "user", "content": user})
        self.history.append({"role": "assistant", "content": bot})
        self.save()

    def load(self):
        if os.path.exists(self.path):
            with open(self.path, "r") as f:
                return json.load(f)
        return []

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.history, f, indent=2)

    def get_history(self, limit=10):
        return self.history[-limit:]