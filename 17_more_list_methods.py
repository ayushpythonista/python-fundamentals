
print("""Find length of list-------""")

a = list(range(25, 35))

len_a = len(a)

print(len_a)


count = 0
for x in a:
    count+=1
print(count)

"""
Using length_hint()
The length_hint() function from the operator module provides an estimated length (not a guaranteed accurate count) of an iterable. This method is not typically used in regular code where len() is applicable.
"""

from operator import length_hint

l_a = length_hint(a)
print(l_a)


# ----------=-=-=-=-==-============---------
print("Find Largest Number in a List---------")

a = [10, 24, 76, 23, 12]

largest_a = max(a)
print(largest_a)


# everytime if val is greater than the coming value then it will store in largest
largest = a[0]
for val in a:
    if val > largest:
        largest = val
print(largest)


from functools import reduce
a = [10, 24, 76, 23, 12]
def greater(a, b):
    if a > b:
        return a
    else:
        return b
large_a = reduce(greater, a)
print(large_a)


large_a = reduce(lambda x, y : x if x > y else y, a)
print(large_a)



# using sort
# first sort the list and then return the last index val
a.sort()
large_a = a[-1]

print(large_a)

"""
Which method to choose?
 - Using max(): This is easiest and most recommended way.
 - Using a Loop: This method is good if we want to solve manually.
 - Using reduce(): An advanced option for those interested in functional programming.
 - Using sort(): This method is not recommended here due to its higher time complexity.
"""


# ----------=-=-=-=-==-============---------
print("Check if element exist in a List---------")


a = [10, 20, 30, 40, 50]

if 30 in a:
    print("Yess")
else:
    print("No")


"""
Using any()
The any() function is used to check if any element in an iterable evaluates to True. It returns True if at least one element in the iterable is truthy (i.e., evaluates to True), otherwise it returns False
"""

# means first create it where x is 30 and then any returns
truethy = any(x == 30 for x in a)
print(truethy)


"""
The count() function can also be used to check if an element exists by counting the occurrences of the element in the list. It is useful if we need to know the number of times an element appears.
"""

count_a = a.count(30)
print(count_a)


"""
- in Statement: The simplest and most efficient method for checking if an element exists in a list. Ideal for most cases.
- for Loop: Allows manual iteration and checking and provides more control but is less efficient than using 'in'.
- any(): A concise option that works well when checking multiple conditions or performing comparisons directly on list.
- count(): Useful for finding how many times an element appears in the list but less efficient for checking existance of element only.
"""

# ----------=-=-=-=-==-============---------
print("Ways to remove duplicates from list ---------")

a = [1, 2, 2, 3, 4, 4, 5]

# create set then convert to list 
list_a = list(set(a))
print(list_a)

# NOTE: Using set() removes duplicates but does not guarantee the order of elements.

new_a = []
for x in a:
    if x not in new_a:
        new_a.append(x)
print(new_a)

res = []
[res.append(x) for x in a if x not in res]
print(res)


# ----------=-=-=-=-==-============---------
print("Sum of list ---------")


a = [10, 20, 30, 40]

res = sum(a)
print(res)

n = 0
for x in a:
    n += x
print(n)

from functools import reduce
# reduce
total = reduce(lambda x, y: x + y, a)
print(total)


# ----------=-=-=-=-==-============---------
print("Merge Two Lists ---------")

a = [1, 2, 3]
b = [4, 5, 6]

c = a + b           # it returns a new list
print(c)

a.extend(b)         # it modifies the existing list
print(a)


a = [1, 2, 3]
b = [4, 5, 6]

# unpack the list and combine them in new list
c = [*a, *b]
print(c)


"""
Using the itertools.chain()
The itertools.chain() method from the itertools module provides an efficient way to merge multiple lists. It doesn't create a new list but returns an iterator, which saves memory, especially with large lists.
"""

from itertools import chain

a = [1, 2, 3]
b = [4, 5, 6]

c = chain(a, b)
c = list(c)
print(c)

"""

extend() WINS

Which method to choose?
 - + Operator: Quick and simple for small lists but can consume a lot of memory for larger ones.
 - extend() Method: Efficiently merges large lists by modifying the original list in place.
 - Unpacking (*): It provides a clean syntax, however, it may not be optimal for very large lists due to memory usage.
 - itertools.chain(): It works best for large lists. It merges without creating additional memory.
 - For Loop: It provides more control to use complex merging conditions.
 - List Comprehension: This is an alternative approach of using “for loop”, it has concise and cleaner syntax.

"""



# ----------=-=-=-=-==-============---------
print("SORTED ---------")


"""
Python sorted() function returns a sorted list. It is not only defined for the list and it accepts any iterable (list, tuple, string, etc.). It does not modify the given container and returns a sorted version of it.

It always returns a list
"""

a = (10, 12, 5, 1)
print(sorted(a))

# Sorting a set
s = {'gfg', 'course', 'python'}
print(sorted(s))

# Sorting a string
st = 'gfg'
print(sorted(st))

# Attempting to sort a dictionary (it will sort the keys)
d = {10: 'gfg', 15: 'ide', 5: 'course'}
print(sorted(d))

# Sorting a list of tuples
l = [(10, 15), (1, 8), (2, 3)]
print(sorted(l))


"""
The Python all() function returns true if all the elements of a given iterable (List, Dictionary, Tuple, set, etc.) are True otherwise it returns False. It also returns True if the iterable object is empty. Sometimes while working on some code if we want to ensure that user has not entered a False value then we use the all() function.
"""

print(all([True, True, False]))


# All elements of list are true
l = [4, 5, 1]
print(all(l))

""" where any any returns if any of the elements are true"""


print(any([True, True, False]))


# any elements of list are true
l = [4, 5, 1]
print(any(l))

print(any([False, False, False]))