def mySqrt(x: int) -> int:
    L, R = 0, x
    res = 0

    while L <= R:
        M = L + (R - L) // 2
        if M ** 2 > x:
            R = M - 1
        elif M ** 2 < x:
            L = M + 1
            res = M
        else:
            return M

    return res


x = 8
print(mySqrt(x))
