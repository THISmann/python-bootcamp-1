# For example,
# my_name = "Frank"  this line creates a name variable type: string
#print("My name is {}".format(my_name))

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

a = 33
b = 200
if a > b:
    print("a is greater than b")

print("Finished")


a = 33
b = 200

if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")

print("Finished")


if a > b:
    print(" a is small than b")
elif a < b:
    print("a si greater than b")
elif a == b:
    print(("a == b"))


my_hobbies = ["sport", "code", "food", "icecreams", "netflix"]
if "code" in my_hobbies:
    print("Hello world")
    
    
 
user_number = input("entrez un nombre")
if int(user_number) % 3 == 0:
    print("Fizz")  
elif int(user_number) % 5 == 0:
    print("Buzz")
elif int(user_number) % 3 == 0 and int(user_number) % 5 == 0:
    print("Fizz Buzz")
        