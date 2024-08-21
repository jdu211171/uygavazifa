
def bigger_price(num: int, catalog: list) -> list:
    sorted_catalog = sorted(catalog, key=lambda x: x['price'], reverse=True)
    return sorted_catalog[:num]


print(bigger_price(2, [{'name': 'bread', 'price': 5}, {'name': 'wine', 'price': 138}, {'name': 'meat', 'price': 15}, {'name': 'water', 'price': 1}]))
