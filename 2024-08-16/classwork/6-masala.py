def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a

user = int(input("n = "))
lst = [fibonacci(i) for i in range(user)]
index = 0
for i in range(1, user + 1):
    print(' ' * (user - i), end='')
    for j in range(i):
        if index < len(lst):
            print(lst[index], end=' ')
            index += 1
    print()
