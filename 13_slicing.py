"""
Python list slicing is fundamental concept that let us easily access specific elements in a list. In this article, we'll learn the syntax and how to use both positive and negative indexing for slicing with examples.
"""


# list_name[start : end : step]
"""
start (optional): Index to begin the slice (inclusive). Defaults to 0 if omitted.
end (optional): Index to end the slice (exclusive). Defaults to the length of list if omitted.
step (optional): Step size, specifying the interval between elements. Defaults to 1 if omitted
"""

list_a = list(range(10))
print(list_a)

res = list_a[::]
print(res)

res = list_a[:]
print(res)


res = list_a[1:]
print(res)

res = list_a[-1:]       # get last element
print(res)


res = list_a[::2]       #skip 2 steps
print(res)


res = list_a[1:4:]       # or [1:4]
print(res)


res = list_a[1:4]
print(res)


"""
Out-of-bound slicing
In Python, list slicing allows out-of-bound indexing without raising errors. If we specify indices beyond the list length then it will simply return the available items.

Example: The slice a[7:15] starts at index 7 and attempts to reach index 15, but since the list ends at index 8, so it will return only the available elements (i.e. [8,9]).
"""

res = list_a[1:110]
print(res)


"""
Negative Indexing
Negative indexing is useful for accessing elements from the end of the list. The last element has an index of -1, the second last element -2, and so on.
"""
# -1 is the last index and -2 is the second last and so on

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get elements starting from index -2
# to end of list
b = a[-2:]
print(b)

# Get elements starting from index 0 
# to index -3 (excluding 3th last index)
c = a[:-3]
print(c)

# Get elements from index -4
# to -1 (excluding index -1)
d = a[-4:-1]
print(d)

# Get every 2nd elements from index -8
# to -1 (excluding index -1)
e = a[-8:-1:2]
print(e)


# reversing the list 
res = a[::-1]
print(res)



