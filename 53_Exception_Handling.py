"""
Python Exception Handling handles errors that occur during the execution of a program. Exception handling allows to respond to the error, instead of crashing the running program. It enables you to catch and manage errors, making your code more robust and user-friendly.
"""


"""NOTE: raise immediately stops further code execution and propagates the exception up the call stack unless it is caught by another try-except block."""

n = 10

try : 
    n / 0
except ZeroDivisionError:
    print("Heyy, by zero?")
except ValueError:
    raise ValueError("Hey fool diving by zero?")
except Exception as e:
    raise

"""try, except, else and finally Blocks
 - try Block: try block lets us test a block of code for errors. Python will “try” to execute the code in this block. If an exception occurs, execution will immediately jump to the except block.
 - except Block: except block enables us to handle the error or exception. If the code inside the try block throws an error, Python jumps to the except block and executes it. We can handle specific exceptions or use a general except to catch all exceptions.
 - else Block: else block is optional and if included, must follow all except blocks. The else block runs only if no exceptions are raised in the try block. This is useful for code that should execute if the try block succeeds.
 - finally Block: finally block always runs, regardless of whether an exception occurred or not. It is typically used for cleanup operations (closing files, releasing resources)."""

print("---=--=-----")
try:
    n = 0
    res = 100 / n
    
except ZeroDivisionError:
    print("You can't divide by zero!")
    
except ValueError:
    print("Enter a valid number!")
    
else:
    print("Result is", res)
    
finally:
    print("Execution complete.")


"""
Performance overhead: Exception handling can be slower than using conditional statements to check for errors, as the interpreter has to perform additional work to catch and handle the exception.
"""



# CUSTOM EXCEPTION

"""
 - Define a New Exception Class: Create a new class that inherits from Exception or any of its subclasses.
 - Raise the Exception: Use the raise statement to raise the user-defined exception when a specific condition occurs.
 - Handle the Exception: Use try-except blocks to handle the user-defined exception.
"""

# we need inherit here else error is ~ TypeError: catching classes that do not inherit from BaseException is not allowed
# here I tried multiple exception inheritance and everyone was working because each of them somehow have inherited to BaseException
class InvalidAgeError(Exception):
    def __init__(self, age, msg="Age must be between 0 and 120"):
        self.age = age
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.age} -> {self.msg}'


# Step 2: Use the custom exception in your code
def set_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    else:
        print(f"Age set to: {age}")

try:
    set_age(150)  # This will raise the custom exception
except InvalidAgeError as e:
    print(e)


# NetworkError has base RuntimeError and not Exception
class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg     #args is build in BaseException and is tuple
        self.my_arg = arg

try:
    raise Networkerror("Error")

except Networkerror as e:
    print(e.args)
    print(e.my_arg)