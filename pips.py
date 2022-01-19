from ast import Return
from enum import IntEnum

class Pips(IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6

    @classmethod
    def get_values(cls):
        return [pip.value for pip in cls.__members__.values()]

    @classmethod
    def reversed_values(cls):
        return list(reversed(cls.get_values()))

    @classmethod
    def filter_pip(cls, pip):
        return list(set(cls.get_values()) - { pip.value })

if __name__ == "__main__":

    print(list(Pips))
    print(Pips.ONE)
    print(Pips.ONE.value)

    for pip in Pips.__members__.values():
        print(pip.value)

    print(Pips.get_values())
    print(Pips.reversed_values())
    print(Pips.filter_pip(Pips.FIVE))

    