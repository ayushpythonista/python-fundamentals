"""
Python Data types are the classification or categorization of data items. It represents the kind of value that tells what operations can be performed on a particular data. Since everything is an object in Python programming, Python data types are classes and variables are instances (objects) of these classes. The following are the standard or built-in data types in Python:

Numeric: int, float, complex
Sequence Type: string, list, tuple
Mapping Type: dict
Boolean: bool
Set Type: set, frozenset
Binary Types: bytes, bytearray, memoryview


"""

# This code assigns variable ‘x’ different values of few Python data types – int, float, list, set and string. Each assignment replaces the previous value, making ‘x’ take on the data type and value of the most recent assignment.

x = 5
x = 77.963
x = "Hello Ayush"
x = 'X'
x = ['1', 3, "Ayush"]
x = {1, 2, 2, 4, "Hey", 4}
print(x)
x = (1, 2, 3)
x = {
    "name": "Ayush",
    "age": 29
}
print(x)


# /** ================*/


""" The numeric data type in Python represents the data that has a numeric value. A numeric value can be an integer, a floating number, or even a complex number. These values are defined as Python int , Python float , and Python complex classes in Python . 




** Integers: This value is represented by int class. It contains `positive or negative whole numbers` (without fractions or decimals). In Python, there is no limit to how long an integer value can be.
But when I tried to assign a variable large interger value it gave the following error
    ~ SyntaxError: Exceeds the limit (4300 digits) for integer string conversion: value has 13857 digits; use sys.set_int_max_str_digits() to increase the limit - Consider hexadecimal for huge integer literals to avoid decimal conversion limits.

** Float: This value is represented by the float class. It is a real number with a floating-point representation. It is specified by a decimal point. Optionally, the character e or E followed by a positive or negative integer may be appended to specify scientific notation.

** Complex Numbers – A complex number is represented by a complex class. It is specified as (real part) + (imaginary part)j . For example – 2+3j

"""


p = 5
print(type(p))

q = 16.258
print(type(q))

r = 2+3j
print(type(r))

