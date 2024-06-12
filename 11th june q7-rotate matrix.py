nested_list = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
rotated_matrix = [list(row) for row in zip(*nested_list[::-1])]
print(rotated_matrix)
for row in rotated_matrix:
    print(row)
