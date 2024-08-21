from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        L = 1
        for R in range(1, len(nums)):
            if nums[R] != nums[R - 1]:
                nums[L] = nums[R]
                L += 1
        return L


lst = [1, 2, 2, 3, 3, 5, 5]
order = Solution()
print(order.removeDuplicates(lst))
print(lst)
