from orchestrator import Orchestrator

bot = Orchestrator()

print("🧠 Mini LLM Chat (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    reply = bot.run(user_input)
    print(f"Bot: {reply}\n")