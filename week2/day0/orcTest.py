import unittest
from orc import Orc

class OrcTest (unittest.TestCase):
    def setUp(self):
        self.orc = Orc("The DragonSlayer killer", 100, 1.5)

    def test_hero_init(self):

        self.assertEqual(self.orc.name, "The DragonSlayer killer")
        self.assertEqual(self.orc.maxhealth, 100)
        self.assertEqual(self.orc.berserk_factor, 1.5)

    def test_get_health(self):

        self.assertEqual(self.orc.get_health(), 100)

    def test_is_alive_return_false(self):

        self.orc.maxhealth = 0
        self.assertFalse(self.orc.is_alive())

    def test_is_alive(self):

        self.assertTrue(self.orc.is_alive())

    def test_take_damage(self):

        self.assertEqual(80, self.orc.take_damage(20))

    def test_take_damage_more_than_health(self):

        self.assertEqual(0,self.orc.take_damage(120))

    def test_take_healing_to_dead_person(self):

        self.orc.maxhealth = 0
        self.assertFalse(self.orc.take_healing(20))

    def test_take_healing_more_than_enough(self):

        self.orc.maxhealth = 90
        self.assertFalse(self.orc.take_healing(100))

    def test_take_healing_true(self):

        self.orc.maxhealth = 40

    def test_berserk_factor_below_one(self):
        self.orc.berserk_factor = 0.5
        self.assertEqual(self.orc.berserk_factor_check(), 1)

    def test_berserk_factor_above_two(self):
        self.orc.berserk_factor = 2.15
        self.assertEqual(self.orc.berserk_factor_check(), 2)


if __name__ == '__main__':
    unittest.main()
