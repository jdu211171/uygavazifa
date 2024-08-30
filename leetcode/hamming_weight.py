def hammingWeight(n: int) -> int:
    return format(n, 'b').count('1')


print(hammingWeight(n = 11))
