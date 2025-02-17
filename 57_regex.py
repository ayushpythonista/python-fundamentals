"""

A Regular Expression or RegEx is a special sequence of characters that uses a search pattern to find a string or set of strings.

It can detect the presence or absence of a text by matching it with a particular pattern and also can split a pattern into one or more sub-patterns.

"""

import re


#  Check whether a string starts and ends with the same character or not (using Regular Expression)

regex = r'^[a-z]$|^([a-z]).*\1$'

def check(string):
    # pass the regular expression 
    # and the string in the search() method 
    if(re.search(regex, string)):  
        print("Valid")  
    else:  
        print("Invalid") 

sample1 = "abba"
sample2 = "a"
sample3 = "abcd"

check(sample1)
check(sample2)
check(sample3)