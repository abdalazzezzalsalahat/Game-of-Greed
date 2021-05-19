
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
