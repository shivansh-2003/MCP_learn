import os
import sys
from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters
import asyncio

MCP_SERVER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mcp_server.py")
print(MCP_SERVER_PATH)

# create server params
server_params = StdioServerParameters(
    command=sys.executable,
    args=[str(MCP_SERVER_PATH)],
    env=None,
)

# Create a Client Session
async def main():

    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()
            # Fetch the tools
            tools = await session.list_tools()
            print("Available tools:", tools)

            # Use the process tool
            result = await session.call_tool("process", arguments={"path": MCP_SERVER_PATH})
            print("Result:", result)


if __name__ == "__main__":
    asyncio.run(main())
