class Talaba:

    def __init__(self, ism: str, familiya: str, baho: int):
        self.ism = ism
        self.familiya = familiya
        self.baho = baho


talaba1 = Talaba('Nur Islom', 'Tukhtamishhoji-zoda', 494)
talaba2 = Talaba('Samandar', 'Oydinov', 500)
talaba3 = Talaba('Asadbek', 'Mo\'minov', 489)

talabalar = [talaba2, talaba1, talaba3]
talabalar.sort(key=lambda x: x.baho)

print(talabalar[0].ism)
