#Practice class creation by creating a product catalog

class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_product_stock_value(self):
        value = self.price * self.quantity
        print(f"The total value of the product {self.name} in stock is {value} shillings")

salt = Product ("Chumvi",10, 10000)
salt.get_total_product_stock_value()