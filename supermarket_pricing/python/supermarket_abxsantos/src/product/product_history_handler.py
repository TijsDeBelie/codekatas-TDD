from datetime import datetime

from src.product.products import Product


class ProductHistoryHandler(object):
    def __init__(self, product: Product, updated_price: float):
        """
        Concerned with adding new product prices to the history
        >>> sweet_potato_product = Product(name='beans', cost=0.50, price=1.00, sku='003', stock_quantity=100, unit='Kg')
        >>> now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        >>> ProductHistoryHandler(product=sweet_potato_product, updated_price=1.25).change_product_price()
        >>> sweet_potato_product.price = 1.25
        >>> sweet_potato_product.price_history = [(1.25, now)]
        """
        self._validate_parameters(product, updated_price)
        self.product = product
        self.updated_price = updated_price

    @staticmethod
    def _validate_parameters(product: Product, updated_price: float):
        if not product:
            raise TypeError('A product must be provided')
        if not updated_price:
            raise TypeError('A new price must be provided')

    def _update_price(self):
        """Updates the price of the product"""
        self.product.price = self.updated_price

    def _update_history(self):
        """Updates the price history of the product"""
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        price_history_entry = (self.updated_price, now)
        self.product.price_history.append(price_history_entry)

    def change_product_price(self):
        """Updates the price and price history of the product"""
        self._update_price()
        self._update_history()
