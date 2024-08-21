with open('text.txt', 'r') as file:
    text = file.read()
    text = text.split()

even_words = []
odd_words = []
for word in text:
    if len(word) % 2 == 0:
        even_words.append(word)
    else:
        odd_words.append(word)

with open('even_words.txt', 'w') as file:
    for word in even_words:
        file.write(word + '\n')

with open('odd_words.txt', 'w') as file:
    for word in odd_words:
        file.write(word + '\n')
