# Brute Force: O(n^2)
def brute_force(nums: list):
    max_sum = nums[0]

    for i in range(len(nums)):

        cur_sum = 0
        for j in range(i, len(nums)):
            cur_sum += nums[j]
            max_sum = max(max_sum)

    return max_sum


# Kadane's Algorithm: O(n)
def kadanes(nums: list):
    max_sum = nums[0]
    cur_sum = 0

    for n in nums:
        cur_sum = max(cur_sum + n, n)
        max_sum = max(max_sum, cur_sum)

    return max_sum


# Sliding window variation of Kadane's: O(n)
def sliding_window(nums: list):
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
