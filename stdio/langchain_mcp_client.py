from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
import os
import sys


# Path to the MCP server script
mcp_server_script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mcp_server.py")

# Path to the virtual environment
venv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".venv")


async def main():

    # Create an instance of the MultiServerMCPClient
    client = MultiServerMCPClient(
        # MCP Server Config (JSON)
        {
            "data_fetch_mcp_stdio": {
                "transport": "stdio",
                "command": sys.executable,
                "args": [str(mcp_server_script)],
            }
        }
    )

    # List the tools
    tools = await client.get_tools()
    print("Available tools:", tools)


if __name__ == "__main__":
    asyncio.run(main())