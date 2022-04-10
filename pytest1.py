import calculator
import pytest
import youtube

#calculator tests:

def testAddPass():
    assert calculator.add(1,2) == 3


def testAddFail():
    assert calculator.add(2,2) == 3


def testSubPass():
    assert calculator.sub(5,2) == 3


def testSubFail():
    assert calculator.sub(4,2) == 3


def testMulPass():
    assert calculator.mul(3,3) == 9


def testMulFail():
    assert calculator.mul(3,3) == 10


def testDivPass():
    with pytest.raises(ZeroDivisionError):
        calculator.div(10,0)


def testDivFail():
    with pytest.raises(ZeroDivisionError):
        calculator.div(10,10)


def testDivEvenPass():
    assert calculator.divEven(10,4) == 2


def testDivEvenFail():
    assert calculator.divEven(7,2) == 3.5


def testModuloPass():
    assert calculator.modulo(10,5) == 0


def testModuloFail():
    assert calculator.modulo(10,5) == 2


def testSqrtPass1():
    assert calculator.sqrt(144) == 12


def testSqrtPass2():
    assert calculator.sqrt(-5) == 'Invalid Number'


#Youtube automtaion tests:
def testYoutubeSelenium():
    assert youtube.driver.title == 'I Want It That Way | Brooklyn Nine-Nine - YouTube'


