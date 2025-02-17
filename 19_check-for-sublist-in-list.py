test_list = [5, 6, 3, 8, 2, 1, 7, 1]

sublist = [8, 2, 1]


# loop through the index list
"""see in the list we need to find 3 elements so either we can loop till last but will not affect as we need to find 3 in this case so after last 3rd there will be no use to loop bcoz then only 2 and 1 will be present

next we will check after every index upto the lenght of subslist

say first loop gives 0 index
then slice will check 0 to sublist length that is 3 [0:3]

5, 6, 3 = 8, 2, 1

then index will be one so [1:3] which is wrong also increment the right index
[1 : 1+3] = [1:4] and so on
"""
is_present = False
for index in range(len(test_list) - len(sublist) + 1):
    if test_list[index : index + len(sublist)] == sublist:
        is_present = True
        break

print(f"{sublist} is present: ", is_present)

# now same logic using any - PREFFERED

is_sub = any(test_list[index : index + len(sublist)] == sublist 
                for index in range(len(test_list) - len(sublist) + 1)
            )
print(f"{sublist} is present: ", is_sub)


# OR : first convert list to str and then check using in 
# list to str
a = "".join(map(str, sublist)) in "".join(map(str, test_list))
print(a)





