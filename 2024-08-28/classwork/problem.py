from typing import List
from typing_extensions import Counter


def frequencySort(nums: List[int]) -> List[int]:
    freq = Counter(nums)
    nums.sort(key=lambda x: (freq[x], -x))
    return nums


nums = [1,1,2,2,2,3]
# print(frequencySort(nums))


def sortSentence(s: str) -> str:
    return ''.join([i[:-1]+' ' for i in sorted(s.split(), key=lambda x: x[-1])]).strip()


s = "is2 sentence4 This1 a3"
# print(sortSentence(s))


def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
    arr = []
    for i in arr2:
        for j in range(arr1.count(i)):
            arr.append(i)
    arr += sorted(list(set(arr1).difference(arr)))
    return arr


arr1, arr2  = [2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]
print(relativeSortArray(arr1, arr2))
