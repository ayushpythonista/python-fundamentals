"""In Python, functions are treated as first-class objects. First-class objects in a language are handled uniformly throughout. They may be stored in data structures, passed as arguments, or used in control structures. A programming language is said to support first-class functions if it treats functions as first-class objects. Python supports the concept of First Class functions.

Properties of first-class functions:

A function is an instance of the Object type.
You can store the function in a variable.
You can pass the function as a parameter to another function.
You can return the function from a function.
You can store them in data structures such as hash tables, lists, etc."""

"""Inner functions
A function defined inside another function is known as an inner function or a nested function. Nested functions can access variables of the enclosing scope. Inner functions are used so that they can be protected from everything happening outside the function. This process is also known as Encapsulation."""

def outerFunction(text): 
    def innerFunction(): 
        print(text) 
    innerFunction() 


outerFunction('Hey!')


"""In the above example, innerFunction() has been defined inside outerFunction(), making it an inner function. To call innerFunction(), we must first call outerFunction(). The outerFunction() will then go ahead and call innerFunction() as it has been defined inside it."""


"""Scope of variable in nested function"""
def f1():
    s = 'I love GeeksforGeeks'      # this will be considered as global for f2
    
    def f2():
        s = 'Me too'                 # this will be considered as local for f2
        print(s)
        
    f2()
    print(s)

# Driver's code
f1()

# ------------- 

# here the value of both s will change because we are not assigning the new value instead changing the value and python store value as reference
def f1():
    s = ['I love GeeksforGeeks']
    
    def f2():
        s[0] = 'Me too'
        print(s)
        
    f2()
    print(s)

# Driver's code
f1()


"""Using nonlocal keyword: with this we can access the outer func var but global is different it is used to access the global means the outest defined variable

The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.
"""
def f1():
    s = 'I love GeeksforGeeks'
    y = "Ayush"
    def f2():
        nonlocal s
        global y
        s = 'Me too'
        y = "OK"
        print(s, y)         
        
    f2()
    print(s, y)         # s will be changed here also but not y 

# Driver's code
f1()


"""---------"""
def f1():
    f1.s = 'I love GeeksforGeeks'
    
    def f2():
        f1.s = 'Me too'
        print(f1.s)
        
    f2()
    print(f1.s)

# Driver's code
f1()


"""closure is a nested function that helps us access the outer function's variables even after the outer function is closed."""

def outerFunction(text): 
    text = text 
  
    def innerFunction(): 
        print(text) 
  
    return innerFunction

myFunction = outerFunction('Hey !') 
myFunction()

"""
DIFFERENCE

1 ---
 - outerFunction('Hey !') executes and returns innerFunction without calling it.
 - myFunction now holds a reference to innerFunction, which can be called later.
 - myFunction() is then explicitly called, printing "Hey !".

2 --- 
 - outerFunction('Hey !') executes and calls innerFunction() before returning.
 - Since innerFunction() is called inside outerFunction, "Hey !" is printed immediately.
 - The return value of outerFunction is whatever innerFunction() returns.
 - Since innerFunction() does not return anything explicitly, it returns None, meaning myFunction is None.

Means in closure the inner function is not called it just holds reference, so that we can call later
"""