from collections import Counter


x = Counter (a = 2, x = 3, b = 3, z = 1, y = 5, c = 0, d = -3)

counter2 = Counter(a=1, b=2, c=3)
counter1 = Counter(a=0, b=5)
difference = counter2 - counter1
print(difference)  # Output: Counter({'a': 2})
