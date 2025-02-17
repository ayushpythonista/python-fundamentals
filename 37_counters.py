from collections import Counter

val = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

ctr = Counter(val)

print(ctr)


ctr2 = Counter([3, 1, 2, 3, 7, 8, 1])
print(ctr2)

"""Accessing Counter Elements
We can access the count of each element using the element as the key. If an element is not in the Counter, it returns 0."""

print(ctr2[7])
print(ctr2[3])
print(ctr2[30])     


"""Updating counters
Counters can be updated by adding new elements or by updating the counts of existing elements. We can use the update() method to achieve this."""
ctr2.update([2, 3, 3, 7, 9])
print(ctr2)


"""elements(): Returns an iterator over elements repeating each as many times as its count. Elements are returned in arbitrary order."""

print(list(ctr2.elements()))

"""only doing this list(ctr2) will return the counter keys that is [3, 1, 2, 7, 8, 9] the numbers signled after counter it"""


"""most_common(): Returns a list of the n most common elements and their counts from the most common to the least. If n is not specified, it returns all elements in the Counter."""

common = ctr2.most_common(2)
print(common)


common = ctr2.most_common(3)
print(common)


common = ctr2.most_common()
print(common)

# if number is greater still it returns all
common = ctr2.most_common(100)
print(common)



"""The subtract() method decreases the counts for elements found in another iterable."""
ctr = Counter([1, 2, 2, 3, 3, 3])
ctr.subtract([2, 3, 7, 8, 8])
print(ctr)



"""Arithmetic Operations on Counters
Counters support addition, subtraction, intersection union operations, allowing for various arithmetic operations."""
ctr1 = Counter([1, 2, 2, 3])
ctr2 = Counter([2, 3, 3, 4])
# Addition
print(ctr1 + ctr2)  
# Subtraction
print(ctr1 - ctr2)  

# Intersection
print(ctr1 & ctr2)  
# Union
print(ctr1 | ctr2)


