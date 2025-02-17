"""
Inserting an element into a sorted list while maintaining the order is a common task in Python. It can be efficiently performed using built-in methods or custom logic. In this article, we will explore different approaches to achieve this.
"""

# Using bisect.insort
"""
bisect module provides the insort function which inserts an element into a sorted list at the correct position, bisect.insort and performs a binary search to find the correct position which makes it more efficient than manual iteration.
"""


a = [1, 3, 4, 7, 10]

import bisect

bisect.insort(a, 5)

print(a)


# ----
a = [1, 3, 4, 7, 10]
insert_val = 5
for i in range(len(a)):
    if a[i] > insert_val:
        a.insert(i, insert_val)
        break
print(a)  


insert_val = 5
a = [1, 3, 4, 7, 10]
for i in range(len(a)):
    if insert_val < a[i]:
        a.insert(i, insert_val)
        break
print(a)


# list comprehenion

# make two list one less and one greater then join them
a = [1, 3, 4, 7, 10]
list_a = [x for x in a if x < insert_val] + [insert_val] + [x for x in a if x > insert_val]
print(list_a)


# first append then sort
a = [1, 3, 4, 7, 10]
a.append(5)
a.sort()
print(a)

