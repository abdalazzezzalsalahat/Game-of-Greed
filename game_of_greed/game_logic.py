from random import randint, sample
from collections import Counter


class GameLogic:

    def __init__(self,roller = None, calculate=0):
        self.roller = roller or self.roll
        self.calculate = calculate or self.calculate_score

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
                   







# You banked 50 points in round 1
# Total score is 50 points
# Starting round 2
# Rolling 6 dice...meLogic()

# game.play()
# 6,5,1,6,6,6
# Enter dice to keep (no spaces), or (q)uit: q
# Total score is 50 points
# Thanks for playing. You earned 50 points

                # else:
                #     print('Enter number between 1 and 6')

                






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

        # 3x1's	1,000
        # 4x1's	2,000
        # 5x1's	3,000
        # 6x1's	4,000
        
        # 3x5's	500
        # 4x5's	1,000
        # 5x5's	1,500
        # 6x5's	2,000


        # 3x6's	600
        # 4x6's	1,200
        # 5x6's	1,800
        # 6x6's	2,400
    
        # 3x4's	400You can view your grades based on What-If scores so that you
        # 4x4's	800
        # 5x4's	1,200
        # 6x4's	1,600

        # 3x3's	300
        # 4x3's	600
        # 5x3's	900
        # 6x3's	1,200

        # 3x2's	200
        # 4x2's	400
        # 5x2's	600
        # 6x2's	800

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


# game = GameLogic()

# game.play()
