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


def sqrt(num1):
    return pow(num1, 0.5)
