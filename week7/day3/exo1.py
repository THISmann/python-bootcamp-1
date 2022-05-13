# class Dog ():
#     def __init__(self , name_human , age_human , size_human):
#         self.name = name_human
#         self.age = age_human
#         self.size = size_human


# dog1 = Dog()

# dog1.color = "red"

# print(dog1.color)


class Computer():

    def description(self, name):
        """
        This is a totally useless function
        """
        print("I am a computer, my name is", name)
        # Analyse the line below
        print(self)


mac_computer = Computer()
mac_computer.brand = "Apple"
print(mac_computer.brand)

dell_computer = Computer()

#Computer.description(dell_computer, "Mark")
# IS THE SAME AS:
dell_computer.description("Mark")


class BankAccount:

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def view_balance(self):
        self.transactions.append("View Balance")
        print(f"Balance for account {self.account_number}: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount < 100:
            print("Minimum deposit is 100")
        else:
            self.balance += amount
            self.transactions.append(f"Deposit: {amount}")
            print("Deposit Succcessful")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")
            print("Withdraw Approved")
            return amount

    def view_transactions(self):
        print("Transactions:")
        print("-------------")
        for transaction in self.transactions:
            print(transaction)


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat("nono", 22)
cat2 = Cat("poupou", 19)
cat3 = Cat("titi", 18)

li = [cat1, cat2, cat3]


def compare_age(lis):
    age = 0
    name = ""
    for item in lis:
        if item.age > age:
            age = item.age
            print(item.name)
            return item.name


print(f"The oldest dog is {compare_age(li)}")


class Dog():
    def __init__(self, name, heigth):
        self.name = name
        self.heigth = heigth

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumb {self.heigth*2} cm")


davids_dog = Dog("rex", 50)

davids_dog.bark()
davids_dog.jump()

sarah_dog = Dog("Teacup", 20)

sarah_dog.bark()
sarah_dog.jump()

dog_list = [davids_dog, sarah_dog]
dog_heigth = 0

for item in dog_list:
    if item.heigth > dog_heigth:
        dog_heigth = item.heigth
        print(f"le plus grand chien est {item.name}")


class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for item in self.lyrics:
            print(item)


stairway = Song(["There’s a lady who's sure", "all that glitters is gold",
                "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()
