
def bigger_price(son: int, catalog: list) -> list:
    catalog = sorted(catalog, key=lambda x: list(x.keys())[0], reverse=True)
    return [catalog[i] for i in range(son)]


print(bigger_price(2, [{'a': 1}, {'b': 2}, {'c': 3}]))
