"""
The OS module in Python provides functions for interacting with the operating system. OS comes under Python’s standard utility modules. This module provides a portable way of using operating system-dependent functionality.

The *os* and *os.path* modules include many functions to interact with the file system.

Python-OS-Module Functions

 - Handling the Current Working Directory
 - Creating a Directory
 - Listing out Files and Directories with Python
 - Deleting Directory or Files using Python
"""


import os 
cwd = os.getcwd() 
print("Current working directory:", cwd) 


os.chdir('../') 
print("Now dir is: ", os.getcwd())

os.chdir("fundamentals")
print("dir changed to: ", os.getcwd())

if not os.path.exists("MyTestCreatedDir"):
    os.mkdir("MyTestCreatedDir")
else:
    print("Directory already exists")


"""Joining two paths using"""
directory = "Ayush"
parent_dir = "D:/Pycharm projects/"
path = os.path.join(parent_dir, directory)
print(path)
