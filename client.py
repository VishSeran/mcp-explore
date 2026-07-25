# client.py
import asyncio
from fastmcp import Client
from fastmcp.client.transports import StdioTransport

stdio_transport = StdioTransport(
    command="npx",
    args=["-y", "@upstash/context7-mcp"]
)

stdio_client = Client(stdio_transport) 


async def main():
    async with stdio_client as client:
        result = await client.list_tools()
        print("number of tools: ", len(result))  
        
        for i,tool in enumerate(result):
            print(f"tool {i+1} name: ", tool.name)
            print(f"\ntool {i+1} description: ", tool.description)
            print(f"\ntool {i+1} schema: ", tool.inputSchema)
            
            
        print("\n\n============Tool Interactions============\n\n")
        
        response = await client.call_tool(
            
            "resolve-library-id", {
                "libraryName": "fastmcp",
                "query": "How to create an MCP server using FastMCP"
            }
        )
        
        print("Response: ", response.content[0].text)
        


if __name__ == "__main__":
    asyncio.run(main())