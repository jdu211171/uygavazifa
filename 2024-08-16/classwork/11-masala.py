user = input("Gap kiriting: ")
user = user.split()
new_sentence = ' '.join([user[0][::-1], *user[1:-1], user[-1][::-1]])

print(new_sentence)
