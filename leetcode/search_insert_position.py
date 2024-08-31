from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    return nums.index(target) if target in nums else len([n for n in nums if n < target])


nums, target = [1,3,5,6], 5
print(searchInsert(nums, target))


# Neetcode
def search_insert(nums: List[int], target: int) -> int:
    L, R = 0, len(nums) - 1
    while L <= R:
        M = (L + R) // 2
        if target == nums[M]:
            return M
        if target > nums[M]:
            L = M + 1
        else:
            R = M - 1
    return L


nums, target = [1,3,5,6], 5
print(search_insert(nums, target))
