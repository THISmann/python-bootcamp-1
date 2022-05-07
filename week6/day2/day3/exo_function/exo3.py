# Some Geography

import random


def describe_city(city, country="cameroun"):
    print(city, "is in ", country)


describe_city("yaounde")

# Random


def random_generator(number):
    num = int(random.random()*1)
    if(num == number):
        print("success the number is correct")
    else:
        print("Failled !!")


random_generator(99)

# Personalized Shirts !


def make_shirt(size="large", text="i love python"):
    print("you tee-shirt is size :", size, "and the message is ", text)


make_shirt("medium")
make_shirt("large", "i miss you")

# Magicians ...add()
magicians = ["abeba", "toto", "momo", "nono", "papa"]

def make_great():
    for item in magicians:
        item += " this great"
        print(item)
        
def show_magicians():
    make_great() 



    
    