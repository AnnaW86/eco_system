import unittest

from src.bear import Bear
from src.fish import Fish
from src.river import River

class TestFish(unittest.TestCase):
    def setUp(self):
        self.fish = Fish("Main Fishy")

    def test_fish_has_name(self):
        self.assertEqual("Main Fishy", self.fish.name)