"""The zip() function in Python combines multiple iterables such as lists, tuples, strings, dict etc, into a single iterator of tuples. Each tuple contains elements from the input iterables that are at the same position.
"""

names = ['John', 'Alice', 'Bob', 'Lucy']
scores = [85, 90, 78, 92]

res = zip(names, scores)
print(list(res))

# the count should be equal as is pairs, if there are uneven then low count will be taken and remaing will be ignored
# there should be a corresponding value for each element



# single zip

print(list(zip(names)))



"""In Python, zipping is a utility where we pair one list with the other. Usually, this task is successful only in the cases when the sizes of both the lists to be zipped are of the same size. But sometimes we require that different-sized lists also be zipped."""

"""itertools.cycle() repeats the shorter list to match the length of the longer list. This method is efficient for situations where we want the shorter list’s elements to cycle through continuously."""

print("-----------itertools.cycle--")
import itertools
a= [7, 8, 4, 5, 9, 10]
b= [1, 5, 6]

list_a = list(zip(a, itertools.cycle(b)))
print(list_a)


"""itertools.zip_longest() zips lists of different lengths by padding the shorter list with a specified value. It's useful when we need to ensure both lists are fully paired, filling missing values with a default value."""
res = list(itertools.zip_longest(a, b, fillvalue='X'))
print(res)


"""How to Zip two lists of lists in Python?"""
l1 = [[1, 2], [3, 4], [5, 6]]
l2=  [[7, 8], [9, 10], [11, 12]]

 # Zipping list
res = [(a, b) for a, b in zip(l1, l2)]
print(list(zip(l1, l2)))
print(res)


"""Python | Ways to sort a zipped list by values"""
print("sort zipped list-------------")

"""Using sorted() with operator.itemgetter()
operator.itemgetter() is a fast way to sort a zipped list by values. It efficiently retrieves specific elements from tuples, making it ideal for sorting large datasets."""

import operator
a = ['akshat', 'manjeet', 'nikhil']
b = [3, 2, 1]
zipped = zip(a,b)

# Converting to list
zipped = list(zipped)
print("zipped: ", zipped)

# Using sorted and operator
res = sorted(zipped, key = operator.itemgetter(1))
print("--", res)


res = sorted(zipped, key = lambda x : x[0])
print("---", res)

"""NOTE: in sorting always remeber that if there are mixed case like capital and small then the capital one is sorted first"""

zipped_2 = list(zip(a, b))
zipped_2.sort(key=lambda x : x[1])
print(zipped_2)



