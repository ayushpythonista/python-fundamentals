"""
In Python, decorators are a powerful and flexible way to modify or extend the behavior of functions or methods, without changing their actual code. A decorator is essentially a function that takes another function as an argument and returns a new function with enhanced functionality.

Decorators are often used in scenarios such as logging, authentication and memorization, allowing us to add additional functionality to existing functions or methods in a clean, reusable way.
"""

"""
1. Function Decorators:
The most common type of decorator, which takes a function as input and returns a new function. The example above demonstrates this type.
"""

def my_decorator(func):
    def wrapper():
        print("First")
        func()
        print("Second")
    return wrapper


@my_decorator
def greet():
    print("Hey Bro")


greet()

#NOTE: if we return wrapper with `()` -> return wrapper() then greet will be called without `()`
# and if we dont have def wrapper() inside then also greet will be called without `()`

"""
decorator takes the greet function as an argument.
It returns a new function (wrapper) that first prints a message, calls greet() and then prints another message.
The @decorator syntax is a shorthand for greet = decorator(greet).
"""



"""
2. Method Decorators:

Used to decorate methods within a class. They often handle special cases, such as the self argument for instance methods."""


def method_decorator(func):
    def wrapper(self):
        print("First")
        func(self)
        print("Second")
    return wrapper

class MyClass:
    @method_decorator
    def greet_me(self):
        print("Hey Bro")

myClass = MyClass()
myClass.greet_me()

"""NOTE that in case of method decorator, everything will have self as first parameter"""


"""
3. Class Decorators
Class decorators are used to modify or enhance the behavior of a class. Like function decorators, class decorators are applied to the class definition. They work by taking the class as an argument and returning a modified version of the class.
"""

def funcClass(className):
    className.class_name = className.__name__
    className.hello_world = "Hello World"
    print(className)
    return className


@funcClass
class MyClassDec:
    pass

print(MyClassDec.class_name)
print(MyClassDec.hello_world)




"""
Python provides several built-in decorators that are commonly used in class definitions. These decorators modify the behavior of methods and attributes in a class, making it easier to manage and use them effectively. The most frequently used built-in decorators are @staticmethod, @classmethod, and @property.
"""


"""
@staticmethod
The @staticmethod decorator is used to define a method that doesn’t operate on an instance of the class (i.e., it doesn’t use self). Static methods are called on the class itself, not on an instance of the class.
"""

class MathOperations:
    
    @staticmethod       # expects new line at end of decorator
    def addNums(x, y):
        return x + y
    
    def multiply(x, y):
        return x * y


add_num = MathOperations.addNums(20, 55)
print(add_num)

mul_num = MathOperations.multiply(20, 55)   # this works
print(mul_num)


# but if we dont define static method , then we need to pass self in addNums else it will give error
mathOperations = MathOperations()
added = mathOperations.addNums(70, 99)
print(added)

# mul = mathOperations.multiply(70, 99)   # this will require self inside class
# print(mul)


"""
@classmethod
The @classmethod decorator is used to define a method that operates on the class itself (i.e., it uses cls). Class methods can access and modify class state that applies across all instances of the class.
"""


class Employee():
    raise_amount = 1.05

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def set_raise_amount(self, amount):
        self.raise_amount = amount


Employee.set_raise_amount(200)
print(Employee.raise_amount)


"""NOTE that classmethod has 2 params first is class and second is param (it can be any numbers) but during call only second param is passed but in staticmethod neither first param is required nor in method call"""


"""@property
The @property decorator is used to define a method as a property, which allows you to access it like an attribute. This is useful for encapsulating the implementation of a method while still providing a simple interface."""


class Circle:
    def __init__(self, radius):         # __init__ is required to pass arguments
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius cannot be negative")
    
    @property
    def area(self):
        return 3.14159 * (self._radius ** 2)
    

# Using the property
c = Circle(5)
print(c.radius) 
print(c.area)    
c.radius = 10
print(c.area)

"""means if it is a property we can use setter as well as no need to call as function, call like variable"""

class Student:
    def __init__(self, name):
        self.stud_name = name

    @property
    def name(self):
        return self.stud_name
    
    @name.setter
    def name(self, value):
        self.stud_name = value      # remember to keep self.{name} to be different than func name else it will be recursive
    
    @name.setter
    def add_surname(self, value):
        self.stud_name = f"{self.stud_name} {value}"     # this self.name should be same as above setter func name
        # self.name will call the function and set there nane
        # self.name = "TEST" ~ calling name()


student = Student("Ayush")

print(student.name)

student.name = "Abhinav"
print(student.name)


student.add_surname = "Srivastava"
print(student.name)



"""Chaining Decorators
In simpler terms chaining decorators means decorating a function with multiple decorators."""

def decor1(func): 
    def inner(): 
        x = func() 
        return x * x 
    return inner 

def decor2(func): 
    def inner(): 
        x = func() 
        return x * 2
    return inner 

# first decor2 will be called then decor1 and so on, works from bottom to top
@decor1     # 400
@decor2     # 20
def num(): 
    return 10


@decor2     # 200
@decor1     # 100
def num2(): 
    return 10


print(num()) 
print(num2())


"""
In Python, when multiple decorators are applied to a function, they are executed from the innermost (closest to the function) to the outermost.
"""