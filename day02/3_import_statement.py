from day02 import utility
from utility import getScore, square, calculate, add

import day01.utility2 as u2

"""
    Allows us to reuse the functions/features of one python file (.py) in another
    We need to import the python file in order to use its properties in other python files
    We can create an alias name by using the 'as' keyword when we import a python file
"""

print(utility.add(3))

utility.calculate(2, 5, '+')
u2.calculate2(2, 3, '+')

getScore(70)

print(square(2))
