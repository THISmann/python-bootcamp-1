class Dog():
    number_of_dogs = 0
    dogs_king = "Bernie IV"

    # Initializer / Instance Attributes
    def __init__(self, name_of_the_dog):
        print("A new dog has been initialized !")
        print("His name is", name_of_the_dog)
        self.name = name_of_the_dog

    def bark(self):
        print("{} barks ! WAF".format(self.name))

    def walk(self, number_of_meters):
        print("{} walked {} meters".format(self.name, number_of_meters))

    def rename(self, new_name):
        self.name = new_name


my_dog = Dog("Rex")
my_dog.rename("Paul")
print(Dog.dogs_king)
print("Curently, there are {} dogs".format(Dog.number_of_dogs))

bull = Dog("bull")
rex = Dog("rex")
maxi = Dog("maxi")

print("Curently, there are {} dogs".format(Dog.number_of_dogs))
