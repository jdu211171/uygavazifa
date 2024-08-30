from typing import List


def is_valid_square(matrix: List[List[int]], i: int, j: int, square: int) -> bool:
    if len(matrix[0]) != len(matrix):
        return False
    valid = True
    for count in range(square):
        valid = bool(matrix[i][j] and matrix[i][j+count] and matrix[i + count][j] and matrix[i+count][j+count])
        if not valid:
            return False
    return valid


matrix = [
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]
]



area = 0
m = 2
z = 3
k = 0
for i in range(len(matrix)):
    # for j in range(i):
        # print(f'matrix[{i}][:{m}]')
    # z += i
    for j in range(len(matrix[0])):
        print(f'matrix[{z}][:{m}]')

    # print(matrix[i][:m])


    # new_arr = []
    # new_arr.append(matrix[i][:m])
    # some = is_valid_square(new_arr, 0, 0, 3)
