from typing import List


def repeating_count(lst: List[int]) -> bool:
    tmp = {i: lst.count(i) for i in set(lst)}
    return True if len(set(tmp.values())) > 1 else False

arr =  [1,2,3]
print(repeating_count(arr))
