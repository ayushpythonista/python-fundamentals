"""
------- Memory allocation -------

Memory allocation can be defined as allocating a block of space in the computer memory to a program. In Python memory allocation and deallocation method is automatic as the Python developers created a garbage collector for Python so that the user does not have to do manual garbage collection.
"""

"""
------- Garbage collection -------

Garbage collection is a process in which the interpreter frees up the memory when not in use to make it available for other objects.
Assume a case where no reference is pointing to an object in memory i.e. it is not in use so, the virtual machine has a garbage collector that automatically deletes that object from the heap memory

Garbage collection is a memory management technique used in programming languages to automatically reclaim memory that is no longer accessible or in use by the application. It helps prevent memory leaks, optimize memory usage, and ensure efficient memory allocation for the program.
"""

"""
------- Reference Counting -------

Reference counting works by counting the number of times an object is referenced by other objects in the system. When references to an object are removed, the reference count for an object is decremented. When the reference count becomes zero, the object is deallocated.

Python and various other programming languages employ reference counting, a memory management approach, to automatically manage memory by tracking how many times an object is referenced. A reference count, or the number of references that point to an object, is a property of each object in the Python language. When an object’s reference count reaches zero, it becomes un-referenceable and its memory can be freed up.

For example, Let’s suppose there are two or more variables that have the same value, so, what Python virtual machine does is, rather than creating another object of the same value in the private heap, it actually makes the second variable point to that originally existing value in the private heap. Therefore, in the case of classes, having a number of references may occupy a large amount of space in the memory, in such a case referencing counting is highly beneficial to preserve the memory to be available for other objects

`x = 10`


When x = 10 is executed an integer object 10 is created in memory and its reference is assigned to variable x, this is because everything is object in Python.

"""


x = 10
y = x 

if id(x) == id(y): 
    print("x and y refer to the same object") 


"""In the above example, y = x will create another reference variable y which will refer to the same object because Python optimizes memory utilization by allocation the same object reference to a new variable if the object already exists with the same value."""

# Now, let’s change the value of x and see what happens.

x += 1
  
if id(x) != id(y): 
    print("x and y do not refer to the same object") 


# So now x refer to a new object x and the link between x and 10 disconnected but y still refer to 10.



import sys
 
# Create an object
x = [1, 2, 3]
y = x
# Get reference count
ref_count = sys.getrefcount(x)
 
print("Reference count of x:", ref_count)



