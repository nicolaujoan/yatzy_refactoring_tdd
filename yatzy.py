class Yatzy:

    def __init__(self, *dice):
        self.dice = list(dice)
        
        
    @staticmethod
    def chance(*dice):
        return sum(dice)    


    @staticmethod
    def yatzy(*dice):
        YATZY_SCORE = 50
        equal_dice = dice[:-1] == dice[1:]
        return YATZY_SCORE if equal_dice else 0
    

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


    @classmethod
    def __find_matching_dice(cls, dice, desired_matchings):
        matchings_found = False
        PAIR = 2
        matchings = 0
        score = 0
        
        while not matchings_found and len(dice) >= PAIR:
            biggest_die = max(dice)
            if dice.count(biggest_die) >= PAIR:
                matchings += 1
                score += biggest_die * PAIR
                if matchings == desired_matchings:
                    matchings_found = True
                    return score
            dice = list(filter(biggest_die.__ne__, dice))   # eliminate dice that cannot match
        return 0
    

    @classmethod
    def score_pair(cls, *dice):
        desired_matchings = 1
        score = cls.__find_matching_dice(list(dice), desired_matchings)
        return score
    

    @classmethod
    def two_pair(cls, *dice):
        desired_matchings = 2
        score = cls.__find_matching_dice(list(dice), desired_matchings)
        return score
        

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
        return sum(small_straight) if list(dice) == small_straight else 0


    @staticmethod
    def largeStraight(*dice):
        max = 6 
        min = 2
        large_straight = list(range(min, max + 1))
        return sum(large_straight) if list(dice) == large_straight else 0
    

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
