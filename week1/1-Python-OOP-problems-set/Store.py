class Product:

    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):

        return self.final_price -self.stock_price



class Laptop(Product):

    def __init__(self, name, stock_price, final_price, ram):
        super().__init__(name, age, weight)
        self.ram = ram

class Smartphone(Product):
    def __init__(self, name, stock_price, final_price, display_size,mega_pixels):
        super().__init__(name, stock_price, final_price)
        self.display_size = display_size
        self.mega_pixels = mega_pixels


class Store:
    def __init__(self,name):

        self.name = name
        self.items = {}
        self.income = 0



    def load_new_products(self, product, count):
        self.product = product
        self.count = count
        if product in self.items:
            self.items[product] += count
        else:
            self.items[product] = count


    def __str__(self):
        return "Name: {} ".format(self.name)


    def list_products(self, product_class):
        #return false or true
        self.product_class = product_class
        for item in self.items:
            if isinstance(item, product_class):
                print(item)

    def sell_product(self, product):

        if product in self.items and self.items[product] > 0:
            self.items[product] -= 1
            self.income += product.profit()
            return True

        return False

    def total_income(self):
        return self.income


store = Store('Laptop.bg')
smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
print(smarthphone.profit())
store.load_new_products(smarthphone, 2)
print(store.sell_product(smarthphone)) # True
print(store.sell_product(smarthphone)) # True
print(store.sell_product(smarthphone)) # False
#
print(store.total_income())#640
