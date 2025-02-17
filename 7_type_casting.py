# Type Casting is the method to convert the Python variable datatype into a certain data type in order to perform the required operation by users. 

x = 5
y = str(x)

print(x)
print(type(x))
print(y)
print(type(y))

"""
 There can be two types of Type Casting in Python:

 * Python Implicit Type Conversion
 * Python Explicit Type Conversion
"""


# Implicit Type Conversion in Python
## In this, method, Python converts the datatype into another datatype automatically. Users don’t have to involve in this process.

a = 7
print(type(a))

b = "Ayush"
print(type(b))

c = 3.012
print(type(c))

# here above we can see python automatically assigns a datatype to variable based on values given


# see a is 7 (int) but when we multiply it will float so result will be float and variable will be converted to float implicitly

a = a * c
print(a)
print(type(a))      # ~ <class 'float'>


# Explicit Type Conversion in Python
## In this method, Python needs user involvement to convert the variable data type into the required data type. 

"""
* Int(): Python Int() function take float or string as an argument and returns int type object.
* float(): Python float() function take int or string as an argument and return float type object.
* str(): Python str() function takes float or int as an argument and returns string type object.
"""

print(int(a))

print(float(7735))


print(str(98))



# we can convert string to int but if it is not a number it will give error

var = 't'
# print(int(var))         # ValueError: invalid literal for int() with base 10: 't'





