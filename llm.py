import re


class SimpleLLM:
    def __init__(self):
        self.knowledge = {
            r"capital of (\w+)": self.answer_capital,
            r"your name": lambda _: "I'm a fake LLM built for testing!",
            r"hello|hi": lambda _: "Hello! How can I help you today?",
        }

    def chat(self, messages):
        user_input = messages[-1]["content"].lower()

        for pattern, handler in self.knowledge.items():
            match = re.search(pattern, user_input)
            if match:
                return handler(match)

        return "Sorry, I don't know the answer to that yet!"

    def answer_capital(self, match):
        country = match.group(1).capitalize()
        capitals = {
            "France": "Paris",
            "Germany": "Berlin",
            "India": "New Delhi",
            "Japan": "Tokyo"
        }
        return f"The capital of {country} is {capitals.get(country, 'unknown')}."