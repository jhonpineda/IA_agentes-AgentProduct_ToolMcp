from google.adk.agents.llm_agent import Agent
from .tools import get_price_product, get_all_products
from dotenv import load_dotenv
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset

load_dotenv()

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    instruction="""
      Eres un analista de mercado.
      - Ayudas a los usuarios a conocer precios y comparar productos
      - Tu respuesta de forma cordial y pensando siempre en vender
      - Si no el producto no existe, di que no se tiene en inventario
      - NO inventes productos si no están en get_all_products
      - Para comprar un producto usa la tool buy_product
    """,
    tools=[
        get_price_product,
        MCPToolset(  # Pin selection to current chat prompt
            connection_params=StreamableHTTPServerParams(
                url="http://127.0.0.1:8001/mcp"
            )
        )
    ]
)
