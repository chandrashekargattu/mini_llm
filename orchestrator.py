from llm import SimpleLLM
from memory import SimpleMemory
from prompts import build_prompt

class Orchestrator:
    def __init__(self):
        self.llm = SimpleLLM()
        self.memory = SimpleMemory()

    def run(self, user_input):
        history = self.memory.get_history()
        history.append(build_prompt(user_input))

        reply = self.llm.chat(history)
        self.memory.add(user_input, reply)

        return reply