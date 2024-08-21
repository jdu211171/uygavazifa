from collections import Counter
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]):
        missing_num = {num for num in range(min(nums), max(nums) + 1)}.difference(set(nums))
        return missing_num.pop() if missing_num else None


nums = [3,0,1]
solve = Solution()
print(solve.missingNumber(nums))
# print(*{1, 2, 3, 4}.difference({1, 2, 4}))
