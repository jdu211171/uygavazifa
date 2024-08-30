from typing import List


def remove_element(nums: List[int], val: int) -> int:
    if not nums:
        return 0

    L = 0
    for R in range(0, len(nums)):
        if nums[R] != val:
            nums[L] = nums[R]
            L += 1
    return L

nums = [3,2,2,3]
print(remove_element(nums, 3))
