"""
The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along. This function is defined in “functools” module.


 - filters filter from the list and returns value according to condition
 - map is like perform operation on every element
 - reduce perform the operation on every element and reduce returns the output and it takes two params
"""
from functools import reduce

a = [1, 2, 3, 4, 5]

reduce_a = reduce(lambda x,y: x+y, a)
print(reduce_a)


"""
Explanation:

The reduce() function applies add() cumulatively to the elements in numbers. First, 1 + 2 = 3. Then, 3 + 3 = 6. And so on, until all numbers are processed.
The final result is 15.

"""
"""
Syntax of reduce()
functools.reduce(function, iterable[, initializer])

- function: A function that takes two arguments and performs an operation on them.
- iterable: An iterable whose elements are processed by the function.
- initializer (optional): A starting value for the operation. If provided, it is placed before the first element in the iterable.
"""


def add(x, y):
    return x + y

a = [1, 2, 3, 4, 5]
res = reduce(add, a)

print(res)
