from entity import Entity
import unittest


class TestHeroEnity(unittest.TestCase):

    def setUp(self):

        self.hero = Hero("Bron", 100, "DragonSlayer")
