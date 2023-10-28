"""
Used to create a new list based the values of an exiting iterable (list/set/tuple)
"""
divisable_by_5 = []

nums1 = []
for x in range(1, 51):
    nums1.append(x)

print(nums1)
print('---------------------------------')
# for x in nums1:
#     if x % 5 == 0:
#        divisable_by_5.append(x)
#
# print(divisable_by_5)

"""         List comprehensions         """

divisable_by_5 = [x for x in nums1 if x % 5 == 0]
print(divisable_by_5)

""" tuple does not support list comprehension       but """

divisable_by_5 = tuple([x for x in nums1 if x % 5 == 0])

even_numbers = [x for x in nums1 if x % 2 == 0]
odd_numbers = [x for x in nums1 if x % 2 != 0]

print(even_numbers)
print(odd_numbers)

print('------------------ remove all java --------------------------------')

names = ['Python', "Java", "Java", "JavaScript", "java", "JaVA", "Ruby"]

names = [x for x in names if x.lower() != 'java']
print(names)
