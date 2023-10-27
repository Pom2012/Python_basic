num =int(input('Enter a positive number:\n'))

while num <= 0:
    num=int(input('Enter a positive number:\n'))

print(f'You have entered {num}')


answer = str(input('Enter yes or no:\n'))

while not (answer.lower()=='yes' or answer.lower()=='no'):
    answer=str(input('Enter yes or no:\n'))

print('You entered '+answer)