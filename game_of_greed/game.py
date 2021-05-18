from random import randint, sample
from collections import Counter

class Game:
    
    def __init__(self,roller = None, calculate=0):
        self.roller = roller or GameLogic.roll
        self.calculate = calculate or GameLogic.calculate_score

    def play(self):
        # qutt = ('no','n','quit','q')
        print('''Welcome to Game of Greed''')
        res = input('''Wanna play?''')
        def exit_fun(total):
            print(f'''Total score is {total} points\nThanks for playing. You earned {total} points''')
            exit()

        if res.lower() == 'n':
            print('OK. Maybe another time')
            exit()
        elif res.lower() == 'y':
            rounds = 1
            points = 0
            total = 0
            dice = 6

            while rounds in range(6):
                print(f'Starting round {rounds}')
                print(f'Rolling {dice} dice...')
                rolled = self.roller(dice)
                print(','.join([str(i) for i in rolled ]))
                res = input('Enter dice to keep (no spaces), or (q)uit: ')
                if  res.lower() == 'q':
                    exit_fun(total)

                # simulation case 3
                else:
                    if int(res): # removed in rolls
                        li = list()
                        for i in res:
                            li.append(int(i))
                        points = self.calculate(tuple(li))
                        dice = dice - len(li)
                        print(f'You have {points} unbanked points and {dice} dice remaining')
                        res = input('(r)oll again, (b)ank your points or (q)uit ')
                        if res == 'q':
                            exit_fun(total)
                        elif res == 'b':
                            print(f'You banked {points} points in round {rounds}')
                            total += points
                            dice = 6
                        print(f'Total score is {total} points')
                        rounds+=1
                    else:
                        print('error')
                        break
     



class GameLogic:

    def __init__(self):
        pass
                   
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

        # unless rolled at one time then its automatic 10,000
        if len(count)==2 and count.most_common(2)[1][1] == 3:  
               score = score * 2
        return score


# game = Game()

# game.play()
