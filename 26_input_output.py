# Single variable
s = "Bob"
print(s)

# Multiple Variables
s = "Alice"
age = 25
city = "New York"
print(s, age, city)

amount = 150.75
print("Amount: ${:.2f}".format(amount))


print("Ayush", end="@")
print("AksTechies")


print("Apple", "Mango", "Banana", sep=", ")


"""INPUT"""
# Input takes string ~ we can type cast it according to the need

name = input("Enter your name: ")

print(name)

# Take Multiple Input in Python

# taking two inputs at a time
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
 
# taking three inputs at a time
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)


"""For more control, you can use the sys.stdout to write directly to the standard output stream, which is useful for more complex console applications."""
import sys
sys.stdout.write("This is some output data.\n")