"""
    A string is an object that represents sequences of characters
    • A string object is immutable, Once it is created it can’t be altered
    • String objects are surrounded by either single quotes or double quotes
    Strings are ordered sequences of characters, and each character has two
    Python has a built-in string class named str
    A string object is immutable, methods of string can not change the original
    string, therefore they return new values
"""

name ='Python'

print(len(name)) # check the length of string -> 6

print(name[0])
print(name[1])
print(name[-1])
print(name[-2])
# print(name[-20])  IndexError: string index out of range
# print(name[22])   IndexError: string index out of range

word = 'Wooden Spoon'

s1= word[0:6]
print(s1)   #Wooden

s1= word[6:]
print(s1)   # Spoon

s1= word[:4]
print(s1)   #Wood

s1= word[::4]
print(s1)   #Wep

s1= word[::-1]
print(s1)   #noopS nedooW

s5=reversed(word)
print(type(s5)) #   <class 'reversed'>
s5='Python programming'
s6 = s5[7:]
print(s6)   #   programming
print(s6[::-1])

s7="CYDEO SCHOOL"
s=s7.lower()
print(s)
s=s.capitalize();
print(s)

s= 'JAVA ABA'
print(s.index('A'))
print(s.rindex('A'))
s= 'JAVA JAVA'
print(s)
print(s.replace('JAVA', 'PYTHON'))

s= 'C# C# JAVA'
s = s.replace(' C#', ' PYTHON')
print(s)

s= 'java JAVA java JAVA Python Python'
count_java= s.count('JAVA')
print(count_java)

s ='Java'
s2="java"
print(s.lower()==s2.lower()) # true

print(s[0].islower()) #False


"""
capitalize()	Converts the first character to upper case
casefold()	    Converts string into lower case
center()	    Returns a centered string
count()	        Returns the number of times a specified value occurs in a string
encode()	    Returns an encoded version of the string
endswith()	    Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	        Searches the string for a specified value and returns the position of where it was found
format()	    Formats specified values in a string
format_map()	Formats specified values in a string
index()	        Searches the string for a specified value and returns the position of where it was found
isalnum()	    Returns True if all characters in the string are alphanumeric
isalpha()	    Returns True if all characters in the string are in the alphabet
isascii()	    Returns True if all characters in the string are ascii characters
isdecimal()	    Returns True if all characters in the string are decimals
isdigit()	    Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	    Returns True if all characters in the string are lower case
isnumeric()	    Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	    Returns True if all characters in the string are whitespaces
istitle()	    Returns True if the string follows the rules of a title
isupper()	    Returns True if all characters in the string are upper case
join()	        Converts the elements of an iterable into a string
ljust()	        Returns a left justified version of the string
lower()	        Converts a string into lower case
lstrip()	    Returns a left trim version of the string
maketrans()	    Returns a translation table to be used in translations
partition()	    Returns a tuple where the string is parted into three parts
replace()	    Returns a string where a specified value is replaced with a specified value
rfind()	        Searches the string for a specified value and returns the last position of where it was found
rindex()	    Searches the string for a specified value and returns the last position of where it was found
rjust()	        Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	    Splits the string at the specified separator, and returns a list
rstrip()	    Returns a right trim version of the string
split()	        Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	        Returns a trimmed version of the string
swapcase()	    Swaps cases, lower case becomes upper case and vice versa
title()	        Converts the first character of each word to upper case
translate()	    Returns a translated string
upper()	        Converts a string into upper case
zfill()	        Fills the string with a specified number of 0 values at the beginning
"""


