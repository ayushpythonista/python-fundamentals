# Python code to illustrate 
# Decorators with parameters in Python 
def decorator(like):
    print("Inside decorator")
    
    def inner(func):
        # code functionality here
        print("Inside inner function")
        print("I like", like) 
        
        def wrapper():
            func()
        
        return wrapper
    
    # returning inner function 
    return inner

@decorator(like="Coding")
def my_func():
    print("Inside actual function")

# Call the decorated function
my_func()


# ------------=== ------------

# Python code to illustrate 
# Decorators with parameters in Python 

def decorator_func(x, y):

    def Inner(func):

        def wrapper(*args, **kwargs):
            print("I like Geeksforgeeks")
            print("Summation of values - {}".format(x+y) )

            func(*args, **kwargs)
            
        return wrapper
    return Inner


# Not using decorator 
def my_fun(*args):
    for ele in args:
        print(ele)

# another way of using decorators
decorator_func(12, 15)(my_fun)('Geeks', 'for', 'Geeks')


# with decorator
@decorator_func(x = 15, y = 22)
def my_fun(*args):
    for ele in args:
        print(ele)

my_fun('Ayush', 'Anand', 'Srivastava')



"""While function-based decorators are widely used, class-based decorators can offer more flexibility and better organization, especially when the decorator needs to maintain state or requires multiple methods to function properly. A Python class decorator is simply a class that implements the __call__ method, allowing an instance of the class to be used as a decorator."""


import time

class TimerDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {self.func.__name__} executed in {end_time - start_time} seconds")
        return result

@TimerDecorator
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

# Usage
print(example_function(100000000))



class DoubleReturnDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        return result * 2

@DoubleReturnDecorator
def add(a, b):
    return a + b
# we will see that the results will be doubling so for class the decorator uses the __call__ function defined


# Usage
print(add(3, 5))  
print(add(10, 20)) 