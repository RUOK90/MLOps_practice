# TODO(everyone): 더하기, 빼기, 곱하기, 나누기 함수 테스트 케이스 작성

import functions


def test_addition():
    assert functions.addition(1, 1) == 2


def test_subtraction():
    assert functions.subtraction(1, 1) == 0


def test_multiplication():
    assert functions.multiplication(1, 1) == 1


def test_division():
    assert functions.division(1, 1) == 1


def test_sqrt():
    assert functions.sqrt(4) == 2
