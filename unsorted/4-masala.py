
with open('hello.txt') as file:
    rows = file.read()

rows = rows.replace('\n', '').replace(' ', '')
print(rows)

left_hand = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b', '!', '1', '@', '2', '#', '3', '$', '4', '%', '5']
left_hand_count = 0
right_hand = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm', '^', '6', '&', '7', '*', '8', '9', '0', '(', ')', '-', '_', '+', '=']
right_hand_count = 0

for i in rows:
    if i.lower() in left_hand:
        left_hand_count += 1
    elif i.lower() in right_hand:
        right_hand_count += 1

print('Chap qo\'lda yozilgan harflar soni: ', left_hand_count)
print('O\'ng qo\'lda yozilgan harflar soni: ', right_hand_count)
