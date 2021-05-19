from random import randint, sample
from collections import Counter
from game_of_greed.banker import Banker
from game_of_greed.game_logic import GameLogic
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

    def play(self):
        print('''Welcome to Game of Greed''')
        print('(y)es to play or (n)o to decline')
        res = input('''> ''')

        if res.lower() == 'n':
            print('OK. Maybe another time')
            exit()
        
        elif res.lower() == 'y':
            self.start()

    def start(self):
        while Game.score < 10000 and Game.stop == False:
                print(f'Starting round {self.round}')
                Game.remaining_dice = 6
                self.rolling_again()

    def end(self):
        print(f'Total score is {self.score} points')
        print(f'Thanks for playing. You earned {self.score} points')
        Game.stop = True

        # rolled = self.roller(dice)
        # while total <10000 and flag == False:

    def validate_in(self, input, roll):
        lst = list(input)
        saved = tuple([int(n) for n in lst])
        for num in saved:
            print(num)
            if num not in roll:
                return False
            return True

    def valid_cases(self, list):
        Game.remaining_dice = Game.remaining_dice - len(list)
        print(f'You have {self.to_shelf} unbanked points and {self.remaining_dice} dice remaining')
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

    def banked():
        Game.banker.shelf(Game.to_shelf)
        banked = Game.banker.bank()
        Game.to_shelf = 0
        Game.score += banked
        print(f'You banked {banked} points in round {Game.round}')
        Game.round +=1
        print(f'Total score is {Game.score} points')

    def rolling_again():
        pass
            












        # print(f'Rolling {dice} dice...')
        # rolled_points = self.calculate(rolled)
        # if rolled_points == 0:
        #     print("****************************************\n**        Zilch!!! Round over         **\n****************************************")
        #     rounds += 1
        #     continue

        # print(f'*** ' + ' '.join([str(i) for i in rolled ])+' ***')
        # print('Enter dice to keep (no spaces), or (q)uit:')
        # res = input('> ')
        # if  res.lower() == 'q':
        #     exit_fun(total)

        #         # simulation case 3
        # else:
        #     if int(res): # removed in rolls
        #         li = list()
        #         for i in res:
        #             li.append(int(i))
        #         points = self.calculate(tuple(li))
        #         roll_again += points
        #         dice = dice - len(li)
        #         if dice == 0:
        #             flag = True
        #             rounds+=1
        #             dice = 6
        #             continue
        #         if not GameLogic.validate_keepers(rolled, tuple(li)):
        #             print('Cheater!!! Or possibly made a typo...')
        #             continue

        #         if res == 'q':
        #             exit_fun(total)
        #         elif res == 'b':
        
        #         total += roll_again
        #         dice = 6
        #         roll_again=0
        #         flag =True
        #     elif res == 'r' and dice > 0 :
                
        #         flag = False                                

        #     if flag:
                
        #         rounds+=1
        # else:
        #     print('error')
        #     break
        # exit_fun(total)
     
# points = 0
            
        # dice = 6
        # roll_again=0
        # flag = True
 
        # def exit_fun(total):
        #     print(f'''Total score is {total} points\nThanks for playing. You earned {total} points''')
        #     exit()

# def subset_check(test_list, sub_list):
#     set1 = set(test_list)
#     set2 = set(sub_list)
#     is_subset = set2.issubset(set1)
#     print(is_subset)
#     # if(all(x in test_list for x in sub_list)):
#     #     print('yes')

# subset_check([1, 2, 3, 4], [4, 6])

    # @staticmethod
    # def zilch(points):
    #     if points == 0:
    #         print("****************************************\n**        Zilch!!! Round over         **\n****************************************")
    #         return True
     

# game = Game()

# game.play()
