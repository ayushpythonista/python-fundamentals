"""
Python | Print unique rows in a given boolean matrix using Set with tuples
"""

# Given a binary matrix, print all unique rows of the given matrix. Order of row printing doesn’t matter. 


input1 = [
        [0, 1, 0, 0, 1],
        [1, 0, 1, 1, 0],
        [0, 1, 0, 0, 1],
        [1, 1, 1, 0, 0]
    ]


def problem_1(input_list):

    # convert list to tuple using map
    to_tuple = map(tuple, input_list)
    
    # then put in set
    set_a = set(to_tuple)
    
    # print all unique rows
    for row in list(set_a):
        print (row)


problem_1(input1)
