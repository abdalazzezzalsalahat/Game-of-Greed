# from game_of_greed.game import Game
from random import randint
from collections import Counter

class GameLogic:

    @staticmethod
    def roll (dice):
        return tuple(randint(1,6) for n in range(0, dice))

    @staticmethod
    def calculate_score(dice_set):
        score = 0
        count = Counter(dice_set)

        # Straight 1- 6 (1500)
        if len(count) == 6:
            score += 1500
            return score
      
        # Three Pairs 1500
        elif len(count)==3 and count.most_common(3)[2][1] == 2:
            score += 1500
            return score

        # Check on each key and update it accordingly 
        for key in count:
            sum = 0
            if key == 1 and count[key] <= 2:
                sum += count[key]*100
            elif key == 5 and count[key] <= 2:
                sum += count[key]*50

            elif key == 1 and count[key] > 2:
                sum += (count[key] - 2)*1000
            
            elif key == 5 and count[key] > 2:
                sum += (count[key] - 2)*500
            
            elif key != 5 or key != 1:
                
                if count[key] == 3:
                    sum += key*100
                
                elif count[key] == 4:
                    sum += key*200

                elif count[key] == 5:
                    sum += key*300

                elif count[key] == 6:
                    sum += key*400 
            score+=sum

        # Unless rolled at one time then its automatic 10,000
        if len(count)==2 and count.most_common(2)[1][1] == 3:  
               score = score * 2
        return score

    # @staticmethod
    # def validate_keepers(dice_list, dice_input):
    #     return not Counter(dice_input) - Counter(dice_list)
        # a = Counter(dice_input).most_common()
        # b = Counter(dice_list).most_common()
        # if len(a) > len(b):
        #   return True
        # votes =0
        # fair_game = False
        # for i in a:
        #      for j in b:
        #          if i[0] == j[0]:
        #              if i[1] <= j[1]:
        #                   votes +=1
        # if len(a) == votes:
        #     fair_game = True
        # return fair_game

    @staticmethod
    def get_scorers(tup):
        score = list()
        if 1 in tup:
            score.append(1)
        if 5 in tup:
            score.append(5)
        return tuple(score)

    # @staticmethod 
    # def get_scorers(dice):
    #     all = GameLogic.calculate_score(dice)
    #     if all == 0: 
    #         return tuple()
    #     sco = []
    #     for i in range(len(dice)):
    #         roll = dice[:i] + dice[i + 1:]
    #         sub = GameLogic.calculate_score(roll)
    #         if sub != all:
    #             sco.append(dice[1])
    #     return tuple(sco)

