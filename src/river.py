class River:
    def __init__(self, name):
        self.name = name
        self.fish_stock = []
    
    
    def add_fish(self, fish):
        self.fish_stock.append(fish)
    

    def lose_fish(self):
        return self.fish_stock.pop()


    def lose_fish_to_bear(self, bear):
        bear.stomach.append(self.fish_stock.pop())
    
### Extension method
    def count_fish(self):
        return len(self.fish_stock)