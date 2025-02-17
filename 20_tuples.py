"""
A tuple in Python is an immutable ordered collection of elements. Tuples are similar to lists, but unlike lists, they cannot be changed after their creation (i.e., they are immutable). Tuples can hold elements of different data types. The main characteristics of tuples are being ordered , heterogeneous and immutable.
"""

# Creating an empty Tuple
tup = ()
print(tup)

# Using String
tup = ('Geeks', 'For')
print(tup)

# Using List
li = [1, 2, 4, 5, 6]
print(tuple(li))

# Using Built-in Function
tup = tuple('Geeks')
print(tup)


# for single single we can do
tup1 = ("Ayush",)
print(tup1)


# Creating a Tuple with Mixed Datatype
tup = (5, 'Welcome', 7, 'Geeks')
print(tup)


# Creating a Tuple with nested tuples
tup1 = (0, 1, 2, 3)
tup2 = ('python', 'geek')
tup3 = (tup1, tup2)             # ((0, 1, 2, 3), ('python', 'geek'))
print(tup3)

# Creating a Tuple with repetition
tup1 = ('Geeks',) * 3
print(tup1)

# Creating a Tuple with the use of loop
tup = ('Geeks')
n = 5
for i in range(int(n)):
    tup = (tup,)                # tup inside tup inside tup
    print(tup)


"""
Accessing of Tuples
We can access the elements of a tuple by using indexing and slicing, similar to how we access elements in a list. Indexing starts at 0 for the first element and goes up to n-1, where n is the number of elements in the tuple. Negative indexing starts from -1 for the last element and goes backward.
"""

tup1 = tuple(range(15, 25))
print(tup1)


print(tup1[0])
print(tup1[5])

print(tup1[-1])
print(tup1[-3])


print(tup1[1:5])

print(tup1[::-1])



# Tuple unpacking
tup = ("Geeks", "For", "Geeks")

# This line unpack values of Tuple1
a, b, c = tup           # the variable should be same count as per tuple values
print(a)
print(b)
print(c)



"""
Concatenation of Tuples
Tuples can be concatenated using the + operator. This operation combines two or more tuples to create a new tuple.

Note- Only the same datatypes can be combined with concatenation, an error arises if a list and a tuple are combined. 
"""

tup1 = (0, 1, 2, 3)
tup2 = ('Geeks', 'For', 'Geeks')

tup3 = tup1 + tup2
print(tup3)


"""
Slicing of Tuple
Slicing a tuple means creating a new tuple from a subset of elements of the original tuple. The slicing syntax is tuple[start:stop:step].

Note- Negative Increment values can also be used to reverse the sequence of Tuples. 
"""

# Slicing of a Tuple with Numbers
tup = tuple('GEEKSFORGEEKS')            # string is array of chars so it will convert each values to tuple

print(tup)

# else use double bracket
tup2 = tuple((1, 2, 3, 4, 5))
print(tup2)

# Removing First element
print(tup[1:])

# Reversing the Tuple
print(tup[::-1])

# Printing elements of a Range
print(tup[4:9])



"""
Deleting a Tuple
Since tuples are immutable, we cannot delete individual elements of a tuple. However, we can delete an entire tuple using del statement.

Note- Printing of Tuple after deletion results in an Error. 
"""

tup = (0, 1, 2, 3, 4)
del tup

# print(tup)


tup = (0, 1, 2, 3, 4)
# tup[2] = 7          # TypeError: 'tuple' object does not support item assignment
print(tup)