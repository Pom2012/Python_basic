"""
    Grouping a series of code fragments to perform a task
    • Allows us to reuse the function rather than repeating the same set of statements
    • Improves the reusability and efficiency of our codes
    def  -> keyword -> indicates that the start of the function
    Function name ->  Descriptive name of the function
    Parenthesis ()

    in java
    public static void method(){}

    in python
    def function_name():
        statements


"""
import numbers


def display_message():
    print('Hello Cydeo')
    print('Hello World')


display_message()


def value():
    return 'Python programming'


print(value())


def return_int() -> int:
    return 10;


print(return_int())


def divide(num1, num2):
    return num1 / num2


print(divide(10, 2))


def square(num: int):
    return num * num


def add(num: int):
    return num + num


def add2(num: int, num2: int) -> int:
    return num + num2


print(square(5))
print(add(5))
print(add('Java'))
print(add2(2, 2))
print('**************************')


# print(add2('Java', 2)) TypeError: can only concatenate str (not "int") to str


def calculate(num1: numbers, num2: numbers, operator: str) -> numbers:
    if operator == '-':
        return print(num1 - num2)
    elif operator == '+':
        return print(num1 + num2)
    elif operator == '*':
        return print(num1 * num2)
    else:
        return print(int(num1 / num2))


calculate(10, 2, '-')
calculate(2, 2, '+')
calculate(3, 2, '*')
calculate(12, 4, '/')

class test:
    def method(self):   # this is a method
        pass




