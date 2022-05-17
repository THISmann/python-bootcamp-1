import random


class Game:
    def __init__(self, user_name):
        self.user_name = user_name

    def get_user_item(self):
        self.user_item = input(
            "choose one item 'rock' , 'paper' and 'scissors'")
        choose = ['paper', 'rock', 'scissors']
        for item in choose:
            if item == self.user_item:
                return self.user_item

        # if self.user_item in choose:
        #     return self.user

    def get_computer_item(self):
        # ran = random.sample(['paper', 'rock', 'scissors'],1)
        # return ran
        ran = random.choice(['paper', 'rock', 'scissors'])
        return ran

    def get_game_result(self, user_item, computer_item):
        computer_item = self.get_computer_item()
        user_item = self.get_user_item()
        if user_item == "rock" and computer_item == "scissors":
            print(f"{self.user_name} have win ")
            return 'win'
        elif user_item == "scissors" and computer_item == "paper":
            print(f"{self.user_name} have win ")
            return 'win'
        elif user_item == "paper" and computer_item == "rock":
            print(f"{self.user_name} have win ")
            return 'win'
        elif user_item == "paper" and computer_item == "scissors":
            print(f"{self.user_name} have loss ")
            return 'loss'
        elif user_item == "rock" and computer_item == "paper":
            print(f"{self.user_name} have loss ")
            return 'loss'
        elif user_item == "scissors" and computer_item == "rock":
            print(f"{self.user_name} have loss ")
            return 'loss'
        else:
            return 'draw'

    def play(self):
        pass
