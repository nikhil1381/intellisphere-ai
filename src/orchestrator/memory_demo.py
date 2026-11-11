from dotenv import load_dotenv

load_dotenv()

from src.orchestrator.intellisphere_copilot import IntelliSphereCopilot

copilot = IntelliSphereCopilot()

copilot.ask(
    "How many vacation days do employees receive?"
)

copilot.ask(
    "What is the parental leave policy?"
)

print("\n=== Memory ===\n")

for item in copilot.show_memory():

    print(item)