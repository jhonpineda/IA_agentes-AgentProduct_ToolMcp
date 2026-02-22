from fastmcp import FastMCP
import asyncio

mcp = FastMCP("product-mcp")

products = {
    "iphone 14": 200,
    "iphone 13": 150,
    "PC Dell Windows": 500,
    "Macbook mini": 1000,
}

@mcp.tool
def get_products() -> dict[str, int]:
    return products

async def main():
    # Use run_async() in async contexts
    await mcp.run_async(transport="http", host="127.0.0.1", port=8001)

if __name__ == "__main__":
    # Start an HTTP server on port 8000
    asyncio.run(main())