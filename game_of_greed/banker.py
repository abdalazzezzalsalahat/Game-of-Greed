class Banker:

    def __init__(self):
        self.balance = 0
        self.shelved = 0

    def __str__(self):
        return self.balance

    def shelf(self, int):
        
        self.shelved += int
        return self.shelved

    def bank(self):
        self.balance = 0
        self.balance += self.shelved
        self.clear_shelf()

        return self.balance

    def clear_shelf(self):
        self.shelved = 0
        return self.shelved

