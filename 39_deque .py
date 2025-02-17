"""A deque stands for Double-Ended Queue. It is a data structure that allows adding and removing elements from both ends efficiently. Unlike regular queues, which are typically operated on using FIFO (First In, First Out) principles, a deque supports both FIFO and LIFO (Last In, First Out) operations."""


"""Types of Restricted Deque Input
 - Input Restricted Deque:  Input is limited at one end while deletion is permitted at both ends.
 - Output Restricted Deque: output is limited at one end but insertion is permitted at both ends."""

"""OPERATIONS"""
"""

 - append(x): Adds x to the right end of the deque.
 - appendleft(x): Adds x to the left end of the deque.
 - extend(iterable): Adds all elements from the iterable to the right end.
 - extendleft(iterable): Adds all elements from the iterable to the left end (in reverse order).
 - remove(value): Removes the first occurrence of the specified value from the deque. If value is not found, it raises a ValueError.
 - pop(): Removes and returns an element from the right end.
 - popleft(): Removes and returns an element from the left end.
 - clear(): Removes all elements from the deque.

"""


from collections import deque

dq = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(dq)

dq.append(10)
print(dq)


# Add elements to the left
dq.appendleft(5)  
print("Append left 5: ", dq)

# extend(iterable)
dq.extend([50, 60, 70]) 
print("After extend([50, 60, 70]):", dq)

# extendleft(iterable) ` inserted like 11 5 0 7` ~ reverse order
dq.extendleft([7, 0, 5, 11])  
print("After extendleft([0, 5]):", dq)

# remove method
try:
    dq.remove(20)
    print("After remove(20):", dq)
except ValueError:
    dq.remove(6)
    print("After remove(6) with ValueError:", dq)

# Remove elements from the right
dq.pop()

# Remove elements from the left
dq.popleft()  

print("After pop and popleft:", dq)

# clear() - Removes all elements from the deque
dq.clear()  # deque: []
print("After clear():", dq)


"""
Accessing Item and length of deque
 - Indexing: Access elements by position using positive or negative indices.
 - len(): Returns the number of elements in the deque.
"""
dq = deque([1, 2, 3, 3, 4, 2, 4])

print(dq[0])  
print(dq[-1]) 

# Finding the length of the deque
print(len(dq))


"""deque (double-ended queue) in Python, from the collections module, provides optimized operations for appending and popping elements from both ends of the sequence. Compared to list, which provides constant time complexity for append operations (amortized O(1)), deque offers consistent O(1) time complexity for append and pop operations from both ends. This makes deque suitable for scenarios where efficient appends and pops are required from both ends of the sequence, such as implementing queues and stacks.

Count, Rotation and Reversal of a deque
 - count(value): This method counts the number of occurrences of a specific element in the deque.
 - rotate(n): This method rotates the deque by n steps. Positive n rotates to the right and negative n rotates to the left.
 - reverse(): This method reverses the order of elements in the deque.
"""

# Create a deque
dq = deque([10, 20, 30, 40, 50, 20, 30, 20])

# 1. Counting occurrences of a value
print(dq.count(20))  # Occurrences of 20
print(dq.count(30))  # Occurrences of 30

# 2. Rotating the deque
"""Last 2 elements (30, 20) move to the front.
Remaining elements shift right."""
dq.rotate(2)  # Rotate the deque 2 steps to the right
print(dq)


"""First 3 elements (30, 20, 10) move to the end.
Remaining elements shift lef"""
dq.rotate(-3)  # Rotate the deque 3 steps to the left
print(dq)

# 3. Reversing the deque
dq.reverse()  # Reverse the deque
print(dq)

