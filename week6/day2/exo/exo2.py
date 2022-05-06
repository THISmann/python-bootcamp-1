# number = int(input("intrer votre nombre"))
# table = list(range(1, 12))

# for tab in table:
#     print(f"{tab} * {number} = {tab * number}")


# num = 1
# while num < 11:
#     print(num)
#     num += 1


# userString = input('votre string svp')
# if len(userString) > 10:
#     print(" String too long")
# else:
#     print(" string is shoot")


# for i in list(range(1, len(stg))):
#     print(stg[0:i + 1])


# person_age = int(input("you age :"))
# ticket_price = 0

# if person_age < 3:
#     ticket_price = 0
#     print("the ticket is free")
# elif person_age > 3 and person_age < 13:
#     ticket_price = 10
#     print("the ticket price is ", ticket_price, "$")
# elif person_age > 12:
#     ticket_price = 15
#     print("the ticket price is ", ticket_price, "$")


family = {"rick": 43, "beth": 13, "morty": 5, "summer": 12}
som = 0

for x, y in family.items():
    if family[x] < 3:
        ticket_price = 0
        som += ticket_price
        print("the ticket is free")
    elif family[x] > 2 and family[x] < 13:
        ticket_price = 10
        som += ticket_price
        print("the ticket price is ", ticket_price, "$")
    elif family[x] > 12:
        ticket_price = 15
        print("the ticket price is ", ticket_price, "$")
        som += ticket_price

print("the price ", som)
