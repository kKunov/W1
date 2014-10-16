class Product:

    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        return self.final_price - self.stock_price


class Laptop(Product):

    def __init__(self, name, stock_price, final_price, discspace, ram):
        super().__init__(name, stock_price, final_price)
        self.discspace = discspace
        self.ram = ram


class Smartphone(Product):

    def __init__(self, name, stock_price, final_price, display_size, mega_pixels):
        super().__init__(name, stock_price, final_price)
        self.display_size = display_size
        self.mega_pixels = mega_pixels


class Store:

    def __init__(self, name):
        self.name = name
        self.product = {}
        self.profit = 0

    def load_new_products(self, product, count):
        if product in self.product:
            self.product[product] += count
        else:
            self.product[product] = count

    def list_of_products(self, product_class=object):
        for product in self.product:
            if isinstance(product, product_class):
                print(product.name)

    def sell_product(self, product):
        if product in self.product and self.product[product] > 0:
            self.product[product] -= 1
            self.profit += product.profit()
            return True
        else:
            return False

    def total_income(self):
        return self.profit


new_store = Store('Lapopt.bg')
new_product = Laptop('HP HackBook', 1000, 1243, 500, 2)
new_store.load_new_products(new_product, 5)
print (new_store.sell_product(new_product))
print (new_store.sell_product(new_product))
print (new_store.sell_product(new_product))
print (new_store.sell_product(new_product))
print(new_store.total_income())
