keys = ['a','b','c','d','e']
values = [1,2,3,4,5]  

my_dict = {k : v for (k, v) in zip(keys, values)}
print(my_dict)


dic=dict.fromkeys(range(5), True)
print(dic)

myDict = {x: x**2 for x in [1,2,3,4,5]}
print (myDict)


eachSqrDict = {y: y ** 2 for y in range(7, 13)}
print(eachSqrDict)


# Python code to demonstrate dictionary 
# comprehension using if.
newdict = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(newdict)


# nested dict comprehension
# given string
l="GFG"

# using dictionary comprehension
dic = {
    x: {y: x + y for y in l} for x in l
}

print(dic)