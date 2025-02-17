"""File handling refers to the process of performing operations on a file such as creating, opening, reading, writing and closing it, through a programming interface. It involves managing the data flow between the program and the file system on the storage device, ensuring that data is handled safely and efficiently."""

# with open('ayush.txt', 'r') as file:  # r ~ Read-only mode.	
# When opening a file, we must specify the mode we want to which specifies what we want to do with the file.
# File must exist; otherwise, it raises an error.


file = open("INFO/NOTES", "r")
content = file.read()
print(content)
file.close()


# """Reading a File in Binary Mode (rb)"""
file = open("INFO/NOTES", "rb")
content = file.read()
print(content)
file.close()


# it will also create the file if not exists
file = open("geeks.txt", "w")

# The below will replace the previous contents
file.write("Hello, World!")
file.write("Hello, Ayush!")
file.close()


"""Writing to a File in Append Mode (a)"""
# It is done using file.write() which adds the specified string to the end of the file without erasing its existing content.
file = open('geeks.txt', 'a')
file.write("\nThis will add this line")
file.close()


# Closing a file is essential to ensure that all resources used by the file are properly released. file.close() method closes the file and ensures that any changes made to the file are saved.


"""Using with Statement

with statement is used for resource management. It ensures that file is properly closed after its suite finishes, even if an exception is raised. with open() as method automatically handles closing the file once the block of code is exited, even if an error occurs. This reduces the risk of file corruption and resource leakage.
"""

with open("geeks.txt", "r") as file:
    content = file.read()
    print(content)



# Handling Exceptions When Closing a File

try:
    file = open("geeks.txt", "r")
    content = file.read()
    print(content)
finally:
    file.close()


"""
 open()  : Opens a file and returns a file object. 
 read()  : Reads data from a file. 
 write()  : Writes data to a file. 
 close()  : Closes the file, releasing its resources. 
"""


