# The append() method does not return any value, it just modifies the original list in place.

import random

a = [random.randint(0, 100) for _ in range(10)]
print(a)


let_a = a.append(73)
print(let_a)        # None bcoz nothing return
# instrad check a as it will be modified

print(a)

# appending a list to list
a.append(list((444, 999)))
print(a)

"""No, append() can only add one element at a time. To add multiple elements we use the extend() method or we can use the append() method in a loop.

The append() method has a time complexity of O(1) (constant time) because it adds an element to the end of the list without requiring any resizing or reordering.

No, the append() method only adds elements to the end of the list. If we need to insert an element at a specific index we can use the insert() method.

No, the append() method will always add the entire list as a single element resulting in a nested list. To merge the contents of another list without nesting we use the extend() method instead.
"""


"""In Python, extend() method is used to add items from one list to the end of another list. This method modifies the original list by appending all items from the given iterable."""

a.extend((1, 2, 3))
print(a)


# we can also pass list in extend but it will not create a list just it will add elements in the list
b = ["Ayush", "abhinav"]
a.extend(b)
print(a)


# The extend() method can work with various types of iterables such as: Lists, Tuples, Sets and Strings (each character will be added separately)

b = ("Tup1", "Tup2")
a.extend(b)
print(a)

b = {"Set1", "Set2"}
a.extend(b)
print(a)

b = "abcde"         # NOTE: string is array of characters to it will append each character in list
a.extend(b)
print(a)


# extending lists in list  ~ basically creating 2d List
a = [random.randint(0, 100) for _ in range(10)]
b = [["L1, L2", "L3"], "L4"]
a.extend(b)
print(a)



# we can also extend a list using +
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)


"""Extend using slicing
Using slicing
We can use slicing with [:] to replace or extend the content of a list. It modifies the original list in-place, similar to extend().
"""

a[len(a):] = b
print(a)

"""a[len(a):] represents the slice starting at the end of the list.
Assigning b to this slice effectively appends all elements of b to a in-place.

NOTE: slicing in Python can be used to insert values at specific positions in a list, for instance, using a[:0], the values are added at the beginning of the list."""


# Using itertools.chain()
## The itertools.chain() method combines multiple iterables into one continuous sequence, which can be converted to a list or extended into an existing list.

from itertools import chain
# ~ Return a chain object whose .__next__() method returns elements from the first iterable until it is exhausted, then elements from the next iterable, until all of the iterables are exhausted.

n = [7, 8, 9]
a.extend(chain(n))
print(a)


"""Python List insert() method inserts an item at a specific index in a list."""

a = [1, 2, 4, 5]
print(a)

a.insert(2, 3)
print(a)

# inserting anything in list bcoz list can contain any data type values
a.insert(len(a), [6, 7, 8, 9])
print(a)


# let us say we want to insert an element before a specific element so first we can find the index of that element using .index() then insert
index = a.index(5)      # it returns index -> int

a.insert(index, 4.5)    # now this will insert before the element we specified
print(a)


# to insert element at the end we can use either len(a) or -1 but generally we use append() for single element at end or extend() for multiple at end of we can `+` two list also
a.extend(([1]))
print(a)

a.insert(-1, 10)
print(a)

"""`extend() and +` adds two list while append() and insert() can take integers also"""




"""
Python list remove() function removes the first occurrence of a given item from list. It make changes to the current list. It only takes one argument, element you want to remove and if that element is not present in the list, it gives ValueError.
"""

a = ['a', 'b', 'c']
a.remove("b")
print(a)



# Remove multiple items from list

# Original list
a = [1, 2, 3, 4, 5, 6, 7, 8]

# List of elements to remove
b = [2, 4, 6]


for item in b:
    if item in a:
        a.remove(item)

print(a)

res = list(range(20, 30))
# clearing the entire list 
res.clear()
print(res)


"""
Using deque for Frequently Removal

If we frequently need to remove elements from the start of the list then Python’s collections.deque provides a more efficient solution. Deques are optimized for appends and pops from both ends, which makes them faster than lists for such operations.

Explanation:

* deque() converts the list a into a deque object, this allowing efficient insertions and removals from both ends.
* a.popleft() removes and returns the first element in constant time (O(1)), making it far more efficient compared to a list for such operations.

NOTE: Adding or removing items at the start or end of a list takes a lot of time (O(n)) because all other elements need to shift. Whereas, deque do the same operations in just O(1) time.

"""

a = list(range(20, 30))

print(a)

from collections import deque

a2 = deque(a)
print(a2)


a2.popleft()
print(a2)


"""COUNT"""
# The count() method is used to find the number of times a specific element occurs in a list. It is very useful in scenarios where we need to perform frequency analysis on the data.
# we can pass any type of element in count 

count_a = a.count(25)
print(count_a)


a = [1, 1, 30, "Ayush", [1, 2], "Ayush", 11, 1, 30]

count_a = a.count(1)
print(count_a)

count_a = a.count([1, 2])
print(count_a)


# NESTED LIST COUNT
a = [[1, 2, 3], [4, 5, 6, 7, 5], [7, 8, 9]]
count_a = a.count([1, 2, 3])
print(count_a)

count_a = a[1].count(5)
print(count_a)


"SORT"
"""
Syntax of sort() method
- list_name.sort(key=None, reverse=False)


Parameter:
 - key (Optional): This is an optional parameter that allows we to specify a function to be used for sorting. For example, we can use the len() function to sort a list of strings based on their length.
 - reverse (Optional): This is an optional Boolean parameter. By default, it is set to False to sort in ascending order. If we set reverse=True, the list will be sorted in descending order.
"""

a = [5, 2, 9, 1, 5, 6]

# Sort the value in increasing order
a.sort()
print(a)


# Sorting in Descending Order
a.sort(reverse=True)
print(a)


# The key=len tells the sort() method
# to use length of each string during sorting
a = ["apple", "banana", "kiwi", "cherry"]
a.sort(key=len)
print(a)


"""
Sorting with a Custom Function
We can also define our custom sorting function to control the sorting behavior. In the the below example, we are sorting a list of tuples by the second element (those tuple whose second value are smaller would come first).
"""

a = [(1, 3), (2, 2), (3, 1)]

def sort_fun(x):
    return x[1]

a.sort(key=sort_fun)
print(a)


# sorting based on last character using lambda function
a = ["apple", "banana", "kiwi", "cherry"]

a.sort(key=lambda x: x[-1])
print(a)


"""
Case Insensitive Sort
By default, the sort() method is case sensitive, resulting in all capital letters being sorted before lowercase letters. To perform a case insensitive sort, we can use the str.lower function as the key.
"""

a = ["mango", "Banana", "apple", "Grape", "pear"]
a.sort()

print(a)        # this is first sorting caps then small


# lets lower then sort
a.sort(key=str.lower)       # it just sort based on cases but dont change the actual case
print(a)




"""SORTED"""

# sorted() function returns a new sorted list from the elements of any iterable like (e.g., list, tuples, strings ). It creates and returns a new sorted list and leaves the original iterable unchanged.

a = [4, 1, 3, 2]

b = sorted(a)
print(b)

# sorted(iterable, key=None, reverse=False)
"""
 - iterable: The sequence to be sorted. This can be a list, tuple, set, string, or any other iterable.
 - key (Optional): A function to execute for deciding the order of elements. By default it is None
 - reverse (Optional): If True, sorts in descending order. Defaults value is False (ascending order)
"""

# "reverse= True" helps sorted() to arrange the element 
#from largest to smallest elements
res = sorted(a, reverse=True)
print(res)


a = ["apple", "banana", "cherry", "date"]
res = sorted(a, key=len)
print(res)


a = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 91},
    {"name": "Eve", "score": 78}
]

# Use sorted() to sort the list 'a' based on the 'score' key
# sorted() returns a new list with dictionaries sorted by the 'score'

b = sorted(a, key=lambda a: a["score"])
print(b)




"""REVERSE"""
# The reverse() method is an inbuilt method in Python that reverses the order of elements in a list. This method modifies the original list and does not return a new list, which makes it an efficient way to perform the reversal without unnecessary memory uses.

a = [1, 2, 3, 4, 1, 2, 6] 

a.reverse() 

print(a)

# Or using slicing
"""
But slicing creates a new list while .reverse() modified the existing list

Explanation: The slicing approach [:: -1] creates a new list, which requires additional memory, whereas reverse() modifies the existing list.

Note: If we want to keep the original list without modifying it then should use slicing. But if we need to change the list directly then use reverse().
"""

a = [1, 2, 3, 4, 5]

res = a[::-1]

print(res)



"""INDEX"""

# list index() method searches for a given element from the start of the list and returns the position of the first occurrence.

a = ["cat", "dog", "tiger"]

print(a.index("dog"))


"""
Syntax: list_name.index(element, start, end) 

Parameters: 
- element: The element whose lowest index will be returned.
- start(optional): The position from where the search begins.
- end(optional): The position from where the search ends.
"""

a = [10, 20, 30, 40, 50, 40, 60, 40, 70]

# Find the index of 40 between index positions 4 and 8
res = a.index(40, 4, 8)
print(res)



a = [4, 7, 9, 7, 2, 7]

# find all the index of value 7
i = 0
list_a = []
for val in a:
    if val == 7:
        list_a.append(i)
    i+=1
print(list_a)


# Find all indices of the value 7
indices = []
start = 0

# more optimized bcoz here what will happen first index will come say 1 then 2nd time other index will come directly so loop will run only the times till value is there
while True:
    try:
        print(start)
        index = a.index(7, start)
        indices.append(index)
        start = index + 1
    except ValueError:
        break



"""Remove takes only elements"""

a = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, [1,2]]

a.remove([1,2])
print(a)

# and if element is not there then ~ ValueError: list.remove(x): x not in list


a = [10, 20, 30, 40]

""" pop without index removes last element while pop with index removes indexed element"""
# Remove the last element from list
val = a.pop()

print(val)
print(a)


a = ["Apple", "Orange", "Banana", "Kiwi"]

# Remove the 2nd index from list
val = a.pop(2)

print(val)
print(a)

"""
NOTE: removes modified the list while pop create a new list
"""
