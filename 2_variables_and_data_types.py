# Python variables are dynamically typed, meaning the same variable can hold different types of values during execution.

x: int = 10
print(x)

x = "Hello"
print(x)

a = b = c = 100
print(a, b, c)


var1, var2, var3 = 155, 12.5, "Ayush"
print(var1, var2, var3)

# Casting refers to the process of converting the value of one data type into another. Python provides several built-in functions to facilitate casting, including int(), float() and str() among others.

var4 = 20
var5 = float(var4)

print(var5)
print(type(var5))

var6 = int(23.417)
print(var6)

var7 = str(var6)
print(var7)
print(type(var7))

# SCOPE OF VARIABLES
## Local scope
### Variables defined inside the function are local to that function

def func1():
    func_var: int = 177
    print(func_var)

func1()     
# print(func_var) ~ # NameError: name 'func_var' is not defined
# python interpreter executes line by line so all the above code will be executed until the error occurs

print("Goooooo")

## Global Variables
### Variables defined outside any function are global and can be accessed inside functions using the global keyword.

var8 = 754

def func2():
    global var8
    print("var8: ", var8)
    var8 = 414
    print("var8 changed to: ", var8)

func2()
print(var8)     # since inside function we have said global to var8 hence var8 value is changed here also

# /** -----=========-------------------------  **/

# Object Reference in Python
x = 5

"""When x = 5 is executed, Python creates an object to represent the value 5 and makes x reference this object.

x -> 5

Now, if we assign another variable y to the variable x.

"""

y = x

"""
x -> 5 <- y

Python encounters the first statement, it creates an object for the value 5 and makes x reference it. The second statement creates y and references the same object as x, not x itself. This is called a Shared Reference, where multiple variables reference the same object.

Now, if we write

"""

x = "Ayush"

"""

Python creates a new object for the value "Ayush" and makes x reference this new object.

but The variable y remains unchanged, still referencing the original object 5.

x -> Ayush
5 <- y

If we now assign a new value to y:

"""

y = "Abhinav"


"""

x -> Ayush
5 -> garbage
y -> Abhinav

- Python creates yet another object for "Abhinav" and updates y to reference it.
- The original object 5 no longer has any references and becomes eligible for garbage collection.

- Python variables hold references to objects, not the actual objects themselves.
- Reassigning a variable does not affect other variables referencing the same object unless explicitly updated.

"""

# /** -----=========-------------------------  **/

# Delete a variable using del keyword
## We can remove a variable from the namespace using the del keyword. This effectively deletes the variable and frees up the memory it was using.

x1 = 666

print (x1)

del x1

# print(x1)     # ~ NameError: name 'x1' is not defined


# PROGRAM SWAP 2 numbers
a, b = 5, 10
print(a, b)

a, b = b, a
print(a, b)

# PROGRAM counting characters in strings
my_name = "Ayush"
print(len(my_name))

