import unittest

from src.bear import Bear
from src.fish import Fish
from src.river import River

class TestBear(unittest.TestCase):
    def setUp(self):
        self.bear1 = Bear("Yogi", "grizzly")
        self.fish1 = Fish("Main Fishy")
        self.fish2 = Fish("Fishy2")
        self.fish3 = Fish("Fishy3")
        self.river = River("Amazon")
    
    def test_has_name(self):
        self.assertEqual("Yogi", self.bear1.name)
    
    def test_has_type(self):
        self.assertEqual("grizzly", self.bear1.type)
    
    def test_has_empty_stomach(self):
        self.assertEqual(0, len(self.bear1.stomach))

    def test_eat_fish(self):
        self.bear1.eat_fish(self.fish1)
        self.assertEqual(1, len(self.bear1.stomach))
    
    # Test for Method 1 in src.bear
    def test_takes_specific_fish_from_river(self):
        self.river.add_fish(self.fish1)
        self.river.add_fish(self.fish2)
        self.river.add_fish(self.fish3)
        self.bear1.eat_fish(self.fish2)
        self.bear1.eat_fish(self.fish3)
        self.bear1.take_specific_fish_from_river(self.river)
        self.assertEqual(1, len(self.river.fish_stock))
        self.assertEqual(2, len(self.bear1.stomach))
    
    # Test for Method 2 in src.bear
    def test_takes_random_fish_from_river(self):
        self.river.add_fish(self.fish1)
        self.river.add_fish(self.fish2)
        self.river.add_fish(self.fish3)
        self.bear1.take_random_fish_from_river(self.river)
        self.assertEqual(2, len(self.river.fish_stock))
        self.assertEqual(1, len(self.bear1.stomach))

    def test_roar(self):
        self.assertEqual("ROOOAAAAARRRRRR!!!!!", self.bear1.roar())
    
    def test_food_count(self):
        self.assertEqual(0, self.bear1.count_food())