import numbers


def concat(a: str, b, c, d, e):
    print(f'{a},{b},{c},{d},{e}')


# concat('Cydeo','School') TypeError: concat() missing 3 required positional arguments: 'c', 'd', and 'e'

# we have no method overloading in python
def concat(a: str, b, c='', d='', e=''):
    print(f'{a} {b} {c} {d} {e}'.strip())
    concat('Cydeo', 'School')
    concat('Cydeo', 1)
    concat('Cydeo', 'School',2,3*2,True)

"""
1.  declaring
2.  parameters
3.  restricting parameter' data type
4.  setting default value
5.  restricting return type

"""
def calculate(num1: numbers, num2: numbers, operator: str) -> numbers:
    if operator == '-':
        return print(num1 - num2)
    elif operator == '+':
        return print(num1 + num2)
    elif operator == '*':
        return print(num1 * num2)
    else:
        return print(int(num1 / num2))