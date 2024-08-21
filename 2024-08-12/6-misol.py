class Car:

    def __init__(self, brands: list):
        self.brands = brands

    def brand_exists(self, brand: str) -> bool:
        return brand in self.brands


lst1 = Car(['BMW', 'Ford', 'Toyota', 'Volkswagen', 'Audi', 'Honda', 'Mercedes Benz', 'Hyundai', 'Nissan'])

print(lst1.brand_exists('Lexus'))
print(lst1.brand_exists('Ferrari'))
print(lst1.brand_exists('Ford'))
