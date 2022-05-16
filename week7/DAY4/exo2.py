class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog(Animal):
    def bark(self):
        print(f"{self.name} tu es le meilleur des chiens")

    def bomb(self):
        print(f"{self.name} tu as {self.age}")


bog = Dog("rex", 10)
bog.bark()
bog.bomb()


class Animal():
    def __init__(self, type, number_legs, sound):
        self.type = type
        self.number_legs = number_legs
        self.sound = sound


class Dog(Animal):
    def __init__(self, type, number_legs, sound, fetch_ball):
        super().__init__(type, number_legs, sound)
        #     # Or : Animal.__init__(self,type, number_legs, sound)
        #     self.fetch_ball = fetch_ball


rex = Dog('dog', 4, 'woupp', False)
print(rex.type)


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
c.set_max_price(200)
c.sell()


class Book():
    def __init__(self, title, author, publication_date, price):
        self.title = title
        self.author = author
        self.publication = publication_date
        self.price = price

    def present(self):
        print(f'Title: {self.title}')


class Fiction(Book):
    def __init__(self, title, author, publication_date, price, is_awesome):
        super().__init__(title, author, publication_date, price)
        self.genre = 'Fiction'
        self.is_awesome = is_awesome
        if self.is_awesome:
            self.bored = False
            print('Woow this is an awesome book')
        else:
            self.bored = True
            print('I am very bored')


print(__name__)
foundation = Fiction("nice live", "etienne", "19/02/20", 400, False)
print(foundation.bored)


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

# question 1


class Charplom(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# question2
instance1 = Bengal('wouffff', 32)
instance2 = Chartreux('nickkkk', 3)
instance3 = Charplom("rex", 4)

# question3
my_cats = [instance1, instance2, instance3]

# question4
my_pets = Pets(my_cats)

my_pets.walk()


#Exercise 2

class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def bark(self):
        print(f'{self.name} is barking')
        return f'{self.name} is barking'
    
    def run_speed(self):
        print(f'the dog running speed{self.weight/self.age*10}')
        return f'{self.weight/self.age*10}'  
    
    def fight(self , other_dog):
        print(f'which {other_dog} want to fly')
        return f'which {other_dog} want to fly'  
    
dog1 = Dog('rex', 12 , 23)   
dog2 = Dog('pirex', 13 , 23) 
dog3 = Dog('bouldog', 12 , 23) 

dog1.run_speed()