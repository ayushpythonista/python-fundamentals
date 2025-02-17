"""
An iterator in Python is an object that holds a sequence of values and provide sequential traversal through a collection of items such as lists, tuples and dictionaries. . The Python iterators object is initialized using the iter() method. It uses the next() method for iteration.

__iter__(): __iter__() method initializes and returns the iterator object itself.
__next__(): the __next__() method retrieves the next available item, throwing a StopIteration exception when no more items are available.
"""


"""
Difference between Iterator and Iterable--

Iterables are objects that can return an iterator. These include built-in data structures like lists, dictionaries, and sets. Essentially, an iterable is anything you can loop over using a for loop. An iterable implements the __iter__() method, which is expected to return an iterator object.

Iterators are the objects that actually perform the iteration. They implement two methods: __iter__() and __next__(). The __iter__() method returns the iterator object itself, making iterators iterable as well.

"""

s = "GFG"
it = iter(s)

# this next we need to call everytime, if we store in variable then call then it will not work as expected bcoz it will store the variable then
print(next(it))
print(next(it))
print(next(it))


# Custom iterator
class EvenNumbers:
    def __iter__(self):
        self.n = 2  # Start from the first even number
        return self
    
    def __next__(self):
        x = self.n
        self.n += 2  # Increment by 2 to get the next even number
        return x
        # means whenever then next is called it will add +  to it

    def __printme__(self):
        print("Heyy Thanks")
        return "I got it"
    

even = EvenNumbers()

it = iter(even)

# Print the first five even numbers
print(next(it))  
print(next(it)) 
print(next(it))  
print(next(it)) 
print(next(it))


"""
StopIteration Exception
The StopIteration exception is integrated with Python's iterator protocol. It signals that the iterator has no more items to return. Once this exception is raised, further calls to next() on the same iterator will continue raising StopIteration."""

li = [100, 200, 300]
it = iter(li)

# Iterate until StopIteration is raised
while True:
    try:
        print(next(it))
    except StopIteration:
        print("End of iteration")
        break


# ALSO WE CAN USE

# Python code demonstrating
# basic use of iter()

listB = ['Cat', 'Bat', 'Sat', 'Mat']


iter_listB = listB.__iter__()

try:
    print(iter_listB.__next__())
    print(iter_listB.__next__())
    print(iter_listB.__next__())
    print(iter_listB.__next__())
    print(iter_listB.__next__())
except:
    print(" \nThrowing 'StopIterationError'",
                     "I cannot count more.")
    

"""SO we can use either --.__iter__() or iter(--) and --.__next__() or next(--)"""