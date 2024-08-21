# all() / any()
string = ['My user input', 'asef', True, False]
print(all(string))
print(any(string))

# format()
print(bin(3).split('b')[-1])
print(format(-14, 'b'))
print(format(11, '0x'))
print(hex(12))
print(format(98, 'c'))
print(format(8, 'o'))

# frozenset()
frznst = frozenset(string)
print(frznst.union({'a', 'b'}))

# getattr()
class Person:
  def __init__(self, name: str, age: int, country: str) -> None:
      self.name = name
      self.age = age
      self.country = country


# getattr(obj, attribute)
person = Person('John', 36,'Norway')

print(getattr(person, 'country', 'my message'))
delattr(person, 'age')
print(hasattr(person, 'age'))
setattr(person, 'age', 38)
print(person.age)

# callable()
print(callable(Person))
