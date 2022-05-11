from functools import reduce


def test(*args):
    print(list(args))


print(test(1, 3, "wi"))


def say_test(**kwargs):
    for x, y in kwargs.items():
        print(x, y)


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}


say_test(brand="sarah", age=21, classe="terminal")


def check_arguments_keywordedarguments(*args, **kwargs):
    print('*args', args)
    print('**kwargs', kwargs)


print(check_arguments_keywordedarguments(
    12, "etienne", 53, nom="fuh", classe="ter"))


def check(number, *numbers, **dict):
    print(number)

    for element in numbers:
        print(element)

    for x, y in dict.items():
        print(f"value = {x} + {y}")


print(check("hello", 1, 2, 3, name="etienne", last="fuh"))


def check(a, b, c):
    print(a, b, c)


a = [1, 3, 5]
print(check(*a))

a = {'a': 'etienne', 'b': 'fuh', 'c': 'goolove'}
print(check(**a))

try:
    num = 1
    num2 = 0
    num/num2
except:
    print("call emergency")


def age():
    #user_age = input("how old are you ? \n >>>")
    user_age = 22

    try:
        user_age = int(user_age)
        print(f"i have {user_age}")
    except:
        print("sorry")


age()

my_list = [2, "3", 1, " 2", "hello",  "42", 1, -5, "3", "store"]


def sums(*args):
    som = 0
    for x in args:
        try:
            som += x
        except:
            continue
        else:
            print("saluer")
        finally:
            print('you are Welcome here !!')
    return som


print(sums(*my_list))

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]

map_object = map(lambda n: n.upper(), fruit)
print(list(map_object))

filter_obj = filter(lambda n: n[0] == "A", fruit)
print(list(filter_obj))

my_lists = [1, 3, 5, 7]
reduce_obj = reduce(lambda a, b: a+b, my_lists)

print(reduce_obj)

people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
len_four = filter(lambda n: len(n) == 4, people)
map_people = map(lambda n: print(f"hello word {n} \n"), len_four)
print(list(map_people))


def factoriel(n): return reduce(lambda x, y: x*y, range(1, n+1))


print(factoriel(5))
