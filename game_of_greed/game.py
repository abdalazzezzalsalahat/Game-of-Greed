# from random import randint, sample
from collections import Counter
# import sys

# from game_logic import GameLogic
# from banker import Banker

from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker



class Game:
    
    def __init__(self, roller = None, calculate = 0):
        self.roller = roller or GameLogic.roll
        self.calculate = calculate or GameLogic.calculate_score

    game = GameLogic()
    banker = Banker()
    round = 1
    remaining_dice = 6
    score = 0
    to_shelf = 0
    stop = False

    def play(self, roller = None):
        global rolling
        rolling =roller or GameLogic.roll
        print('''Welcome to Game of Greed''')
        print('(y)es to play or (n)o to decline')
        res = input('''> ''')

        if res.lower() == 'y' or res.lower() == 'yes':
            self.start()
            exit()
        
        else:
            print('OK. Maybe another time')

    def start(self, ):
        while Game.score < 10000 and Game.stop == False:
                if self.remaining_dice > 0:
                    print(f'Starting round {self.round}')
                Game.remaining_dice = 6
                self.rolling_again()

    def end(self):
        print(f'Thanks for playing. You earned {self.score} points')
        Game.stop = True

    def validate_keepers(self, roll, userinput):
        roll2 = list(roll)
        ui = list(userinput)
        count = 0
        for i in range(len(ui)):
            for j in range(len(roll2)):
                if int(ui[i]) == roll2[j]:
                    roll2[j] = 0
                    count +=1
                    break
        if count == len(ui):
            return True
        return False

    def valid_cases(self, list):
        Game.remaining_dice = Game.remaining_dice - len(list)
        if Game.remaining_dice > 0:
            print(f'You have {Game.to_shelf} unbanked points and {Game.remaining_dice} dice remaining')
            print('(r)oll again, (b)ank your points or (q)uit:')
            next_step = input('> ')

            if len(list) == 6:
                Game.remaining_dice = 6
            if next_step == 'b':
                self.banked()
            elif next_step == 'q':
                self.end()
            elif next_step == 'r':
                Game.to_shelf += Game.banker.shelved
                self.rolling_again()
        else:
            self.rolling_again()

    def banked(self):
        Game.banker.shelf(Game.to_shelf)
        banked = Game.banker.bank()
        Game.to_shelf = 0
        Game.score += banked
        print(f'You banked {banked} points in round {Game.round}')
        Game.round +=1
        print(f'Total score is {Game.score} points')
    
    def zilch (lst):
        validate = Game.game.calculate_score(tuple([int(x) for x in lst]))
        if validate == 0:
            print('****************************************')
            print('**        Zilch!!! Round over         **')
            print('****************************************')
            return True
        return False

    def rolling_again(self):
        if self.remaining_dice > 0:
            print(f'Rolling {Game.remaining_dice} dice...')
            roll = rolling(Game.remaining_dice)
            print(f'*** ' + ' '.join([str(i) for i in roll ])+' ***')
            lst = list(roll)
            validate = Game.game.calculate_score(tuple([int(x) for x in lst]))
            if validate == 0:
                Game.zilch(lst)
                print(f'You banked {validate} points in round {Game.round}')
                print(f'Total score is {Game.score} points')
                Game.round += 1
                Game.to_shelf = 0
                Game.remaining_dice = 6
                self.rolling_again
            else:
                print('Enter dice to keep, or (q)uit:')
                dice_to_keep = input("> ")
                if dice_to_keep == 'q':
                    self.end()
                else:
                    valid = self.validate_keepers(roll, dice_to_keep)
                    while valid == False:
                        print('Cheater!!! Or possibly made a typo...')
                        print(f'*** ' + ' '.join([str(i) for i in roll ])+' ***')
                        print('Enter dice to keep, or (q)uit:')
                        dice_to_keep = input("> ")
                        if dice_to_keep == 'q':
                            self.end()
                        else:
                            valid = self.validate_keepers(roll, dice_to_keep)
                        break
                    lst = list(dice_to_keep)
                    total = Game.game.calculate_score(tuple([int(x) for x in lst]))
                    Game.to_shelf += total
                    self.valid_cases(lst)

if __name__ == '__main__':
    game = Game()
    game.play()
