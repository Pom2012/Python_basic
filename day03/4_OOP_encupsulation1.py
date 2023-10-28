"""
        An object hides its internal data from code that’s outside the class
        Hide an attribute by giving private access modifier,
        and making the methods that access those fields public
        These public methods are called getters & setters (accessor and mutator)

        private ( _ ) - When the private access modifier is applied to a class member, the
                    member can not be accessed by code outside the class

        constructor can't be overloaded

"""


class Person:

    def __init__(self, name, age: int):
        self.__name = None  # <- this is private
        self.__age = None
        self.set_name(name)
        self.set_age(age)

    def get_name(self) -> str:
        if self.__name is None or self.__name == '' or type(self.__name) != str:
            raise RuntimeError(f'Invalid name has been set: {self.__name}')

        return self.__name

    def set_name(self, name: str):
        if type(name) != str:
            raise RuntimeError(f'Person name must be a string')
        if name == '':
            raise RuntimeError(f'Person name can not be empty')
        self.__name = name

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age):
        if age < 0 or age > 150:
            raise RuntimeError(f'Invalid {age}')
        self.__age = age

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'


person1 = Person('James', 29)
# print(person1.get_name())  # raise RuntimeError(f'Invalide name: {self.__name}')

# print(person1.__set_name__(123)) #RuntimeError: Person name must be a string
# print(person1.__name)  AttributeError: 'Person' object has no attribute '__name'
# person1.set_name('James')
# person1.set_age(29)
print(person1.get_name())
print(person1.get_age())

person2 = Person('Mike', 45)
print(person2.get_name())
print(person2.get_age())


print(person1)
print(person2)
