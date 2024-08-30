def my_pow(x: float, n: int) -> float:
    def helper(x, n) -> float:
        if x == 0: return 0
        if n == 0: return 1
        res = helper(x, n // 2)
        res *= res
        return x * res if n % 2 else res

    res = helper(x, abs(n))
    return res if n >= 0 else 1/res


print(my_pow(x = 2.00000, n = 10) == 1024.00000)
