"""

In Python, a list is a built-in dynamic sized array (automatically grows and shrinks). We can store all types of items (including another list) in a list. A list may contain mixed type of items, this is possible because a list mainly stores references at contiguous locations and actual items maybe stored at different locations.

* List can contain duplicate items.
* List in Python are Mutable. Hence, we can modify, replace or delete the items.
* List are ordered. It maintain the order of elements based on how they are added.
* Accessing items in List can be done directly using their position (index), starting from 0.

"""

list_a = [1, 1, 'a', 'a', 7, 9, "Ayush" ]
print(list_a)

# mutable
list_a[3] = "Blah Blah"
print(list_a)

var_a = list_a[4]
print(var_a)


# add items in list
list_a.append(20)
print(list_a)
# since list is mutable so it can change the items for that existing list without creating a new list

# remove
list_a.remove(9)    # Remove first occurrence of value.
# If value is not there then error is ~ ValueError: list.remove(x): x not in list
print(list_a)


# we can also create list Using list() Constructor
list_b = list((1, 2, 3, 4, 5))          # we need two brackets inside else will raise error ~ TypeError: list expected at most 1 argument, got 5
print(list_b)
print(type(list_b))


# creating list with repeating element (same as string) using `*`
a = [9] * 7
print(a)


# accessing list elements ~ most of the thing we will find same as string becoz string is also array of characters

# GET element by index
print(list_a[-1])       # gives last element
print(list_a[0])  


# WAYS TO ADD ITEMS IN LIST
"""
append(): Adds an element at the end of the list.
extend(): Adds multiple elements to the end of the list.
insert(): Adds an element at a specific position.
"""
list_a.append("let greet")
print(list_a)

list_a.extend((4, "OK", 7))         # it also takes one parameter so pass in bracket
print(list_a)


# lets insert at 3rd index
list_a.insert(3, "DUDEE!")
print(list_a)


# UPDATING by index
list_a[3] = "BABYY!"
print(list_a)

"""
Removing Elements from List
We can remove elements from a list using:

remove(): Removes the first occurrence of an element.
pop(): Removes the element at a specific index or the last element if no index is specified.
del statement: Deletes an element at a specified index.
"""

# it deletes first occurence only like `7` is present twice but only first one will be removed
list_a.remove(7)
print(list_a)

list_a.pop()        # removes last if index not specified
print(list_a)

list_a.pop(3)       # remove from specific index
print(list_a)


# delete a specific elem using `del` keyword
del list_a[4]
print(list_a)

# deleting entire list
del list_a
# print(list_a)     # raises error bcoz the variable and its data has been deleted
# ~ NameError: name 'list_a' is not defined.


# Looping list
fruits = ['apple', 'banana', 'cherry']

for items in fruits:
    print(items)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# lets say we want 5 -> 2nd row 2nd column
item = matrix[1][1]
print(item)

item = matrix[0][2]
print(item)

# if index not there then err is ~ IndexError: list index out of range


# List unpacking
list_a = ["Ayush", "Anand", "Srivastava"]

# This line unpack values of list_a
a, b, c = list_a                # the variable should be same count as per list values
print(a)
print(b)
print(c)
