class Yatzy:

    def __init__(self, *dice):
        self.dice = list(dice)
        
        
    @staticmethod
    def chance(*dice):
        return sum(dice)    


    @staticmethod
    def yatzy(*dice):
        if dice[:-1] == dice[1:]:
            return 50
        return 0
    

    @staticmethod
    def ones(*dice):
        ONE = 1
        return dice.count(ONE) * ONE

    
    @staticmethod
    def twos(*dice):
        TWO = 2
        return dice.count(TWO) * TWO

    
    @staticmethod
    def threes(*dice):
            THREE = 3
            return dice.count(THREE) * THREE
        
    
    def fours(self):
        FOUR = 4
        return self.dice.count(FOUR) * FOUR
    

    def fives(self):
      FIVE = 5
      return self.dice.count(FIVE) * FIVE
    

    def sixes(self):
        SIX = 6
        return self.dice.count(SIX) * SIX
    
    @staticmethod
    def score_pair(*dice):
        mydice = list(dice)
        matching_dice_found = False
        PAIR = 2
        while not matching_dice_found and len(mydice) >= PAIR:
            biggest = max(mydice)
            if mydice.count(biggest) >= PAIR:
                matching_dice_found = True
                return biggest * PAIR
            else:
                mydice = list(filter((biggest).__ne__, mydice))
        return 0

    @staticmethod
    def two_pair(*dice):
        mydice = list(dice)
        double_matching_dice_found = False
        PAIR = 2
        matchings = 0
        score = 0
        while not double_matching_dice_found and len(mydice) >= PAIR:
            biggest = max(mydice)
            if mydice.count(biggest) >= PAIR:
                matchings += 1
                score += biggest * PAIR
                if matchings == PAIR:
                    double_matching_dice_found = True
                    return score
            mydice = list(filter((biggest).__ne__, mydice))
        return 0
            
    @staticmethod
    def four_of_a_kind(*dice):
        FOUR = 4
        for die in range(max(dice), 1, -1):
            if dice.count(die) >= FOUR:
                return die * FOUR
        return 0
    

    @staticmethod
    def three_of_a_kind(*dice):
        THREE = 3
        for die in range(max(dice), 1, -1):
            if dice.count(die) >= THREE:
                return die * THREE
        return 0
    

    @staticmethod
    def smallStraight(*dice):
        max = 5
        min = 1
        small_straight = list(range(min, max + 1))
        if list(dice) == small_straight: return sum(small_straight)
        else: return 0
    

    @staticmethod
    def largeStraight(*dice):
        max = 6 
        min = 2
        large_straight = list(range(min, max + 1))
        if list(dice) == large_straight: return sum(large_straight)
        else: return 0
    
    @staticmethod
    def __two_of_a_kind(*dice):
        TWO = 2
        for die in range(max(dice), 0, -1):
            if dice.count(die) == TWO:
                return die * TWO
        return 0

    @classmethod
    def fullHouse(cls, *dice):
        if cls.__two_of_a_kind(*dice) and cls.three_of_a_kind(*dice):
            return cls.__two_of_a_kind(*dice) + cls.three_of_a_kind(*dice)  
        return 0