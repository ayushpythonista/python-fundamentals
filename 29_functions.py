"""
Python Functions is a block of statements that return the specific task. The idea is to put some commonly or repeatedly done tasks together and make a function so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again.

"""

"""Functions as First-Class Objects
In Python, functions are first-class objects, meaning that they can be treated like any other object, such as integers, strings, or lists. This gives functions a unique level of flexibility and allows them to be passed around and manipulated in ways that are not possible in many other programming languages"""

def func():
    print("HEYY")
    

if __name__ == "__main__":
    func()


def add(a, b):
    return a + b

sum = add(10, 20)
print(sum)


# cleaner way

def multiply(a: int, b: int) -> int :
    print("a is ", a)
    return a * b

print(multiply(b=5, a=15))


"""
Types of Python Function Arguments
Python supports various types of arguments that can be passed at the time of the function call. In Python, we have the following function argument types in Python:

Default argument
Keyword arguments (named arguments)
Positional arguments
Arbitrary arguments (variable-length arguments *args and **kwargs)
"""

# Default argument
"""
A default argument is a parameter that assumes a default value if a value is not provided in the function call for that argument.
"""
def default_arg(x, y=101):
    print(f"X is {x} and Y is {y}")


default_arg(10, 11)

# if we do print(default_arg(10, 11)) then we will also get none printed bcoz it doesnt return any value


"""
Keyword Arguments
The idea is to allow the caller to specify the argument name with values so that the caller does not need to remember the order of parameters.

example is that suppose we have defined (firstName, lastName) function parameter
so either we can pass them in sequence or we can use names directly and so it donot require sequece
"""

def student(firstName, lastName):
    print(f"Student name is {firstName} {lastName}")

student("Ayush", "Sri")
student(firstName="Abhinav", lastName="Srivastava")
student(lastName="Kumar", firstName="Anand")



"""
Position-only arguments mean whenever we pass the arguments in the order we have defined function parameters in which if you change the argument position then you may get the unexpected output. We should use positional Arguments whenever we know the order of argument to be passed. So now, we will call the function by using the position-only arguments in two ways and In both cases, we will be getting different outputs from which one will be correct and another one will be incorrect.
"""

def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)


# You will get correct output because 
# argument is given in order
print("Case-1:")
nameAge("Suraj", 27)
# You will get incorrect output because
# argument is not in order
print("Case-2:")
nameAge(27, "Suraj")



"""
Arbitrary Keyword  Arguments

In Python Arbitrary Keyword Arguments, *args, and **kwargs can pass a variable number of arguments to a function using special symbols. There are two special symbols:

-- *args in Python (Non-Keyword Arguments)
-- **kwargs in Python (Keyword Arguments)
"""


def myFunc(*args):
    print(args)     # it is generally taking up all the variables as tuple
    print(type(args))
    for val in args:
        print(val)

myFunc("Ayush", "Abhinav", "Anita", "Anand")


def myFunc2(**kwargs):
    print(kwargs)
    print(type(kwargs))         # this is being treated as <class 'dict'>

myFunc2(firstName="Ayush", lastName="Srivastava")


def docStringFun():
    """Just for docstring"""
    pass

docStringFun()      # when we hover over this func name we can see the docstring written
# or we can also print using
print(docStringFun.__doc__)


"""Anonymous Functions in Python
In Python, an anonymous function means that a function is without a name. As we already know the def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions."""

def cube(x): return x**3

cube_v2 = lambda x: x**3

print(cube(2))
print(cube_v2(3))


"""
Recursive Functions in Python
Recursion in Python refers to when a function calls itself. There are many instances when you have to build a recursive function to solve Mathematical and Recursive Problems.

Using a recursive function should be done with caution, as a recursive function can become like a non-terminating loop. It is better to check your exit statement while creating a recursive function.
"""


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))


"""
Return Statement in Python Function
The function return statement is used to exit from a function and go back to the function caller and return the specified value or data item to the caller. The syntax for the return statement is:

return [expression_list]
The return statement can consist of a variable, an expression, or a constant which is returned at the end of the function execution. If none of the above is present with the return statement a None object is returned.
"""

# NOTE: in Python every variable name is a reference. When we pass a variable to a function Python, a new reference to the object is created.

"""below we can see python behavious that if values are same then python make reference so when we change anything by x it is also changed to list_a"""
def func(x):
    x[0] = 17

list_a = [10, 20, 30, 40, 50]
print(list_a)
func(list_a)
print(list_a)

# but if we completely assign a new value then the link is broken

def func2(x):
    x = 333

list_b = [10, 20, 30, 40, 50]
print(list_b)
func2(list_b)
print(list_b)



"""Passing Function as an Argument"""

# In Python, we can pass functions as arguments to other functions. We can pass a function by simply referencing its name without parentheses. The passed function can then be called inside the receiving function.


def findSquare(func, num):
    return func(num)


def square(num):
    return num ** 2


squareIs = findSquare(square, 8)

print("square is: ", squareIs)



"""PASS  - During the development of a Python program, we might want to create a function without implementing its behavior. In such cases, we can define the function and use the pass statement inside it to avoid syntax errors.
"""

def func():
    pass


"""Python Global variables are those which are not defined inside any function and have a global scope whereas Python local variables are those which are defined inside a function and their scope is limited to that function only. In other words, we can say that local variables are accessible only inside the function in which it was initialized whereas the global variables are accessible throughout the program and inside every function. """

var1 = 11
var2 = 77

def func():
    global var2
    # var1 = 7  ~ since here global is not defined hence this value change will affect only inside fun and if it not there then the func will use outside global var
    print("Var 1 is: ", var1)
    print("Var 2 is: ", var2)
    # var1 = 66         ~ if var1 is defined here above code will give error ~ UnboundLocalError: cannot access local variable 'var1' where it is not associated with a value
    var2 = 44       # since we have defined global above hence var2 will change inside and outside function both
    print("Var 1 Changed is: ", var1)
    print("Var 2 Changed is: ", var2)

    # any variable declared inside func is not accessible outside
    var_in = 55
    # if I try to print this variable outside it will give error
    # ------- func ends---------


print("Var 1 once is: ", var1)
print("Var 2 once is: ", var2)
func()
print("Var 1 next is: ", var1)
print("Var 2 next is: ", var2)



"""
Self

In Python, when defining methods within a class, the first parameter is always self. The parameter self is a convention not a keyword and it plays a key role in Python’s object-oriented structure.
"""

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        return self.brand, self.model
    # ------ class car ends

# Python automatically passes car1 as the first argument to display.
car1 = Car(brand="Toyota", model="Fortuner")
print(car1.display())



"""Assigning Functions to Variables"""
def msg(name):
    return name

my_msg = msg

print(my_msg("Ayush"))


"""Returning Functions from Other Functions"""

def func1(msg):
    def func2():
        return f"Message is {msg}"
    return func2

func_01 = func1("Hello")        # since this is returning a function we need to again call the function

print(func_01())


"""Storing Functions in Data Structures
Functions can be stored in data structures like lists or dictionaries."""

def add(x, y):
    return x + y


def subtract(a, b):
    return a - b


d = {
    "add": add,
    "subtract": subtract
}

print(d["add"])
print(d["add"](10, 17))     # basically then this will be like add(..)
print(d["subtract"](91, 23))
