from collections import Counter
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]):
        n = len(nums)
        return n * (n+1) // 2 - sum(nums)


nums = [0,1]
solve = Solution()
print(solve.missingNumber(nums))
