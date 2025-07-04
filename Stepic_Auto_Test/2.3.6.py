
class MoneyBox:
    def __init__(self, capacity):
        self.capacity = 0
        self.coins = 0

    def can_add(self, v):
        return self.coins + v <= self.capacity
    def add(self, v):
        self.coins += v