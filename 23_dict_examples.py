print("Length of dict--------------")

d ={'Name':'Steve', 'Age':30, 'Designation':'Programmer'}

# it count according to keys, no matter of nests it will count the outer keys 
print(len(d))


d = {
    "product1": {"name": "Laptop", "price": 800, "stock": 15},
    "product2": {"name": "Smartphone", "price": 500, "stock": 30},
    "product3": {"name": "Tablet", "price": 300, "stock": 25}
}


print(len(d.values()))


# count total items

d = {
    "person1": {"name": "John", "age": 25},
    "person2": {"name": "Alice", "age": 30},
    "person3": {"name": "Bob", "age": 22, "age2": 22}
}

count = 0
for x in d.values():
    count += len(x)

print(count)



print("Check if a Key Exists in a Python Dictionary--------------")


d = {'a': 1, 'b': 2, 'c': 3}

if "b" in d:            # or d.keys() 
    print("Yooo")
else:
    print("Nooo")


# check if "b" is none or not.
if d.get('b') == None:
  print("Not Present")
else:
  print("Present")

# what if key is not there
print(d.get("bbb"))     # ~ Returns none
print(d["bb"])          # errors ~ KeyError: 'bb'

