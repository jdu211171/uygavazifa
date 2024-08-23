def isValid(s: str) -> bool:
    dct = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for char in s:
        if char in dct:
            stack.append(char)
        elif not stack or dct[stack.pop()] != char:
            return False
    return not stack


s = "()[]{}"
print(isValid(s))
