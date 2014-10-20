from entity import Entity
import unittest


class TestEntity(unittest.TestCase):

    def setUp(self):
        self.entity = Hero("Bron", 100, "DragonSlayer")

    def test_hero_init(self):
        self.assertEqual(self.entity.name, "Bron")
        self.assertEqual(self.entity.health, 100)
        self.assertEqual(self.entity.nickname, "DragonSlayer")

    def test_known_as(self):
        self.assertEqual(self.entity.known_as(), "Bron the DragonSlayer")

    def test_get_health(self):
        self.assertEqual(self.entity.get_health(), 100)

    def test_is_alive(self):
        self.assertTrue(self.entity.is_alive())
        self.entity.health = 0
        self.assertFalse(self.entity.is_alive())

    def test_take_damage(self):
        self.entity.take_damage(50)
        self.assertEqual(50, self.entity.get_health())
        self.entity.take_damage(10)
        self.assertEqual(40, self.entity.get_health())
        self.entity.take_damage(25)
        self.assertEqual(15, self.entity.get_health())

    def test_take_healing(self):
        self.assertTrue(self.entity.take_healing(25))
        self.assertEqual(100, self.entity.get_health())
        self.entity.take_damage(40)
        self.assertEqual(60, self.entity.get_health())
        self.assertTrue(self.entity.take_healing(15))
        self.assertEqual(75, self.entity.get_health())
        self.entity.take_damage(100)
        self.assertFalse(self.entity.is_alive())
        self.assertFalse(self.entity.take_healing(100))

    def test_take_healing_dead(self):
        pass

    def test_take_healing_overhealing(self):
        pass


if __name__ == '__main__':
    unittest.main()
