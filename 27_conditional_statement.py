input_val = int(input("Enter your age: "))

if input_val < 18:
    print("Hey boi! You are not eligible to vote")
elif (input_val >= 18 and input_val <= 60):
    if input_val in range(25, 35):
        print("GO and Do your job")
    else:
        print("YOu can vote")
else:
    print("Relax you old")


print("I am young") if input_val < 25 else print("Need to do job")


if input_val > 30: print("You need to push hard")


num = 10
match num:
    case 0:
        print("It is zero")
    case 1:
        print("It is one")
    case 10 if num % 2 == 0:  # Match 10 only if it's even
        print("Matched 10 and it's even!")
    case 10 | 20 | 30:
        print(f"Matched: {num}")
    case _:
        print("It is another")


# with match we can also see if list matched the elements count or dict matching the structure
list_a = [100]

match list_a:
    case [x, y]:
        print(f"Two-element list: {x}, {y}")
    case [a, b, c]:
        print(f"Three-element list: {a}, {b}, {c}")
    case [z]:
        print("Woh" if z < 20 else "Wee")
    case _:
        print("Don't know")


person = {"name": "Alice", "age": 25}

match person:  
    # Dictionary with name and age keys
    case {"name": name, "age": age}:  
        print(f"Name: {name}, Age: {age}")
        
    # Dictionary with only name key    
    case {"name": name}:  
        print(f"Name: {name}")
    case _:
        print("Unknown format")


"""
The match-case statement, also known as pattern matching, is a feature introduced in Python 3.10. It provides a concise and expressive way to perform pattern matching on data structures, such as tuples, lists and classes. It allows you to match the value of an expression against a series of patterns and execute the corresponding block of code for the matched pattern.


The match-case statement is a more powerful and expressive construct compared to if-elif-else statements. While if-elif-else statements rely on boolean expressions, match-case statements can match patterns based on the structure and value of the data. Match-case statements provide a more structured and readable way to handle multiple conditions and perform different actions based on those conditions.
"""


