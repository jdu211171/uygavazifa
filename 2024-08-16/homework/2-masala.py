from typing import List


def findNumbers(nums: List[int]) -> int:
    return len(list(filter(lambda x: len(str(x)) % 2 == 0, nums)))


print(findNumbers([12, 345, 2, 6, 7896]))
