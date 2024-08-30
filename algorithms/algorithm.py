from re import X
from typing import List


# Brute Force: O(n^2)
def brute_force(nums: List[int]) -> int:
    max_sum = nums[0]

    for i in range(len(nums)):

        cur_sum = 0
        for j in range(i, len(nums)):
            cur_sum += nums[j]
            max_sum = max(max_sum, cur_sum)

    return max_sum


# Kadane's Algorithm: O(n)
def kadanes(nums: List[int]) -> int:
    max_sum = nums[0]
    cur_sum = 0

    for n in nums:
        cur_sum = max(cur_sum + n, n)
        max_sum = max(max_sum, cur_sum)

    return max_sum


# Sliding window variation of Kadane's: O(n)
def sliding_window(nums: List[int]) -> List[int]:
    max_sum = nums[0]
    cur_sum = 0
    left_index, right_index = 0, 0
    L = 0

    for R in range(len(nums)):

        if cur_sum < 0:
            cur_sum = 0
            L = R

        cur_sum += nums[R]
        if cur_sum > max_sum:
            max_sum = cur_sum
            left_index, right_index = L, R

    return [left_index, right_index]


# Binary search algorithm: O(logn)
def binary_search(
    lst: List[int],
    low: int,   # 0
    high: int,  # len(lst) - 1
    num: int) -> int:
    if high >= low:
        mid = (high + low) // 2
        if lst[mid] == num:
            return lst.index(num)
        elif lst[mid] > num:
            return binary_search(lst, low, mid - 1, num)
        else:
            return binary_search(lst, mid + 1, high, num)
    else:
        return -1


arr = [1,3,5,6]
x = 2
print(binary_search(arr, 0, len(arr)-1, x))
