"""
Python Defaultdict is a container-like dictionaries present in the module collections.

It is a sub-class of the dictionary class that returns a dictionary-like object.
The difference from dictionary is, It provides a default value for the key that does not exist and never raises a KeyError.
"""


from collections import defaultdict

d = defaultdict(list)

# Add elements to the defaultdict and print it
d['fruits'].append('apple')
d['vegetables'].append('carrot')
print(d)

# No key error raised here and an empty list
# is printed
print(d['juices'])



"""How Does defaultdict Work?
When a defaultdict is created, you specify a factory function that will provide the default value for new keys. This factory function could be int, list, str, or any other callable object.

For example:

Using int: If you use int as the factory function, the default value will be 0 (since int() returns 0).
Using list: If you use list as the factory function, the default value will be an empty list ([]).
Using str: If you use str, the default value will be an empty string ('')."""

d = defaultdict(lambda: "Not Present in this")
d["a"] = 1
d["b"] = 2

print(d)
print(d["a"])
print(d["b"])
print(d["c"])



