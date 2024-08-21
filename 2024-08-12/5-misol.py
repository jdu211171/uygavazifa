class Class:

    def __init__(self, my_list: list):
        self.my_list = my_list

    def delete_first_item(self):
        return self.my_list.pop(0)


lst1 = Class([42, 'Ko\'k'])
lst2 = Class([342, 'Yashil'])
lst3 = Class([352, 'Qizil'])

lstlar = [lst2, lst1, lst3]

for lst in lstlar:
    print(lst.my_list)
    lst.delete_first_item()

for lst in lstlar:
    print(lst.my_list)
