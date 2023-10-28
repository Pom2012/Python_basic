"""
        • A special type of variable
        • Used to store multiple values of any types
        • Size is dynamic, and can be increased/decreased
        • The values in the list are changeable
        • Every element in a list has 2 index numbers:
                • Forward index
                • Reverse index
"""
days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
fruits = ["Apple", 'Banana', 'Lemon', 'Cherry']

print(days[0])
print(days[-1])
print(len(days))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

groceries_list = ['Egg', 'Milk', 'Rice']
print('-----------------------')
print(groceries_list)
print(len(groceries_list))
print('-----------------------')
groceries_list.append('Chicken')
print(groceries_list)
print(len(groceries_list))
print('-----------------------')
groceries_list.extend(('Beef', 'Orange', 'Onion'))
print(groceries_list)
print(len(groceries_list))
print('----------Cherry-------------')
groceries_list[-2] = 'Cherry'
print(groceries_list)
print(len(groceries_list))  # ['Egg', 'Milk', 'Rice', 'Chicken', 'Beef', 'Cherry', 'Onion']

numbers_list = [10, 20, 30, 40, 50, 60, 70, 80]
print(numbers_list)
numbers_list[2:-2] = [300, 800, 5, 6000]
print(numbers_list)

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
list1 = characters[0:len(characters) - 3]
print(list1)
list2 = characters[2:-3]
print(list2)
list3 = characters[:4]
print(list3)
list4 = characters[4:]
print(list4)

characters[2:5] = ['C', 'D', 'E', 'F']
print(characters)

print('-----------------------------------------------')

names = ['Conor', 'Steve', 'Hazel', 'Breanna']

for x in names:
    print(x)

nums = [10, 20, 30, 40, 50, 60]

for x in range(0, len(nums)):
    nums[x] = int(nums[x] / 5)

print(nums)

"""
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
"""
print('-----------------------------------------------')
nums2 = [60000, 10, 200, 30, 40, -50, 60]
nums2.sort()  # ascending
print(nums2)
nums2.sort(reverse=True)  # descending
print(nums2)

"""   how to convert tuples to lists  -> list() method    """
tuple_elements = ('Java', 'Python', 'C#', 'Ruby')
print(f"tuple_elements: {tuple_elements}")
list_elements = list(tuple_elements)
list_elements[-2] = 'C++'
print(f'list_elements: {list_elements}')
list_elements.append('SWIFT')  # Adds an element at the end of the list
print(f'list_elements: {list_elements}')

for x in list_elements:
    print(x)

new = list_elements.copy()
new2 = list_elements.clear()
print(new)
print(new2)

fruits_list2 = ["Apple", 'Banana', 'Lemon', 'Cherry']

fruits_list2.insert(2, "Mango") #insert method
print(f'the size of fruit list is {len(fruits_list2)}')

print(fruits_list2)
fruits_list2.pop(1) # removes the last element
print(fruits_list2)
fruits_list2.remove('Apple')
print(fruits_list2)