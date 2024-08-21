def reverseWords(s: str) -> str:
    return ' '.join(map(lambda x: x[::-1], s.split()))

s = "Let's take LeetCode contest"
print(reverseWords(s))
