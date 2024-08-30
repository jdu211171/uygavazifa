# from typing import List


# def searchInsert(nums: List[int], target: int) -> int:
#     num = nums[len(nums)//2]
#     if num < target:
#         return searchInsert(nums[nums.index(num)+1:], target)
#     elif num >= target:
#         return searchInsert(nums[:nums.index(num)], target)
#     else:
#         return nums.index(num)
#     return 0


# nums, target = [1,3,5,6], 5
# print(searchInsert(nums, target))


# def binary_search
