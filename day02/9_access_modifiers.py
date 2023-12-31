"""
    Python uses ‘_’ symbol to determine the access control for a specific data member or a member function
    of a class. Access specifiers in Python have an important role to play in securing data from
    unauthorized access and in preventing it from being exploited.
    A Class in Python has three types of access modifiers:
        Public Access Modifier
        Protected Access Modifier
        Private Access Modifier
"""


class Geek:

    # constructor
    def __init__(self, name, age):
        # public data members
        self.geekName = name
        self.geekAge = age

    # public member function
    def displayAge(self):
        # accessing public data member
        print("Age: ", self.geekAge)


# creating object of the class
obj = Geek("Nate", 30)

# accessing public data member
print("Name: ", obj.geekName)

# calling public member function of the class
obj.displayAge()


# program to illustrate protected access modifier in a class

# super class
class Student:
    # protected data members
    _name = None
    _roll = None
    _branch = None

    # constructor
    def __init__(self, name, roll, branch):
        self._name = name
        self._roll = roll
        self._branch = branch

    # protected member function
    def _displayRollAndBranch(self):
        # accessing protected data members
        print("Roll: ", self._roll)
        print("Branch: ", self._branch)


# derived class
class Geek(Student):

    # constructor
    def __init__(self, name, roll, branch):
        Student.__init__(self, name, roll, branch)

        # public member function

    def displayDetails(self):
        # accessing protected data members of super class
        print("Name: ", self._name)

        # accessing protected member functions of super class
        self._displayRollAndBranch()


# creating objects of the derived class
obj = Geek("R2J", 1706256, "Information Technology")

# calling public member functions of the class
obj.displayDetails()


# program to illustrate access modifiers of a class

# super class
class Super:
    # public data member
    var1 = None

    # protected data member
    _var2 = None

    # private data member
    __var3 = None

    # constructor
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3

    # public member function
    def displayPublicMembers(self):
        # accessing public data members
        print("Public Data Member: ", self.var1)

    # protected member function
    def _displayProtectedMembers(self):
        # accessing protected data members
        print("Protected Data Member: ", self._var2)

    # private member function
    def __displayPrivateMembers(self):
        # accessing private data members
        print("Private Data Member: ", self.__var3)

    # public member function
    def accessPrivateMembers(self):
        # accessing private member function
        self.__displayPrivateMembers()


# derived class
class Sub(Super):

    # constructor
    def __init__(self, var1, var2, var3):
        Super.__init__(self, var1, var2, var3)

    # public member function
    def accessProtectedMembers(self):
        # accessing protected member functions of super class
        self._displayProtectedMembers()


# creating objects of the derived class
obj = Sub("Geeks", 4, "Geeks !")

# calling public member functions of the class
obj.displayPublicMembers()
obj.accessProtectedMembers()
obj.accessPrivateMembers()

# Object can access protected member
print("Object is accessing protected member:", obj._var2)

# object can not access private member, so it will generate Attribute error
# print(obj.__var3)