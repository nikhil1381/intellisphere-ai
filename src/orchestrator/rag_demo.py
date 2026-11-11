from dotenv import load_dotenv

load_dotenv()

from src.plugins.rag_plugin import RAGPlugin

rag = RAGPlugin()

answer = rag.answer(
    "How many vacation days do employees receive?"
)

print("\n=== RAG Response ===\n")

print(answer)