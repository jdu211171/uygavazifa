def strStr(haystack: str, needle: str) -> int:
    result = haystack.split(needle)
    return len(result[0]) if len(result) > 1 else -1


haystack, needle = "leetcode", "sad"
print(strStr(haystack, needle))
