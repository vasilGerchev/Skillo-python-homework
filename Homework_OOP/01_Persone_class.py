class Person:
    def __init__(self, person, age, country):
        self.person = person
        self.age = age
        self.country = country

    def __str__(self):
        return f"My name is {self.person}, I'm {self.age} old and I Live in {self.country}"


person_one = Person('Vasil', 39, 'Bulgaria')
person_two = Person('Diana', 39, 'Bulgaria')

print(person_one.__str__())
print(person_two.__str__())
