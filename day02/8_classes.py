import numbers

"""
        Objects can share the methods created within the class
        Methods can be called through the object once it’s instantiated
        The first parameter self keyword references the instance of the class
        Used for accessing the attributes of the class
"""


class Employee:
    is_human = True  # similar t0 static variable in Java
    planet = 'Earth'

    def __init__(self, name: str = 'Unknown', job_title='Janitor', salary: numbers = 0):
        self.name = name
        self.job_title = job_title
        self.salary = salary

    def work(self):
        print(f'{self.name} is working')

    def __str__(self):
        return f'name: {self.name}, job_title: {self.job_title}'



print('==========================')
employee2 = Employee('Daniel')

print(employee2.name)
print(employee2.job_title)
print(employee2.salary)

print('==========================')
employee3 = Employee('Brianna', 'SDET', 100000)

print(employee3.name)
print(employee3.job_title)
print(employee3.salary)
print('==========================')
print(Employee.planet)
print(Employee.is_human)

print('==========================')
# print(employee1.work())
employee2.work()
employee3.work()


print(employee2)
print(employee3)


