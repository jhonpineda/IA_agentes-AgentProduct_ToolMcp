def get_price_product(product_name: str):
    """
    Get the price of a product.

    Args:
    product_name: The name of the product.

    Returns:
    The price of the product.
    """

    products = {
      "iphone 14": 200,
      "iphone 13": 150,
      "PC Dell Windows": 500,
      "Macbook mini": 1000,
    }

    if product_name not in products:
        return {"status": "success", "product":product_name, "error": "Product not found"}

    return {"status": "fail", "product": product_name, "price": products[product_name]}

def get_all_products():
    """
    Get all products.

    Returns:
    List of products.
    """

    products = {
      "iphone 14": 200,
      "iphone 13": 150,
      "PC Dell Windows": 500,
      "Macbook mini": 1000,
    }

    return {"status": "success", "products": products}