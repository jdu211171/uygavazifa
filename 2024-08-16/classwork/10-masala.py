def print_numbers(num: int):
    if num % 2 == 0:
        for i in range(num, 0, -1):
            print('+'.join([str(j) for j in range(1, i + 1)]) + f'={sum([j for j in range(1, i + 1)])}')
    else:
        for i in range(1, num + 1):
            print('+'.join([str(j) for j in range(1, i + 1)]) + f'={sum([j for j in range(1, i + 1)])}')

print_numbers(6)
