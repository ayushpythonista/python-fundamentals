"""enumerate() function adds a counter to each item in a list or other iterable. It turns the iterable into something we can loop through, where each item comes with its number (starting from 0 by default). We can also turn it into a list of (number, item) pairs using list()."""

a = ["Ayush", "Anand", "Srivastava"]
for i, name in enumerate(a):
    print(f"Index {i}: {name}")


# how basically enumerate looks like
print(list(enumerate(a)))


# we can use custom start index also

for i, name in enumerate(a, 3)  :
    print(f"Index {i}: {name}")


for val in enumerate(a):
    print(val)

print("---- accessing the next element ----")
# accessing the next element
b = enumerate(a)
print(next(b))
print(next(b))
print(next(b))

"""Each time the next() is called, the internal pointer of the enumerate object moves to the next element, returning the corresponding tuple of index and value."""



print("""---------""")

# create a list of names
names = ['sravan', 'bobby', 'ojaswi', 'rohith', 'gnanesh']

# create a list of subjects
subjects = ['java', 'python', 'R', 'cpp', 'bigdata']

# create a list of marks
marks = [78, 100, 97, 89, 80]

# use enumerate() and zip() function
# to iterate the lists
# unpacking them
for i, (name, subject, mark) in enumerate(zip(names, subjects, marks)):
    print(i, name, subject, mark)

# for every index we have tuple formed using zip
print( list(enumerate(zip(names, subjects, marks))) )


