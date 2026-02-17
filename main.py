from dotenv import load_dotenv
from langchain_groq import ChatGroq
import asyncio
from mcp_use import MCPAgent,MCPClient 
import os 

async def run_memory_chat():
    """Run a chat using MCPAgent's built-in conversation memory."""
    load_dotenv()
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    config_file = "browser_mcp.json"

    print("Initializing chat....")

    client = MCPClient.from_config_file(config_file)
    llm = ChatGroq(model="qwen/qwen3-32b")

    agent = MCPAgent(llm=llm,
                     client=client,
                     max_steps=5,
                     memory_enabled=True)
    
    print("\n===== Interactive MCP Chat =====")
    print("Type 'exit' or 'quit' to the end the conversation")
    print("Type 'clear' to clear the conversation history")
    print("=================================\n")

    try:
        while True:
            user_input = input("\nYou:")

            if user_input.lower() in ['exit','quit']:
                print("Ending the conversation")
                break 

            if user_input.lower() == "clear":
                agent.clear_conversation_history()
                print("Conversation history cleared")
                continue 

            print("\n Assistant: ",end="",flush=True)

            try:
                response = await agent.run(user_input)
                print(response)
            except Exception as e:
                print("\nError:",e)
    
    finally:
        if client and client.sessions:
            await client.close_all_sessions()

if __name__ == "__main__":
    asyncio.run(run_memory_chat())
