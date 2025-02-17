# A string is a sequence of characters. Python treats anything inside quotes as a string. This includes letters, numbers, and symbols. Python has no character data type so single character is a string of length 1.

# Like in c++ the character is 'C' or 'c' with sigle quotes but in python everything is string no characters

s = "Ayush"

print(s[1])

s = s + s[0]

print(s)

# basically string is the array of characters so we can do using index


# Multiline strings ~ If we need a string to span multiple lines then we can use triple quotes (”’ or “””).
# Inside this everything is considered even the space and newline
s = """So!          
Hey booi
This is ayush
Enjoy"""
print(s)

# Accessing characters ~ using indexes

my_name = "AyushAnandSrivastava"

print(my_name[1])
print(my_name[7])

# Note: Accessing an index out of range will cause an IndexError. Only integers are allowed as indices and using a float or other types will result in a TypeError.


# NEGATIVE INDEXING
# Python allows negative address references to access characters from back of the String, e.g. -1 refers to the last character, -2 refers to the second last character, and so on. 
# like my_name[-1] will give the last while [0] will give first
print(my_name[-1])
print(my_name[-4])

# SLICING
# Slicing is a way to extract portion of a string by specifying the start and end indexes. The syntax for slicing is string[start:end], where start starting index and end is stopping index (excluded).

# means if I mentioned from 1 to 5 to 1st index will be included but 5th will not be
print(my_name[1:5])
print(my_name[:5])      # this will print index from 0 to 4th index
print(my_name[2:])      # this from 2nd index till end

# Reverse a string
print(my_name[::-1])


# String Immutability
# Strings in Python are immutable. This means that they cannot be changed after they are created. If we need to manipulate strings then we can use methods like concatenation, slicing, or formatting to create new strings based on the original.

# so after changing string we are creating a new string and it is not modifying the old one

s ="I am a python"
print(s)

s = s + " Engineer"         #basically this will create new
print(s)

# Deleting a String
## In Python, it is not possible to delete individual characters from a string since strings are immutable. However, we can delete an entire string variable using the del keyword.
del s
# print(s)        # NameError: name 's' is not defined


# Updating a String
## Since strings are immutable so we cannot update an existing string but create a new string

s = "hello world world"

s1 = "H" + s[1:]        # so this will take string for 1st index and join it to H
print(s1)

# let's replace ~ (what needs to be replaced, with what) ~ it replaces all occurences
## replace(old, new) replaces all occurrences of a specified substring with another.
s2 = s1.replace("world", "Ayush")
print(s2)


"""Common String Methods"""

# Find length using len
s2Len = len(s2)
print(s2Len)

# to upper and lower case
print(s2.upper())
print(s2.lower())


# strip() removes leading and trailing whitespace from the string

letStrip = "          ddd     "
print(letStrip)
print(letStrip.strip())


my_str = """

Hey Bois

"""
print(my_str)
print(my_str.strip())



s = "hellO ayUsh"
# title to capitalize first case for each words and small all
print(s.title())

# swaps the case like small to caps and caps to small
print(s.swapcase())


# capitalize the first word others small
print(s.capitalize())



# STRINGS OPERATOR

## we can concatenate string using `+` and repeat string using `*`

s = "Test"

s = s + "-" + s
print(s)

print(s*3)


"""
Formatting Strings
Python provides several ways to include variables inside strings.
"""
name = "Ayush"
age = 29

# f-string
print(f"My name is {name} and my age is {age}")

# .format()
print("So the age is {} of {}".format(age, name))



# The `in` keyword checks if a particular substring is present in a string.
print('s' in name)
print('z' in name)
print("yu" in name)


