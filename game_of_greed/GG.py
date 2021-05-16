from random import randint, sample

class GameLogic:

    @staticmethod
    def roll (dice):
        return tuple(randint(1,6) for n in range(0, dice))

    def calculate_score(t):
        return True