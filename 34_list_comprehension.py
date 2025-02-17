a = [1, 2, 3, 4]

a = [ x ** 2 for x in a]

print(a)


# [expression for item in iterable if condition]

import math
# same using for loop
a = [1, 2, 3, 4] 
a2 = []
for x in a:
    a2.append(int(math.pow(x, 2)))
print(a2)


a = [1, 2, 3, 4, 5]
a.extend(list(range(6, 17)))
val_a = [x for x in a if x % 2 == 0]
print(val_a)


# using with if else then if needs to be first
val_a = [str(x) + "-Even" if x % 2 == 0 else str(x) + "-Odd" for x in a]
print(val_a)

# nested
val_a = [y if y % 2 == 0 else y ** 2 if y < 10 else y / 2 for y in a]
print(val_a)


"""Using nested loops
List comprehension can also be used with nested loops. Here, we generate a list of coordinate pairs for a simple 3x3 grid."""


new_list = [(x, y) for x in range(3) for y in range(3)]
print(new_list)

# equivalent
new_list_2 = []
for x in range(3):
    for y in range(3):
        new_list_2.append((x, y))
print(new_list)


"""Flattening a list of lists
Suppose we have a list of lists and we want to convert it into a single list.

in case of multiple loops the first loops start from left"""

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

new_mat = [val for row in mat for val in row]

print(new_mat)

new_mat_2 = []
for loop1 in mat:
    for loop2 in loop1:
        new_mat_2.append(loop2)
print(new_mat_2)


# creating a matrix

new_mat_list = []

for mat_1 in range(1, 3):
    mat_list_2 = []
    for mat_2 in range(11, 14):
        mat_list_2.append([mat_1, mat_2])
    new_mat_list.append(mat_list_2)

print(new_mat_list)


matrix = []
for i in range(5):
    matrix.append([])
    for j in range(5):
        matrix[i].append(j)

print(matrix)


new_matrix = [[aj for aj in range(5)] for _ in range(5)]
print(new_matrix)


"""make an internal list and then multiply it"""

new_matrix = [[aj for aj in range(5)]] * 5
print(new_matrix)

matrix_01 = [[]] * 5
for ja in range(5):
    matrix_01[ja].append(ja)

print(matrix_01)


matrix_02 = []
for ja in range(5):
    matrix_02.append(ja)
matrix_02 = [matrix_02] * 5
print(matrix_02)


matrix_03 = [[j2 for j2 in range(5)]] * 5
print(matrix_03)



matrix = [["apple", "banana", "cherry"],
          ["date", "fig", "grape"],
          ["kiwi", "lemon", "mango"]]

# capitalize
new_matrix = []
for var_1 in matrix:
    mat_1 = map(lambda s : s.upper(), var_1)
    list_mat_1 = list(mat_1)
    new_matrix.append(list_mat_1)
print(new_matrix)

new_matrix_compre = [list(map(lambda s : s.upper(), var_1)) for var_1 in matrix]
print(new_matrix_compre)

 
modified_matrix = []
for row in matrix:
    modified_row = []
    for fruit in row:
        modified_row.append(fruit.capitalize())
    modified_matrix.append(modified_row)
print(modified_matrix)


# actually this is flattening so loop starts from left
modified_matrix_compre = [fruit_2.capitalize() for row_2 in matrix for fruit_2 in row_2 ]
print(modified_matrix_compre)


# but to create matrix
modified_matrix_compre_2 = [[fruit_2.capitalize() for fruit_2 in row_2] for row_2 in matrix]
print(modified_matrix_compre_2)





