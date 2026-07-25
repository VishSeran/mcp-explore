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
        print(result)

if __name__ == "__main__":
    asyncio.run(main())