class Banker:

    def __init__(self):
        self.balance = 0
        self.shelved = 0

    def __str__(self):
        return self.balance

    def shelf(self, int):
        self.shelved += int

    def bank(self):
        depo = self.shelved
        self.balance = 0
        self.balance += self.shelved
        self.shelved = 0
        return depo

    def clear_shelf(self):
        self.shelved = 0

