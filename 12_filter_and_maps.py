"""
FILTER
The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

filter returns the filter object then we can convert it in list using list constructor
"""


def even(n):
    return n % 2 == 0

a = [x for x in range(20)]

filtered_a = filter(even, a)
print(list(filtered_a))


# filter with lambda

filtered_a = list(filter(lambda x: x % 2 != 0, a))
print(filtered_a)



"""
MAP
The map() function is used to apply a given function to every item of an iterable, such as a list or tuple, and returns a map object (which is an iterator).
"""

# using map convert every item to int
s = [str(x) for x in range(10)]
print(s)
print(type(s[1]))

x = list(map(int, s))
print(x)
print(type(x[1]))


def cube(n):
    return n**3

res = list(map(cube, x))
print(res)

res = list(map(cube, map(int, s)))
print(res)


res = list(map(even, x))        # it returns true false 
print(res)
# basically filter  filters but map performs certain operations


"""
Using map() with multiple iterables
We can use map() with multiple iterables if the function we are applying takes more than one argument.

Example: In this example, map() takes two iterables (a and b) and applies the lambda function to add corresponding elements from both lists.
"""

a = [1, 2, 3]
b = [4, 5, 6]

c = [9, 9, 9]

def add(x, y):
    return x+y

res = list(map(add, a, b))          # we can have multiple iterators but since the function we are using have only two params so we can pass two iterables only that means the number of list in map is proportional to the parameter of the function passed
print(res)


"""
NOTE: There are for tuple and list
"""

# converting the above add to lambda

res2 = list(map(lambda x, y: x+y, res, c))
print(res2)

# suppose we want to capitalize every word in list
list_a = ["apple", "mango", "banana"]

## but suppose if one is an int then it will raise error ~ TypeError: descriptor 'upper' for 'str' objects doesn't apply to a 'int' object
res = list(map(str.upper, list_a))
print(res)


# let us extract 1st character only
res = list(map(lambda x: x[0], res))
print(res)


# removing white space
s = ['  hello  ', '  world ', ' python  ']

res = list(map(str.strip, s))
print(res)


