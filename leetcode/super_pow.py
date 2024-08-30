from typing import List


def superPow(a: int, b: List[int]) -> int:
    def my_pow(x: int, n: int) -> int:
        def helper(x, n) -> int:
            if x == 0: return 0
            if n == 0: return 1
            res = helper(x * x, n // 2)
            return x * res if n % 2 else res

        res = helper(x, abs(n))
        return int(res if n >= 0 else 1/res)
    return my_pow(a, int(''.join(map(str, b))))

print(superPow(a = 2147483647, b = [2,0,0]))

# print(int(''.join(['3'])))
