"""
Python Data types are the classification or categorization of data items. It represents the kind of value that tells what operations can be performed on a particular data. Since everything is an object in Python programming, Python data types are classes and variables are instances (objects) of these classes. The following are the standard or built-in data types in Python:


 - Numeric - int, float, complex
 - Sequence Type - string, list, tuple
 - Mapping Type - dict
 - Boolean - bool
 - Set Type - set, frozenset
 - Binary Types - bytes, bytearray, memoryview
"""

#  int, float, string, list and tuple
x = 50
x = 60.5
x = "Hello World"
x = ["geeks", "for", "geeks"]
x = ("geeks", "for", "geeks")
print(type(x))


"""
1. Numeric Data Types in Python
The numeric data type in Python represents the data that has a numeric value. A numeric value can be an integer, a floating number, or even a complex number. These values are defined as Python int , Python float , and Python complex classes in Python .


 * Integers - This value is represented by int class. It contains positive or negative whole numbers (without fractions or decimals). In Python, there is no limit to how long an integer value can be.
 * Float - This value is represented by the float class. It is a real number with a floating-point representation. It is specified by a decimal point. Optionally, the character e or E followed by a positive or negative integer may be appended to specify scientific notation.
 * Complex Numbers - A complex number is represented by a complex class. It is specified as (real part) + (imaginary part)j . For example - 2+3j
"""


"""INT() ~ Python int() function returns an integer from a given object or converts a number in a given base to a decimal."""

xint = 20
print(xint)
print(type(xint))

age = "21"
print("age =", int(age))

"""
Python int() Function Syntax
The syntax of the int() function in Python is as follows:


Syntax: int(x, base)


x [optional]: string representation of integer value, defaults to 0, if no value provided.
base [optional]: (integer value) base of the number.

Returns: Return decimal (base-10) representation of x
"""


# int() on string representation of numbers
print("int('9')) =", int('9'))
 
# int() on float values
print("int(9.9) =", int(9.9))
 
# int() on Python integer
print("int(9) =", int(9))


"""tht value passed must be string else it will raise error"""
# octal to decimal using int()
print("int() on 0o12 =", int('0o12', 8))
 
# binary to decimal using int()
print("int() on 0b110 =", int('0b110', 2))
 
# hexa-decimal to decimal using int()
print("int() on 0x1A =", int('0x1A', 16))



print(""" FLOAT--- - -  """)

# Python program to illustrate
# Various examples and working of float()
# for integers
x = 10.25
print(x)
print(type(x))
print(float(21.89))
 
# for floating point numbers
print(float(8))
 
# for integer type strings
print(float("23"))
 
# for floating type strings
print(float("-16.54"))
 
# for string floats with whitespaces
print(float("     -24.45   \n"))
 
# for inf/infinity
print(float("InF"))
print(float("InFiNiTy"))
 
# for NaN
print(float("nan"))
print(float("NaN"))


print("""Complex - - = -- ==-=---=-=-  """)
# complex()

x = 1 + 2j
print(x)
print(type(x))

# or
x = complex(1, 2)
print(x)
print(type(x))


"""in complex if second param is not there it will be 0j and second param if passed must be numeric"""