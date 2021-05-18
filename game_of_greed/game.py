from random import randint, sample
from collections import Counter

class Game:
    
    def __init__(self,roller = None, calculate=0):
        self.roller = roller or GameLogic.roll
        self.calculate = calculate or GameLogic.calculate_score
    

    def play(self):
        print('''Welcome to Game of Greed''')
        print('(y)es to play or (n)o to decline')
        res = input('''> ''')
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
            roll_again=0
            flag = True

            while total <10000:
                if flag:
                    print(f'Starting round {rounds}')


                print(f'Rolling {dice} dice...')
                rolled = self.roller(dice)
                print(f'*** ' + ' '.join([str(i) for i in rolled ])+' ***')
                print('Enter dice to keep (no spaces), or (q)uit:')
                res = input('> ')
                if  res.lower() == 'q':
                    exit_fun(total)

                # simulation case 3
                else:
                    if int(res): # removed in rolls
                        li = list()
                        for i in res:
                            li.append(int(i))
                        points = self.calculate(tuple(li))
                        roll_again += points
                        dice = dice - len(li)
                        if dice == 0:
                            flag = True
                            rounds+=1
                            dice = 6
                            continue
                        if not GameLogic.validate_keepers(rolled, tuple(li)):
                            print('Cheater!!! Or possibly made a typo...')
                            continue

                        print(f'You have {roll_again} unbanked points and {dice} dice remaining')
                        print('(r)oll again, (b)ank your points or (q)uit:')
                        res = input('> ')
                        if res == 'q':
                            exit_fun(total)
                        elif res == 'b':
                            print(f'You banked {roll_again} points in round {rounds}')
                            total += roll_again
                            dice = 6
                            roll_again=0
                            flag =True
                        elif res == 'r' and dice > 0 :
                            
                            flag = False                                

                        if flag:
                            print(f'Total score is {total} points')
                            rounds+=1
                    else:
                        print('error')
                        break
            exit_fun(total)
     

def subset_check(test_list, sub_list):
    set1 = set(test_list)
    set2 = set(sub_list)
    is_subset = set2.issubset(set1)
    print(is_subset)
    # if(all(x in test_list for x in sub_list)):
    #     print('yes')


subset_check([1, 2, 3, 4], [4, 6])

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


    @staticmethod
    def validate_keepers(set, sub_set):

        sub_set_dictionary = Counter(sub_set)
        set_dictionary = Counter(set)
        for key in sub_set_dictionary:
            if not sub_set_dictionary[key] <= set_dictionary[key]:
                return False
            else:
                return True
    
    @staticmethod
    def get_scorers(tup):
        score = list()
        if 1 in tup:
            score.append(1)
        if 5 in tup:
            score.append(5)
        
        return tuple(score)

    


# game = Game()

# game.play()
