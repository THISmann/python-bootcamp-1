class Circle:
    color = "red"

    def __init__(self, diameter):
        self.diameter = diameter

    def grow(self, factor=2):
        self.diameter = self.diameter * factor

    def get_color(self):
        return Circle.color


circle1 = Circle(2)
print(circle1.color)
print(Circle.color)
print(circle1.get_color())
circle1.grow(3)
print(circle1.diameter)


class MyClass:
    @staticmethod
    def add(a, b):
        return a + b


Tle = MyClass()
print(Tle.add(2, 3))

# print(MyClass.add(3, 6))


class Person:

    used_names = set()

    def __init__(self, name, age):
        if name in self.used_names:
            name = input("That name is taken. Enter another name: ")

        self.name = name
        self.age = age
        self.used_names.add(name)

    @classmethod
    def fromYear(cls, name, birth_year):
        THIS_YEAR = 2020
        return cls(name, THIS_YEAR - birth_year)

    @property
    def professional_name(self):
        return "Mr " + self.name


etienne = Person('fuh', 23)
print(etienne.fromYear('fuh ', 1999).professional_name)
print(Person.used_names)

def test(x):
    x = input('send')
    return  abs(x) , int(x) , x
 
print(test.__doc__)


class Dog:
    pass
