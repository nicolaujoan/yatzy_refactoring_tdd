from pips import Pips

class Yatzy:

    PAIR = 2

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
        return dice.count(Pips.ONE.value) * Pips.ONE.value

    
    @staticmethod
    def twos(*dice):
        return dice.count(Pips.TWO.value) * Pips.TWO.value

    
    @staticmethod
    def threes(*dice):
            return dice.count(Pips.TWO.value) * Pips.TWO.value
        
    
    def fours(self):
        return self.dice.count(Pips.FOUR.value) * Pips.FOUR.value
    

    def fives(self):
      return self.dice.count(Pips.FIVE.value) * Pips.FIVE.value


    def sixes(self):
        return self.dice.count(Pips.SIX.value) * Pips.SIX.value


    @classmethod
    def __find_matching_dice(cls, dice, desired_matchings):
        matchings_found = False
        matchings = 0
        score = 0
        
        while not matchings_found and len(dice) >= cls.PAIR:
            biggest_die = max(dice)
            if dice.count(biggest_die) >= cls.PAIR:
                matchings += 1
                score += biggest_die * cls.PAIR
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
        for die in range(max(dice), 1, -1):
            if dice.count(die) >= Pips.FOUR.value:
                return die * Pips.FOUR.value
        return 0


    @staticmethod
    def three_of_a_kind(*dice):
        for die in range(max(dice), 1, -1):
            if dice.count(die) >= Pips.THREE.value:
                return die * Pips.THREE.value
        return 0

    @staticmethod
    def smallStraight(*dice):
        small_straight = list(range(Pips.ONE.value, Pips.FIVE.value + 1))
        return sum(small_straight) if list(dice) == small_straight else 0


    @staticmethod
    def largeStraight(*dice):
        large_straight = list(range(Pips.TWO.value, Pips.SIX.value + 1))
        return sum(large_straight) if list(dice) == large_straight else 0
    

    def __two_of_a_kind(*dice):
        for die in range(max(dice), 0, -1):
            if dice.count(die) == Pips.TWO.value:
                return die * Pips.TWO.value
        return 0


    @classmethod
    def fullHouse(cls, *dice):
        if cls.__two_of_a_kind(*dice) and cls.three_of_a_kind(*dice):
            return cls.__two_of_a_kind(*dice) + cls.three_of_a_kind(*dice)  
        return 0
