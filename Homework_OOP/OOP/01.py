class Persone:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greate(self):
        return self.name, self.age


person1 = Persone('Vasil', 39)

print(person1.greate())
