# TODO(everyone): 더하기, 빼기, 곱하기, 나누기 함수 정의하기


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    if num2 == 0:
        return 'ZeroDivisionError'
    else:
        return num1 / num2
