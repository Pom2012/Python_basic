#       Logical operators

'''
    'and'
    'or'
    'no'
'''
#   'and' 'or' 'no'
s = 'Hello World'

print('H' and 'W' in s) #   True
print(True and True)    #   True
print(False and True)   #   False
print(True and False)   #   False
print(False and False)  #   False
print(False or False)  #   False


s='Java Python C# C=='

print('Java' or 'Ruby' in s)

age =29
citizenship ='USA'
is_eligable = age >= 18 and citizenship =='USA'
print(is_eligable) # True

name2='James'
age2 =30
citizenship2 ='USA'
is_eligable = age2 >= 18 and citizenship =='USA'
print(f'Is {name2} eligible:',is_eligable) # True
