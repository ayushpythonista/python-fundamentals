"""Python Arrays
In Python, array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together. Unlike Python lists (can store elements of mixed types), arrays must have all elements of same type. Having only homogeneous elements makes it memory-efficient."""

import array as arr

a = arr.array('i', [1, 2, 3, 4])
print(a)

print(a[0])



"""
Adding Elements to an Array
Elements can be added to the Python Array by using built-in insert() function. Insert is used to insert one or more data elements into an array. Based on the requirement, a new element can be added at the beginning, end, or any given index of array. append() is also used to add the value mentioned in its arguments at the end of the Python array.
"""

a.append(7)
print(a)

a.insert(2, 11)         # if an index value provided is greater than the array size it will insert at last 
print(a)

# unpack the array elements using *a 
print(*a)


a1, b1, *c1 = a
print(a1, b1, c1, sep=", ")
# it is like rest operator , assign rest remaining as list


arr1 = arr.array('i', [1, 2, 3, 1, 5])

"""Elements can be removed from the Python array by using built-in remove() function. It will raise an Error if element doesn't exist. Remove() method only removes the first occurrence of the searched element. To remove range of elements, we can use an iterator."""
arr1.remove(1)
print(arr1)


"""pop() function can also be used to remove and return an element from the array. By default it removes only the last element of the array. To remove element from a specific position, index of that item is passed as an argument to pop() method."""

arr1 = arr.array('i', [1, 2, 3, 1, 5, 6, 7, 11, 23, 66])
arr1.pop()
print(arr1)


arr1.pop(1)
print(arr1)

remove_item = arr1.pop(4)
print(remove_item)

# NOTE: here pop not only removes item but also returns the value that is removed


"""Slicing of an Array"""

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = arr.array('i', l)


Sliced_array = a[3:8]
print(Sliced_array)

Sliced_array = a[5:]
print(Sliced_array)

Sliced_array = a[:]
print(Sliced_array)


"""Searching Element in an Array
In order to search an element in the array we use a python in-built index() method. This function returns the index of the first occurrence of value mentioned in arguments."""
myarr = arr.array('i', [1, 2, 3, 1, 2, 5])

print(myarr.index(1))
print(myarr.index(5))
print(myarr.index(2))


"""Updating Elements in an Array"""
# update item at index 2
myarr[2] = 6
print(myarr)

# update item at index 4
myarr[4] = 8
print(myarr)


"""Different Operations on Python Arrays"""

arr2 = arr.array('i', [1, 2, 3, 4, 2, 5, 2])

# count returns the number of occurence
print(arr2.count(2))


arr2 = arr.array('i', [1, 2, 3, 4, 5])
# reverse the array
arr2.reverse()
print([*arr2])


a = arr.array('d', [1.5, 7, 3.9])       # it will convert int to float automatically
a.extend([6, 7.9, 11.4, 44])
print(a)
print([*a])

a.remove(3.9)
print([*a])



"""ARRAY FUNCTIONS"""

import array
    
# initializing array with array values
arr= array.array('i',[1, 2, 3, 1, 2, 5]) 
   
# using typecode to print datatype of array
print ("The datatype of array is : ", arr.typecode)


"""Array itemsize Function
This function returns the size in bytes of a single array element. In this example, we are using itemsize function to find out the size in byte of an array element."""
print ("The itemsize of array is : ", arr.itemsize)


# Return a tuple (address, length) giving the current memory address and the length in items of the buffer used to hold array's contents.
print(arr.buffer_info())


"""This function appends a whole array mentioned in its arguments to the specified array. In this example, we are using extend() to append another array."""
arr1 = array.array('i',[1, 2, 3, 1, 2, 5]) 
arr2 = array.array('i',[1, 2, 3]) 

arr1.extend(arr2)
print(arr1)
# TRIED EXTEND WITH LIST, it still works

"""This function is used to append a list mentioned in its argument to end of array. In this example, we are using fromlist() to append a list to end of array."""
li = [77, 54]

arr1.fromlist(li)   
print(arr1)


# array can extend with list and tuples and set also and even dict and the same works for list
arr3 = [99, 66]
arr1.extend(arr3)
print(arr1)


arr4 = (12, 34)
arr1.extend(arr4)
print(arr1)


arr5 = {312, 56}
arr1.extend(arr4)
print(arr1)


# in case of dict it uses keys
arr6 = {101: "YES", 205: "NO"}
arr1.extend(arr6)
print(arr1)


li.extend(arr6)
print(li)


# this return the new list  
list_a = arr1.tolist()
print(list_a)

