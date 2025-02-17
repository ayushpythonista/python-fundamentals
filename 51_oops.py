"""
Object Oriented Programming is a fundamental concept in Python, empowering developers to build modular, maintainable, and scalable applications. By understanding the core OOP principles (classes, objects, inheritance, encapsulation, polymorphism, and abstraction), programmers can leverage the full potential of Python OOP capabilities to design elegant and efficient solutions to complex problems.
"""


"""OOPs Concepts in Python
Class in Python
Objects in Python
Polymorphism in Python
Encapsulation in Python
Inheritance in Python
Data Abstraction in Python"""



"""A class is a collection of objects. Classes are blueprints for creating objects. A class defines a set of attributes and methods that the created objects (instances) can have.


Some points on Python class:  

- Classes are created by keyword class.
- Attributes are the variables that belong to a class.
- Attributes are always public and can be accessed using the dot (.) operator. Example: Myclass.Myattribute
"""

class Employee():
    gender = "Male"

    # NOTE: self parameter is a reference to the current instance of the class. It allows us to access the attributes and methods of the object.
    def __init__(self, name, age):      # helps to Initializes the name and age attributes when a new object is created
        print("Employee Class")
        print(self)
        print(name, age)
        self.name = name
        self.age = age


# Here we are creating the object of employee class
employee = Employee(name="Ayush", age=29)

print("EMployee name is: ", employee.name)
print("and his age is: ", employee.age)

employee.name = "Abhinav"
print("Another EMployee name is: ", employee.name)


print("The gender of employee is: ", employee.gender)

employee.gender = "Female"
print("We can also have ", employee.gender, " employees")


#  ---------------------------
print("""-- Inheritance ------""")

"Inheritance allows a class (child class) to acquire properties and methods of another class (parent class). It supports hierarchical classification and promotes code reuse."

"""
Types of Inheritance:
 - Single Inheritance: A child class inherits from a single parent class.
 - Multiple Inheritance: A child class inherits from more than one parent class.
 - Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another class.
 - Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
 - Hybrid Inheritance: A combination of two or more types of inheritance.
"""

class Dog:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Dog's Name: {self.name}")


class Labrador(Dog):  # Single Inheritance
    def sound(self):
        print("Labrador woofs")


labrador = Labrador("Tommy")

labrador.sound()
labrador.display_name()


# Multilevel Inheritance
class GuideDog(Labrador):  # Multilevel Inheritance
    def guide(self):
        print(f"{self.name} Guides the way!")


guideDog = GuideDog(name="Max")
guideDog.guide()


# Multiple Inheritance
class Friendly:
    def greet(self):
        print("Friendly!")

class GoldenRetriever(Dog, Friendly):  # Multiple Inheritance
    def sound(self):
        print("Golden Retriever Barks")

retriever = GoldenRetriever("Charlie")
retriever.display_name()
retriever.greet()
retriever.sound()


"""Python Polymorphism
Polymorphism allows methods to have the same name but behave differently based on the object's context. It can be achieved through method overriding or overloading.


Types of Polymorphism
 - Compile-Time Polymorphism: This type of polymorphism is determined during the compilation of the program. It allows methods or operators with the same name to behave differently based on their input parameters or usage. It is commonly referred to as method or operator overloading.
 - Run-Time Polymorphism: This type of polymorphism is determined during the execution of the program. It occurs when a subclass provides a specific implementation for a method already defined in its parent class, commonly known as method overriding.
"""


# Parent Class
class Dog:
    def sound(self):
        print("dog sound")  # Default implementation

# Run-Time Polymorphism: Method Overriding
class Labrador(Dog):
    def sound(self):
        print("Labrador woofs")  # Overriding parent method

class Beagle(Dog):
    def sound(self):
        print("Beagle Barks")  # Overriding parent method


# Compile-Time Polymorphism: Method Overloading Mimic
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c  # Supports multiple ways to call add()
    

# Run-Time Polymorphism
dogs = [Dog(), Labrador(), Beagle()]
for dog in dogs:
    dog.sound()  # Calls the appropriate method based on the object type


# Compile-Time Polymorphism (Mimicked using default arguments)
calc = Calculator()
print(calc.add(5, 10))  # Two arguments
print(calc.add(5, 10, 15))  # Three arguments
"""Compile-Time Polymorphism:

Python does not natively support method overloading. Instead, we use a single method (add) with default arguments to handle varying numbers of parameters.
Different behaviors (adding two or three numbers) are achieved based on how the method is called."""


dogClasses = (Dog(), Labrador(), Beagle())
for dogClass in dogClasses:
    dogClass.sound()



"""Python Encapsulation
Encapsulation is the bundling of data (attributes) and methods (functions) within a class, restricting access to some components to control interactions.


Types of Encapsulation:
 - Public Members: Accessible from anywhere.
 - Protected Members: Accessible within the class and its subclasses.
 - Private Members: Accessible only within the class.
"""


class Dog:
    def __init__(self, name, breed, age):
        self.name = name  # Public attribute
        self._breed = breed  # Protected attribute
        self.__age = age  # Private attribute

    # Public method
    def get_info(self):
        return f"Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"

    # Getter and Setter for private attribute
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")


# Example Usage
dog = Dog("Buddy", "Labrador", 3)

# Accessing public member
print(dog.name)  # Accessible

# Accessing protected member
print(dog._breed)  # Accessible but discouraged outside the class


# print(dog.__age)    # AttributeError: 'Dog' object has no attribute '__age'

# Accessing private member using getter
print(dog.get_age())

# Modifying private member using setter
dog.set_age(5)
print(dog.get_info())


"""Data Abstraction 
Abstraction hides the internal implementation details while exposing only the necessary functionality. It helps focus on “what to do” rather than “how to do it.”

Types of Abstraction:
Partial Abstraction: Abstract class contains both abstract and concrete methods.
Full Abstraction: Abstract class contains only abstract methods (like interfaces)."""


from abc import ABC, abstractmethod

class Dog(ABC):  # Abstract Class
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):  # Abstract Method
        pass

    def display_name(self):  # Concrete Method
        print(f"Dog's Name: {self.name}")


class GermanShepherd(Dog):  # Partial Abstraction
    def sound(self):
        print("Labrador Woof!")


class Beagle(Dog):  # Partial Abstraction
    def sound(self):
        print("Beagle Bark!")


dog = GermanShepherd("TOmmy")
dog.display_name()
dog.sound()

dog = Beagle("Max")
dog.display_name()
dog.sound()

"""
 - Partial Abstraction: The Dog class has both abstract (sound) and concrete (display_name) methods.
 - Why Use It: Abstraction ensures consistency in derived classes by enforcing the implementation of abstract methods.
"""


# NOTE: In Python, we use double underscore (Or __) before the attributes name and those attributes will not be directly visible outside. 



class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."  # Correct: Returning a string
    

dog1 = Dog("Buddy", 3)
print(dog1)


class Test: 
    def __init__(self, a, b): 
        self.a = a 
        self.b = b 
  
    def __repr__(self): 
        return "Test a:%s b:%s" % (self.a, self.b) 
  
    def __str__(self): 
        return "From str method of Test: a is %s, b is %s" % (self.a, self.b) 
  
# Driver Code         
t = Test(1234, 5678) 
print(t) # This calls __str__() 
print([t]) # This calls __repr__() 


print(repr(t))  # Calls __repr__
print(str(t))   # Calls __str__
print(t)        # Calls __str__ implicitly



"""super() Function
super() function is used to call the parent class's methods. In particular, it is commonly used in the child class's __init__() method to initialize inherited attributes. This way, the child class can leverage the functionality of the parent class."""


# Parent Class: Person
class Person:
    def __init__(self, name, idnumber):
        print("Hiii")
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)


# Child Class: Employee
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        super().__init__(name, idnumber)    # this is even calling the person ~ parent class, if we comment this we will see the parent class print is not getting printed
        self.salary = salary
        self.post = post
        super().display()   # we are calling the parent function as super() help us to access parent class methods


employee = Employee(name="Ayush", idnumber=1445, salary=50000, post="Senior")

      


