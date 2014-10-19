import unittest
from Store import Product
from Store import Smartphone
from Store import Laptop
from Store import Store


class StoreTest(unittest.TestCase):

    def test_real_product_profit(self):
        new_product = Product("Mock",50, 100)
        self.assertEqual(50, new_product.profit())

    def test_sell_product(self):
        new_store = Store("Laptop.bg")
        new_product = Smartphone('Hack Phone', 500, 820, 7, 10)
        new_store.load_new_products(new_product,2)
        self.assertTrue(new_store.sell_product(new_product))
        self.assertTrue(new_store.sell_product(new_product))
        self.assertFalse(new_store.sell_product(new_product))


    def test_total_income(self):
        new_store = Store("Laptop.bg")
        new_product = Product('Mock',50,100)
        new_store.load_new_products(new_product,2)
        self.assertEqual(100,new_store.total_income())





if __name__ == '__main__':
    unittest.main()
