from random import randint, sample
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
    
        # 3x4's	400
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
                
        return score
    












                    
                



