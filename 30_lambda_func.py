# Python Lambda Functions are anonymous functions means that the function is without a name. As we already know the def keyword is used to define a normal function in Python. Similarly, the lambda keyword is used to define an anonymous function in Python. 


str1 = "Ayush"
str_lambda = lambda a : a.upper()

print(str_lambda(str1))


# ---

n = lambda x : "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(n(5))   
print(n(-3))  
print(n(0))


"""Lambda with Multiple Statements"""

calc = lambda x, y : (x + y, x * y)

print(calc(2, 3))


"""Using lambda with filter()"""
n = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, n)      # it is same as def func with odd even, this will filter out even numbers only and return it ~ [2, 4, 6]
print(list(even))


"""Using lambda with map()"""
a = [1, 2, 3, 4]
b = map(lambda x: x * 2, a)             # or def doubleFunc... (doubleFunc) .. this will double every number , [1 x 2, 2 x 2,...]
print(list(b))


"""Using lambda with reduce()"""
from functools import reduce

# Example: Find the product of all numbers in a list
a = [1, 2, 3, 4]
b = reduce(lambda x, y: x * y, a)       # def productIT... (productIT), this will give product of 1 x 2 x 3 x 4
print(b)