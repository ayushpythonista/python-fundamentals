"""
Multi-dimensional lists in Python

There can be more than one additional dimension to lists in Python.

Multi-dimensional lists are the lists within lists. 

"""

list_a = [[1, 2, 3]]
print(list_a)

list_a.append([5, 6, 7])
print(list_a)

a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]] 
print(a) 

for record in a:
    print(record)


# using for loop printing each and every element

print("------------==-========----------")

"""
loops first ~ take the range length which resembles with (for i = 0; i < outer list; i++)
second loop ~ for j = 0l j < inner list; j++

we will get index then we can print
"""

# first find length of list
print(len(a))           # this print outer length
print(len(a[0]))        # this prints inner length based on index


for i in range(len(a)):
    for j in range(len(a[i])):
        print(f"Element at {i}-{j} is: ", a[i][j])

# let us beautify it
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")         # this print will not create new line just space
    print()     # this is just for new line after every outer loop


# Creating a multidimensional list with all zeros:
# using list comprehension

row  = 3
column = 5
multi_list = [[0 for x in range(column)] for y in range(row)]
print(multi_list)


a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]] 
print(a)
# 1. append(): Adds an element at the end of the list.
a.append([5, 10, 15, 20, 25]) 
print(a) 

# 2. extend(): Add the elements of a list (or any iterable), to the end of the current list.
## lets add to 2nd list
a[1].extend([11, 54, 99, 88, 55])
print(a) 

# 3. reverse(): Reverses the order of the list.
## reverse 3rd list

a[2].reverse()
print(a)

