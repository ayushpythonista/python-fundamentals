"""
A Python dictionary is a data structure that stores the value in key: value pairs. Values in a dictionary can be of any data type and can be duplicated, whereas keys can't be repeated and must be immutable.

"""

d = {
    1: "Ayush",
    2: "Abhinav",
    3: "Anand",
    4: "Anita",
    "Surname": "Srivastava",
    ('a', 'b') : ['A', 'B']
}           # using list as key will give error
# If we have same keys then second one will be printed

print(d)
print(type(d))



# create dictionary using dict() constructor

d2 = dict(a = "A", b = "B", c = "C")
print(d2)


"""
From Python 3.7 Version onward, Python dictionary are Ordered.
 - Dictionary keys are case sensitive: the same name but different cases of Key will be treated distinctly.
 - Keys must be immutable: This means keys can be strings, numbers, or tuples but not lists.
 - Keys must be unique: Duplicate keys are not allowed and any duplicate key will overwrite the previous value.
 - Dictionary internally uses Hashing. Hence, operations like search, insert, delete can be performed in Constant Time
"""


# Accessing

print(d[2])

print(d.get("Surname"))


# adding key
d["Place"] = "Lucknow"
print(d)


# updating
d["Place"] = "Lucknow, UP"
print(d)


"""
Removing Dictionary Items
We can remove items from dictionary using the following methods:

del: Removes an item by key.
pop(): Removes an item by key and returns its value.
clear(): Empties the dictionary.
popitem(): Removes and returns the last key-value pair.

"""

d = {1: 'Geeks', 2: 'For', 3: 'Geeks', 'age':22}

# Using del to remove an item
del d["age"]
print(d)


# use this or del to remove by key
val = d.pop(3)
print(val)          # val will return d[3] value and remove it from dict
print(d)


# use this to remove last key value
key, val = d.popitem()          #  Using popitem to removes and returns the last key-value pair.
print(f"Key: {key}, Value: {val}")
print(d)

# Clear all items from the dictionary
d.clear()
print(d)




"""Iterating through dict"""


d = {
    1: "Ayush",
    2: "Abhinav",
    3: "Anand",
    4: "Anita",
    "Surname": "Srivastava",
    ('a', 'b') : ['A', 'B']
} 

# It print keys
print("---It print keys--")
for key in d:
    print(key)


# It print values
print("---It print values--")
for value in d.values():
    print(value)


# need both key value
for key, value in d.items():
    print(f"Key is {key} and value is {value}")


# nested dict
stud = {
    "name": "Ayush",
    "age": 29,
    "subject": {
        "stream": "ME",
        "year": 4
    }
}
print(stud)

stud["subject"]["session"] = "2023-24"
print(stud)

stud["subject"]["stream"] = "Mechanical"
print(stud)

print(stud["subject"]["year"])