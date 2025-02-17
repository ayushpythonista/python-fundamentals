"""

Python Boolean type is one of the built-in data types provided by Python, which represents one of the two values i.e. True or False. Generally, it is used to represent the truth values of the expressions.

Python Boolean Type
Boolean value can be of two types only i.e. either True or False. The output <class 'bool'> indicates the variable is a Boolean data type.

"""

a = True
print(type(a))

b = False
print(type(b))

# EMPTY, Zeroes or None values are always false

# Returns False as x is None
x = None
print(bool(x))

# Returns False as x is an empty sequence
x = ()
print(bool(x))

# Returns False as x is an empty mapping
x = {}
print(bool(x))

# Returns False as x is 0
x = 0.0
print(bool(x))

# Returns True as x is a non empty string
x = 'GeeksforGeeks'
print(bool(x))


# Negative or positive numbers are always true unless it is not zero
var1 = 0
print(bool(var1))

var2 = 1
print(bool(var2))

var3 = -9.7
print(bool(var3))


# NOT operator 
a = 0

## Boolean Not operator only requires one argument and returns the negation of the argument i.e. returns the True for False and False for True.
if not a:
    print(False)


# IS operator
## is keyword is used to test whether two variables belong to the same object. The test will return True if the two objects are the same else it will return False even if the two objects are 100% equal.

x = 15
y = 15
z = "15"


print(x is y)
print(x is z)

print(x == y)
print(x == z)

"""
is keyword checks if two variables point to the same object in memory.
In this case, both x and y are assigned the value 10. Python often optimizes memory for small integers, so both x and y reference the same object in memory.
Since x is y evaluates to True, the if block is executed and True is printed.

However, z is a string, and even though it contains the same characters as the integer value of x and y, it is a different object in memory. Therefore, x is z evaluates to False.
"""

a = 10+5
print(a)

# even after calculation it is evaulating to true means whenever same value if get the python assigns it to same object in memory 
print(a is x)



# IN OPERATOR
# in operator checks for the membership i.e. checks if the value is present in a list, tuple, range, string, etc.

a = [1, 2, 3 , 4 , 5]

# it will check whether 2 is present in array or not
if 2 in a:
    print(a)
else:
    print("un present")