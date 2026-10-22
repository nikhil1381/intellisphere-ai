import asyncio
from dotenv import load_dotenv

from semantic_kernel.functions import KernelArguments

from src.services.kernel_service import create_kernel

load_dotenv()

kernel = create_kernel()


async def main():

    result = await kernel.invoke_prompt(
        "Introduce yourself as IntelliSphere AI in three sentences.",
        arguments=KernelArguments()
    )

    print("\n=== Semantic Kernel Response ===\n")
    print(result)

asyncio.run(main())