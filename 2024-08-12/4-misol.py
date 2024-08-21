class Class:

    def __init__(self, my_list: list):
        self.my_list = my_list

    def delete_last_item(self):
        return self.my_list.pop()


lst1 = Class([494, 'Ko\'k'])
lst2 = Class([500, 'Yashil'])
lst3 = Class([489, 'Qizil'])

lstlar = [lst2, lst1, lst3]

for lst in lstlar:
    print(lst.my_list)
    lst.delete_last_item()

for lst in lstlar:
    print(lst.my_list)


