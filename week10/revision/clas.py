class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self):
        print('Person: {}, Age: {}'.format(self.name, self.age))

    def __repr__(self):
        return f"{self.__class__.__name__} : {self.name} {self.age}"

    def __add__(self, other):
        return Person(self.name, other.name)


father = Person('dad', 60)
mother = Person('mom', 65)

family = father + mother
print(family)
goolove = Person('goolove', 23)
