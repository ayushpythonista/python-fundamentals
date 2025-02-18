# https://www.geeksforgeeks.org/generators-in-python/

"""A generator function is a special type of function that returns an iterator object. Instead of using return to send back a single value, generator functions use yield to produce a series of results over time. This allows the function to generate values and pause its execution after each yield, maintaining its state between iterations.
"""


def yield_fun(max_num):
    count = 1
    while count <= max_num: # loop until count is less than max as count start from 1
        yield count
        count+=1

counter = yield_fun(10)
print(list(counter)) #you can see here we creted list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# when use for loop it will return all one by one result

# let create a list of even numbers with yield function
def even_nums(max_num):
    num1 = 1
    while num1 <= max_num:
        if num1 % 2 == 0:
            yield num1
        num1 += 1
        

primes = even_nums(25)
print(list(primes))

# IN SHORT YIELD FEELS LIKE:
def func1():
    yield 1
    yield 2
    yield 3

# we can also print it using next()
gen_func1 = func1()
print(next(gen_func1))      # if you use next(func1()) it will generate same output ~ first one
print(next(gen_func1))
print(next(gen_func1))
# print(next(gen_func1))    #err ~ StopIteration

# it will return all but `return` will return once the first once and function breaks or stop

""" Python Generator Expression """
# like list comprehension we can generate generators then after that we can convert into list tuple or loop it
# let us create generator for cube of numbers

prime_cubes = (x**3 for x in range(50) if x % 2 == 0)
print(list(prime_cubes))

# State Management: Generators maintain their state between yields automatically. You can also pass data into the generator using the send() method.

def stateful_generator():
    value = yield       # as we will take value from outside
    while True:         # While True is used in order to make the generator active else if not used then when this gen is called onces after that it will be stopped
        value *= 5
        yield value     # OR ~ value = yield value * 5 
        

gen = stateful_generator()
next(gen)
gen_val = gen.send(10)
print(gen_val)
gen_val = gen.send(20)
print(next(gen))
print(next(gen))        # works ~ previous val * func val = 1250 * 5
# close it 
gen.close()
# print(next(gen))      # ERROR ~ StopIteration