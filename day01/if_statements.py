if False :
    print('Python programming') # this is not printing

print('Java programming')


score = 50

if score >= 60 :
    print('Congrats! you passed the exam')
else:
    print('Failed')


age = 20
result = None

if age >= 21 :
    result = 'Eligible'
else:
    result = 'Not eligible'

print(result)

"""         ternary             """

age = 26
result = 'Eligible' if age >= 21 else 'Not eligible'

print(result)

"""     multibranch if condition        """

num =-10

result =None

if num > 0 :
    result = 'Positive'
elif num < 0 :
    result = 'Negative'
else :
    result = 'Zero'

print(result)   # Negative

score = 80

if 0 <= score <= 100:   #   pre-condition

    if score >= 60:
        print('Passed')
    else:
        print("Failed")
else:
    print('Invalid score')

score = 90

if 0 <= score <= 100:   #   pre-condition
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
