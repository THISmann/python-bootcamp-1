class MyClass(object):
    def func(self):
        print("I'm being called from the Parent class")


class ChildClass(MyClass):
    def func(self):
        print("I'm actually being called from the Child class")
        print("But...")
        # Calling the `func()` method from the Parent class.
        super(ChildClass, self).func()


my_instance_2 = ChildClass()
my_instance_2.func()


# class Door:
#     def __init__(self, is_open):
#         self.is_open = is_open

#     def open_dog(self):
#         self.is_open = True

#     def close_dog(self):
#         self.is_open = False


# class BlockedDoor(Door):
#     def open_dog(self):
#         print("hello")

#     def close_dog(self):
#         print("")

class Computer():

    def __init__(self):
        self.name = "Apple Computer"  # public
        self.__max_price = 900  # private

    def sell(self):            # public method
        print(f"Selling Price: {self.__max_price}")

    def __sell(self):          # private method
        print('This is private method')

    def set_max_price(self, price):
        self.__max_price = price


c = Computer()
print(c.set_max_price(99))


class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class CatBreed(Cat):
    pass


instance1 = Cat("wow", 7)
instance2 = Cat("zoz", 2)
instance3 = Cat("Rock", 3)

my_list = [instance1, instance2, instance3]

my_cats = Pets("cat")
my_pet = my_cats

for x in my_list:
    print(x.walk())
