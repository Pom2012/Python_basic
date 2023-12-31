"""

    in java: static typing

        DataType var = Data

    in Python

        var = value

            * int(): constructs an integer number from a literal (int, float, or string literals)
            * float(): constructs a float number from a literal (int, or float, or string literals)
            * str(): constructs a string from a literal (int, float, or string literals)
"""

name = None
print(name)

name = 'James'
print(name)
print(type(name))   #<class 'str'>
name = 25
print(type(name))   #<class 'int'>
name = 2.5
print(type(name)) #<class 'float'>

is_employed = True

print(is_employed)

s = 25
print(s*5) #125

s = '25'
print(s*5)  #2525252525

str(s)
print(s)