# concatenation

s = "Ayush" + " " + "Anand"
print(s)


"""Using String Formatting (% operator)
Using the provides for string formatting allows you to insert variables into a string in a specified format. It provides a way to dynamically insert values into strings while maintaining readability and flexibility."""

s = "The number is %d"
# %d for int format specifier
num = 42

result = s % num

print(result)



# str.format
strVal = "{} is the name of {}"
res = strVal.format("Ayush", "DEV")

print(res)

res = "{1} is the college of {0}".format("Ayush", "SRMU")
print(res)



