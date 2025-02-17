"""
Python set is an unordered collection of multiple items having different datatypes. In Python, sets are mutable, unindexed and do not contain duplicates. The order of elements in a set is not preserved and can change.

unordered
mutable
non duplicate
"""

set1 = {"ayush", "Abhinav"}

print(set1)
print(type(set1))

set1= set("Ayush Anand")

print(set1)


set1 = set((1, 2, 3, 4, 5))
print(set1)
print(type(set1))


# add single item
set1.add(6)
print(set1)


# add multiple item
set1.update([7, 8])         # or (7, 8)
print(set1)


set1.update((9, 10))        
print(set1)



# remove
set1.remove(2)
print(set1)

set1.discard(7)
print(set1)

"""
remove vs discard is that if value is not there then remove raises KeyError but discard donot raises error 
"""


"""
Using pop() Method
pop() method removes and returns an arbitrary element from the set. This means we don't know which element will be removed. If the set is empty, it raises a KeyError.


for list pop() removes last item and pop(index) removes as per index
tuple doesnot have pop bcoz it is immutable
dict pop(key) requires key
set pop() doesnot require any params
"""

set1.pop()
print(set1)


# clear clears the list
set1.clear()
print(set1)


"""
Frozen Sets in Python
A frozenset in Python is a built-in data type that is similar to a set but with one key difference that is immutability. This means that once a frozenset is created, we cannot modify its elements that is we cannot add, remove or change any items in it. Like regular sets, a frozenset cannot contain duplicate elements.

immutability
"""

# Creating a frozenset from a list
fset = frozenset([1, 2, 3, 4, 5])
print(fset)  

# Creating a frozenset from a set
set1 = {3, 1, 4, 1, 5}
fset = frozenset(set1)
print(fset)



"""
Python set Union() Method returns a new set that contains all the items from the original set.

The union of two given sets is the set that contains all the elements of both sets. The union of two given sets A and B is a set that consists of all the elements of A and all the elements of B such that no element is repeated.
"""

A = {2, 4, 5, 6} 
B = {4, 6, 7, 8}

C = A.union(B)
print(C)

# Union operator

D = A | B
print(D)


"""
The difference between the two sets in Python is equal to the difference between the number of elements in two sets. The function difference() returns a set that is the difference between two sets. Let's try to find out what will be the difference between two sets A and B. Then (set A - set B) will be the elements present in set A but not in B and (set B - set A) will be the elements present in set B but not in set A. 
"""

"""
A-B means the the elements that are in A but not in B
"""

A = {10, 20, 30, 40, 80}
B = {100, 30, 80, 40, 60}
print (A.difference(B))
print (B.difference(A))