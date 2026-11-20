from fastmcp import FastMCP

mcp=FastMCP()

@mcp.tool()
def fetch():
    """
    This tool fetches the data from the server.
    """ 

    return {'data' : "Hello MCP!"}

@mcp.tool()
def process(path:str):
    return {'data' : f"Processed data at path: {path}"}

if __name__ == "__main__":
    mcp.run(transport="stdio")