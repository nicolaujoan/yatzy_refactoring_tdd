import pytest
from yatzy import Yatzy

# Chance
# The player scores the sum of all dice, no matter what they read.


def test_chance():
    # iterar sobre *args evita codigo cableado a 5 argumentos
    assert 15 == Yatzy.chance(1, 2, 3, 4, 5)
    assert 14 == Yatzy.chance(1, 1, 3, 3, 6)
    assert 21 == Yatzy.chance(4, 5, 5, 6, 1)

def test_yatzy():
    assert Yatzy.yatzy(1, 1, 1, 1, 1) == 50
    assert Yatzy.yatzy(1, 2, 3, 4, 5) == 0


@pytest.fixture
def inyector():
    # Es el setup de unittest o de JUnit
    tirada = Yatzy(5, 6, 4, 4, 5)
    return tirada


def test_fours(inyector):
    # Es necesario un objeto ya creado
    valorEsperado = 8
    # No puedo testear con fixtures = inyeccion de dependencias
    # los metodos estaticos como chance()
    assert valorEsperado == inyector.fours()

def test_fives(inyector):
    valorEsperado = 10
    assert valorEsperado == inyector.fives()

def test_sixes(inyector):
    valorEsperado = 6
    assert valorEsperado == inyector.sixes()

def test_score_pair():
    assert Yatzy.score_pair(3, 3, 3, 4, 4) == 8
    assert Yatzy.score_pair(1, 1, 6, 2, 6) == 12
    assert Yatzy.score_pair(3, 3, 3, 4, 1) == 6
    assert Yatzy.score_pair(3, 3, 3, 3, 1) == 6
    assert Yatzy.score_pair(1, 2, 3, 4, 5) == 0

def test_two_pair():
    assert Yatzy.two_pair(1, 1, 2, 3, 3) == 8
    assert Yatzy.two_pair(1, 1, 2, 3, 4) == 0
    assert Yatzy.two_pair(1, 1, 2, 2, 2) == 6

def test_four_of_a_kind():
    assert Yatzy.four_of_a_kind(2, 2, 2, 2, 5) == 8
    assert Yatzy.four_of_a_kind(2, 2, 2, 5, 5) == 0
    assert Yatzy.four_of_a_kind(2, 2, 2, 2, 2) == 8

def test_three_of_a_kind():
    assert Yatzy.three_of_a_kind(3, 3, 3, 4, 5) == 9
    assert Yatzy.three_of_a_kind(3, 3, 4, 5, 6) == 0
    assert Yatzy.three_of_a_kind(3, 3, 3, 3, 1) == 9

def test_smallStraight():
    assert Yatzy.smallStraight(1, 2, 3, 4, 5) == 15
    assert Yatzy.smallStraight(1, 2, 2 ,3, 4, 5) == 0
    assert Yatzy.smallStraight(2, 4, 3, 3, 1) == 0

def test_largeStraight():
    assert Yatzy.largeStraight(2, 3, 4, 5, 6) == 20
    assert Yatzy.largeStraight(1, 2, 3, 4, 5) == 0
    assert Yatzy.largeStraight(1, 3, 3, 2, 6) == 0

def test_fullHouse():
    assert Yatzy.fullHouse(1, 1, 2, 2, 2) == 8
    assert Yatzy.fullHouse(2, 3, 3, 3, 2) == 13
    assert Yatzy.fullHouse(2, 2, 3, 3, 4) == 0
    assert Yatzy.fullHouse(4, 4, 4 ,4, 4) == 0


