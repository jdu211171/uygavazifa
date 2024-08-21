class Soldier:

    def __init__(self, name: str, age: int, sex: str, weight: int, height: int):
        self.name = name
        self.age = age
        self.sex = sex
        self.weight = weight
        self.height = height

    def choose_division(self):
        if self.height < 150 and self.weight < 75:
            return 'Infanterie'
        return 'Artillerie'


soldier = Soldier('Ali', 25, 'male', 70, 160)
print(soldier.choose_division())
