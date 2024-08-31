def lengthOfLastWord(s: str) -> int:
    return len(s.split()[-1])



s = "   fly me   to   the moon  "
print(lengthOfLastWord(s))
