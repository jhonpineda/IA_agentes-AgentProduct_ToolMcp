from google.adk.agents.llm_agent import Agent
from .tools import get_price_product, get_all_products
from dotenv import load_dotenv
import os

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
    tools=[get_price_product, get_all_products]
)
