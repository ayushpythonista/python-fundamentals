"""In Python, numbers are a core data-type essential for performing arithmetic operations and calculations. Python supports three types of numbers, including integers, floating-point numbers and complex numbers. """

x = 555
y = 230.995
z = 56j

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

# Negative numbers
x = -565
print(x)
print(type(x))


# MATHS
res1 = 10 + 2

# Exponential
res2 = 2 ** 3
print(res2)

# let us find the absolute
res3 = abs(-69)
print(res3)


# Round off upto 2 decimal places
PI = 3.142678965
print(PI)
# unlike C++ in which I saw that on print decimal numbers it may give only upto 4 to 5 decimal places if not mentioned but in python it prints all 


pi_rounded = round(PI, 2)   # it will round to nearest decimal place
print(pi_rounded)


# FLOATS ~ This is a real number with a floating-point representation. It is specified by a decimal point. Optionally, the character e or E followed by a positive or negative integer may be appended to specify scientific notation. . Some examples of numbers that are represented as floats are 0.5 and -7.823457.

# after decimal Extra zeros present at the number’s end are ignored automatically.

x = 5.65
print(x)
print(type(x))

res = 5.65/2.3
print(res)

res1 = 6.354//3.36
print(res1)

res = 5.65//2.3
print(res)

# `//` ~ it returns the truncated quotient such as `1.0` or `2.0` 


# Python Complex
## A complex number is a number that consists of real and imaginary parts. For example, 2 + 3j is a complex number where 2 is the real component, and 3 multiplied by j is an imaginary part.
# EXAMPLE ~ 6 + 3j

x = 2 + 3j

print(x)
print(type(x))

j = 15
res = 2 + 3j / 6 + 1j
print(res)


res = 2.65j + 63j
print(res)


# res = 2.6 + 5.1j // 6.6 + 1.2j        #// TypeError: unsupported operand type(s) for //: 'complex' and 'float'
print(res)

# GET the real and imaginary part
var = 3 + 7j
realVar = var.real
imagVar = var.imag

print(realVar)
print(imagVar)

# get the conjugate
conjuVar = var.conjugate()      # generally it is reversing the symbol `+` <=> `-`

print(conjuVar)



# TYPE CONVERSION

var1: int = 2225
var2: float = 2225
var3: complex = 2 + 7j      

# for complex numbers the casting wont work but other number can be casted to complex and it adds + 0j there

print(type(var1))
print(int(var2))
# print(int(var3))          # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'

print(float(var1))
# print(float(var3))        # TypeError: float() argument must be a string or a real number, not 'complex'

print(complex(var1))
print(complex(var2))

"""
We can't convert a complex data type number into int data type and float data type numbers.
We can't apply complex built-in functions on strings.

"""

# RANDOM NUMBERS

## Let us use python random module to print python random numbers

import random

x = random.randint(1 , 100)
# this will generate random numbers from 1 to 100 both included

print(x)

# for negative numbers, remeber -1 the greatest negative number so reversing the order in randint parameter will raise error ~ raise ValueError(f"empty range in randrange({start}, {stop})")
x = random.randint(-100 , -1)
print(x)

# NOW the above will generate random numbers in interger, for float we can use

# ~ uniform

x = random.uniform(1.0, 3.665)
print(x)

# Same rule for -ve floats
x = random.uniform(-91.150669, -3.665)
print(x)


print(5.004500000000001000000)      # see here end zeros are ignored


# SPECIAL NUMBERS IN PYTHON
# NaN (Not a Number): NaN stands for “Not a Number” and is used to represent undefined or unrepresentable values such as the result of dividing 0 by 0.

# print(70/0)      # Any no. divided by zero raises error ~ ZeroDivisionError: division by zero


print(0/8828012)        # output ~ 0.0
print(0//8828012)       # output ~ 0


# Infinity and -Infinity: Python also supports positive and negative infinity, represented by float('inf') and float('-inf'), respectively. These are useful in various situations, such as when setting bounds for algorithms or detecting overflow conditions.


import math

x = math.nan

print(x)

x = float('inf')
y = float('-inf')

print(x)
print(y)
