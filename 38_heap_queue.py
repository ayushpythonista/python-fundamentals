"""A heap queue or priority queue is a data structure that allows us to quickly access the smallest (min-heap) or largest (max-heap) element. A heap is typically implemented as a binary tree, where each parent node's value is smaller (for a min-heap) or larger (for a max-heap) than its children. However, in Python, heaps are usually implemented as min-heaps which means the smallest element is always at the root of the tree, making it easy to access."""


"""Creating a Heap Queue"""

import heapq

li = [10, 20, 15, 30, 40]

# transform list in heap
heapq.heapify(li)

print(type(li))

"""heapq.heappush() function adds a new element to the heap while maintaining the heap order.
heapq.heappop() function removes the smallest element from the heap and returns it."""

# Appending an element
heapq.heappush(li, 5)

print(li)


# Pop the smallest element from the heap and also remove it
n = heapq.heappop(li)
print(n)
print(li)


"""Push a new element (5) and pop the smallest element at the same time and also returned the removed item"""

heapq.heappushpop(li, 114)
print(li)


"""Finding the Largest and Smallest Elements in a Heap Queue
Although a heap allows for efficient access to the smallest element, it doesn’t directly support finding the largest element. However, the heapq module provides two handy functions, nlargest() and nsmallest(), to retrieve the largest and smallest elements from the heap, respectively.

- nlargest() and nsmallest()
These functions allow us to easily find the n largest or n smallest elements in a heap. They do this by efficiently scanning the heap and sorting the required number of elements.

-- heapq.nlargest(n, iterable) returns the n largest elements from the iterable.
-- heapq.nsmallest(n, iterable) returns the n smallest elements from the iterable.

if n is greater than count then it returns all"""


h = [10, 20, 15, 30, 40]
heapq.heapify(h)

# top 3 large from h
print(heapq.nlargest(3, h))

# top 2 small from h
print(heapq.nsmallest(2, iterable=h))


"""heapq.heapreplace() function is a combination of pop and push. It pops the smallest element from the heap and inserts a new element into the heap, maintaining the heap property. This operation is useful when we want to replace the smallest element with a new value in a heap.

- It returns the smallest element before replacing it.
- It is more efficient than using heappop() followed by heappush() because it performs both operations in one step."""


min = heapq.heapreplace(li, 17)
print(min)
print(li)


"""heapq.merge() function is used to merge multiple sorted iterables into a single sorted heap. It returns an iterator over the sorted values, which we can then iterate through.

This operation is efficient because it avoids sorting the elements from scratch. Instead, it merges already-sorted iterables in a way that maintains the heap property."""
# Merging Heaps
h2 = [2, 4, 6, 8]

h3 = list(heapq.merge(h, h2))
print(h3)

