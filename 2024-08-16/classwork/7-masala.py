def show_like_users(lst: list):
    if len(lst) == 0:
        print('no one likes this')
    elif len(lst) == 1:
        print(f'{lst[0]} likes this')
    elif len(lst) >= 2:
        print(f'{', '.join(lst[:-1])} and {lst[-1]} like this')

show_like_users(['Mike', 'Anna', 'John', 'Alex'])
