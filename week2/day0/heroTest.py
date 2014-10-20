from hero import Hero
import unittest


class TestHero(unittest.TestCase):

    def setUp(self):
        self.hero = Hero("Bron", 100, "DragonSlayer")

    def test_hero_init(self):
        self.assertEqual(self.hero.name, "Bron")
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.nickname, "DragonSlayer")

    def test_known_as(self):
        self.assertEqual(self.hero.known_as(), "Bron the DragonSlayer")

    def test_get_health(self):
        self.assertEqual(self.hero.get_health(), 100)

    def test_is_alive(self):
        self.assertTrue(self.hero.is_alive())
        self.hero.health = 0
        self.assertFalse(self.hero.is_alive())

    def test_take_damage(self):
        self.hero.take_damage(50)
        self.assertEqual(50, self.hero.get_health())
        self.hero.take_damage(10)
        self.assertEqual(40, self.hero.get_health())
        self.hero.take_damage(25)
        self.assertEqual(15, self.hero.get_health())

    def test_take_healing(self):
        self.assertTrue(self.hero.take_healing(25))
        self.assertEqual(100, self.hero.get_health())
        self.hero.take_damage(40)
        self.assertEqual(60, self.hero.get_health())
        self.assertTrue(self.hero.take_healing(15))
        self.assertEqual(75, self.hero.get_health())
        self.hero.take_damage(100)
        self.assertFalse(self.hero.is_alive())
        self.assertFalse(self.hero.take_healing(100))

    def test_take_healing_dead(self):
        pass

    def test_take_healing_overhealing(self):
        pass


if __name__ == '__main__':
    unittest.main()
