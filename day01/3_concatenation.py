
name = 'James'
age = 26

print('My name is '+name)
# print('My age is '+ age) TypeError: can only concatenate str (not "int") to str

print('My age is {}'.format(age)) # My age is 26
print('My name is {} and I am {} years old'.format(name,age)) # My age is 26


print(str('My name is ') + name) #  My name is James

print(f'My name is {name} and I am {age} years old') #My name is James and I am 26 years old

print('Python', 3, 'is awesome:',True)  #Python 3 is awesome: True
