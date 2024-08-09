
user = input('Enter a number: ')
dct = {k: user.count(k) for k in set(user)}
dct = dict(sorted(dct.items(), key=lambda x: x[0]))
for k, v in dct.items():
    print(f'{k} - {v}')
