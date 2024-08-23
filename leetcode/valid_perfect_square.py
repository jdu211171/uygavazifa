# O(log_n) time complexity
# Binary search solution
def isPerfectSquare(num: int) -> bool:
    l, r = 1, num
    while l <= r:
        mid = l + (r - l) // 2
        if mid * mid > num:
            r = mid - 1
        elif mid * mid < num:
            l = mid + 1
        else:
            return True
    return False


print(isPerfectSquare(14))
