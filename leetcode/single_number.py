from typing import List


def singleNumber(nums: List[int]) -> int:
    return min(nums, key=nums.count)


nums = [2,2,1]
print(singleNumber(nums))
