class Book:

    def __init__(self, name: str, author: str, price: float, genre: str, page: int):
        self.name = name
        self.author = author
        self.price = price
        self.genre = genre
        self.page = page

    def get_full_info(self) -> dict:
        return {'name': self.name, 'author': self.author, 'price': self.price, 'genre': self.genre, 'page': self.page}

    def change_price(self, new_price: float) -> None:
        self.price = new_price
