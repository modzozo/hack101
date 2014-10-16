class Product:

    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        true_profit = int(self.final_price) - int(self.stock_price)
        return true_profit



class Laptop(Product):

    def __init__(self, name, stock_price, final_price, ram):
        super().__init__(name, age, weight)
        self.ram = ram

class Smartphone(Product):
    def __init__(self, name, stock_price, final_price, display_size,mega_pixels):
        super().__init__(name, age, weight)
        self.display_size = display_size
        self.mega_pixels = mega_pixels
