
def zero_counter(num: str) -> int:
    i = 0
    count = 0
    while len(num) > i and num[i] == '0':
        count += 1
        i += 1
    return count


print(zero_counter('000'))
