s = "Ayush"

s = s[::-1]

print(s)


a = ["apple", "banana", "cherry", "date"]
list_a = []

for s in a:
    list_a.append(s[::-1])

print(list_a)


# by list comprehension
list_a = [x[::-1] for x in a]
print(list_a)


# map alsp
## bcoz lambda performs operation on each element using function
list_a = list(map(lambda x: x[::-1], a))
print(list_a)
