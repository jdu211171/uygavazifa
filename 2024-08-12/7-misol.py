class Class:

    def __init__(self):
        self.string_data = ''

    def get_string(self):
        self.string_data = input('String kiriting: ')

    def update_string(self):
        lst = [letter for letter in self.string_data]
        lst[0], lst[-1] = lst[0].upper(), lst[-1].upper()
        self.string_data = ''.join(lst)


example = Class()
example.get_string()  # uzbekistan not well known yet full of wonders
example.update_string()
print(example.string_data)  # Uzbekistan not well known yet full of wonderS
