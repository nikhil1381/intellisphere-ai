from dotenv import load_dotenv

load_dotenv()

from src.agents.supervisor_agent import SupervisorAgent

agent = SupervisorAgent()

question = "How many vacation days do employees receive?"

answer = agent.route(question)

print("\nQUESTION:")
print(question)

print("\nANSWER:")
print(answer)