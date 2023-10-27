import numbers


def calculate2(num1: numbers, num2: numbers, operator: str) -> numbers:
    if operator == '-':
        return print(num1 - num2)
    elif operator == '+':
        return print(num1 + num2)
    elif operator == '*':
        return print(num1 * num2)
    else:
        return print(int(num1 / num2))


def square(num: int):
    return num * num


def add(num: int):
    return num + num


def getScore(score: int):
    if 0 <= score <= 100:  # pre-condition
        if score >= 90:
            print('A')
        elif score >= 80:
            print('B')
        elif score >= 70:
            print('C')
        else:
            print("D")
    else:
        print('Invalid score')
