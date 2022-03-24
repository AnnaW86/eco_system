import unittest

from src.bear import Bear
from src.fish import Fish
from src.river import River

class TestRiver(unittest.TestCase):
    def setUp(self):
        self.river = River("Amazon")
        self.fish1 = Fish("Main Fishy")
        self.fish2 = Fish("Fishy2")
        self.fish3 = Fish("Fishy3")
        

    def test_has_name(self):
        self.assertEqual("Amazon", self.river.name)
    

    def test_has_fish(self):
        self.river.add_fish(self.fish1)
        self.river.add_fish(self.fish2)
        self.river.add_fish(self.fish3)
        self.assertEqual(3, len(self.river.fish_stock))
    
    def test_loses_random_fish_to_bear(self):
        bear = Bear("Yogi", "grizzly")
        self.river.add_fish(self.fish1)
        self.river.add_fish(self.fish2)
        self.river.add_fish(self.fish3)
        self.river.lose_fish_to_bear(bear)
        self.assertEqual(2, len(self.river.fish_stock))
        self.assertEqual(1, len(bear.stomach)) 


    
    def test_count_fish(self):
        self.assertEqual(0, self.river.count_fish())