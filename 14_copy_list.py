"""
Deep Copy and Shallow Copy in Python

In Python, assignment statements create references to the same object rather than copying it. Python provides the copy module to create actual copies which offer functions for shallow (copy.copy()) and deep (copy. deepcopy ()) copies. 

 * Deep copy in Python
    - A deep copy creates a new compound object before inserting copies of the items found in the original into it in a recursive manner.
    - It will first construct a new collection object and then recursively populate it with copies of the child objects found in the original. It means that any changes made to a copy of the object do not reflect in the original object. 

 * Shallow copy in Python
    - A shallow copy creates a new object but retains references to the objects contained within the original. It only copies the top-level structure without duplicating nested elements.
    - Changes made to a copy of an object do reflect in the original object. In python, this is implemented using the “copy.copy()” function. 
"""


import copy

a = list(range(0, 10))
print(a)

b = copy.deepcopy(a)
print(b)

# here we can see that we do change do b but a didnot changed
b[4] = 1999
print(b)
print(a)

# ----------=============================---------------------

"""NOTE: these are tested using nested lists"""

a = [[1, 2, 3], [4, 5, 6]]

# Creating a deep copy of the nested list 'a'
b = copy.deepcopy(a)

# Modifying an element in the deep-copied list
b[0][0] = 99 
print(b)

# ----------=============================---------------------

# but here we can see change in `c` bcoz it is shallow copy and python creates a reference hence changes are made in both
c = b
b[1] = 7777
print("b---", b)
print("c---", c)




# ----------=============================---------------------

a = [[1, 2, 3], [4, 5, 6]]

# Creating a shallow copy of the nested list 'original'
b = copy.copy(a)

# Modifying an element in the shallow-copied list
b[0][0] = 99

# Printing the original and shallow-copied lists  
print(b)
print(a)

# ----------=============================---------------------

