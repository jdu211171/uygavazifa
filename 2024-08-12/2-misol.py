class Bino:

    def __init__(self, balandlik: float, rang: str):
        self.balandlik = balandlik
        self.rang = rang


bino1 = Bino(494, 'Ko\'k')
bino2 = Bino(500, 'Yashil')
bino3 = Bino(489, 'Qizil')

binolar = [bino2, bino1, bino3]
for bino in binolar:
    if bino.balandlik > 50:
        print(bino.rang)
