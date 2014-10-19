import unittest
from CashDesk import *

class CashDeskTest(unittest.TestCase):

    def test_total_zero_when_new_instance_made(self):
        new__desk = CashDesk()
        self.assertEqual(0, new__desk.total())

    def test_total_after_money_take(self):
        new_desk = CashDesk()
        new_desk.take_money({1: 1, 2: 1})
        self.assertEqual(3, new_desk.total())

    def test_can_withdraw_money_all_money(self):
        new_desk = CashDesk()
        new_desk.take_money({1: 1, 2: 1})
        self.assertTrue(True, new_desk.can_withdraw_money(4))



if __name__ == '__main__':
    unittest.main()
