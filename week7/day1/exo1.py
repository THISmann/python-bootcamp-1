try:
    print(x)
except:
    print("An error occurred")


# def check_arguments(*args):
#     print(f"These are the arguments {args}")


# check_arguments(1, 2, 'hey')


def send_double(*args):
    return map(lambda n: n*2, args)


print(list(send_double(1, 3, 5, 7, 9)))


def check_keywordedarguments(**kwargs):
    return kwargs


print(check_keywordedarguments(fruit='apple', ordered=2))


def check(a, b, c, d):
    print(a, b, c, d)


a = [1, 2, 3, 5]
check(*a)

# A refaire ca ne marche pas


def sum_number(*args):
    num = 0
    for item in args:
        try:
            num += item
        except:
            continue


print(sum_number(12, 32, 21, 13, "erwrw", 12, "21"))

# A refaire ca ne marche pas


people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]


def say_hello(tab):
    for item in tab:
        try:
            # filter(lambda item : item.length = 4, tab)
            if(len(item) == 4):
                print(f"hello {item}")
        except:
            continue


print(say_hello(people))

# people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
# li = map(lambda n: print(f"hello {n}"), list(
#     filter(lambda n: len(n) <= 4, people)))
# print(list(li))
