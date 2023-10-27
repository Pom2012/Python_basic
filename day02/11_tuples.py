"""
        A special type of variable
        • Used to store multiple values of any types
        • Size is fixed, and can not be increased/decreased
        • The values in the tuple are unchangeable
        • Every element in a tuple has 2 index numbers:
            • Forward index
            • Reverse index
        • Tuple has the following two build-in methods:
        § index(): returns the forward index number of a specified element from the tuple
        § count(): returns the frequency of a specified element from the tuple
"""

days = ('MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN')
fruits = "Apple", 'Banana'
print(days)
print(fruits)
print(type(days))
print(type(fruits))

print('--------------------------')

work_days = days[0:5]
print(work_days)

print('--------------------------')

work_days = days[:-2]
print(work_days)

print('--------------------------')

weekend = days[-2:]
print(weekend)

print('--------------------------')

tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)

print(tuple1 == tuple2)
print(tuple1 is tuple2)

print('--------------------------')

tuple1 = (1, 2, 3)
tuple2 = (5, 6, 7)

tuple3 = tuple1 + tuple2

print(tuple3)

print('--------------------------')

reversed_tuple = days[::-1]
print(reversed_tuple)

print('--------------------------')
reversed_tuple2 = tuple(reversed(days))
print(reversed_tuple2)
print('--------------------------')
numbers = (10, 10, 10, 10, 10, 10, 20, 30, 40)
print(numbers.count(10))
print('--------------------------')

for x in range(0, len(days)):
    print(x)
print('--------------------------')

for x in reversed(range(0, len(days))):
    print(x)