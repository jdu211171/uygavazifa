from typing import List


def plusOne(digits: List[int]) -> List[int]:
    return [int(i) for i in str(int(''.join(map(str, digits))) + 1)]


digits = [1,2,3]
print(plusOne(digits))
