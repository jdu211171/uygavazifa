def addBinary(a: str, b: str) -> str:
    result = ""
    carry = 0
    i, j = len(a) - 1, len(b) - 1
    while i >= 0 or j >= 0:
        sum = carry
        if i >= 0:
            sum += int(a[i])
            i -= 1
        if j >= 0:
            sum += int(b[j])
            j -= 1
        result += str(sum % 2)
        carry = sum // 2
    if carry:
        result += str(carry)
    return result[::-1]


a, b = "11", "1"
print(addBinary(a, b))
