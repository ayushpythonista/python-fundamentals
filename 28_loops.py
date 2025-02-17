"""
Loops in Python are used to repeat actions efficiently. The main types are For loops (counting through items) and While loops (based on conditions). Additionally, Nested Loops allow looping within loops for more complex tasks. While all the ways provide similar basic functionality, they differ in their syntax and condition-checking time. I
"""

count  = 0

while count < 5:
    print("counted till", count, sep=": ")
    count += 1


# while with else block


testing_time = 3

while testing_time < 5:
    print(f"Tested {testing_time}")
    testing_time += 1
else:                   # else block will execute after above condition fails
    print("Already Tested")


for i in range(4):
    print(i, " FOR")


for z in range(4):
    print(z, " FOR LESE")
else:
    print("FOR ELSE")


for i in range(1, 6):
    for j in range(1, i+ 1):
        print(j, end=" ")
    print()

"""The continue statement in Python returns the control to the beginning of the loop."""        
for letter in "Ayush Anand Srivastava":
    if letter == 'u' or letter == 'a':
        continue        # what will happen that loop will not go belo from here if condition satisfies but it will start the next loop
    print(letter)
    

"""The break statement in Python brings control out of the loop."""

# break breaks the loop 

for i in range(10):
    print(i)
    if i == 6:
        break

for i in range(10): {
    print("i is: ", i)
}
    

# pass ~ when we dont want to write a code block but still need a condition 
num = 5
for n in range(num):
    pass        # see here we used the loop but we don't want to do anything inside it

print(n)

# manual loop
fruits = ["apple", "orange", "banana"]
fruits_itr = iter(fruits)


while True:
    try:
        fruit = next(fruits_itr)
        print(fruit)
    except StopIteration:
        break

def test():
    print("LOL")
