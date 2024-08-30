def atoi(word: str) -> int:
    word = word.strip()
    res = ''
    for char in word:
        if char.isalpha():
           break
        res += char

    return int(res)


print(atoi('   -42'))
print(atoi('1337c0d3'))
print(atoi('42'))


# ---------------------------------------------------------------------


from typing import List

def is_valid_square(matrix: List[List[int]], i: int, j: int, square: int) -> bool:
    if i + square > len(matrix) or j + square > len(matrix[0]):
        return False
    for x in range(i, i + square):
        for y in range(j, j + square):
            if matrix[x][y] == 0:
                return False
    return True

def find_max_square_area(matrix: List[List[int]]) -> int:
    max_area = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            square_size = 1
            while is_valid_square(matrix, i, j, square_size):
                max_area = max(max_area, square_size * square_size)
                square_size += 1

    return max_area


matrix = [
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]
]

print(find_max_square_area(matrix))
print(find_max_square_area([[1, 1],
                            [0, 1]]))
