class Bear:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.stomach = []

# Method 1 for taking fish from the river - select specific fish to eat and then remove from fish_stock.
    def eat_fish(self, fish):
        self.stomach.append(fish)
    
    def take_specific_fish_from_river(self, river):
        for fish in self.stomach:
            river.fish_stock.remove(fish)

# Method 2 for taking fish from the river - take a random fish and eat it.
    def take_random_fish_from_river(self, river):
        random_fish = river.lose_fish()
        self.stomach.append(random_fish)
    
### Extension methods
    def roar(self):
        return "ROOOAAAAARRRRRR!!!!!"
    
    def count_food(self):
        return len(self.stomach)