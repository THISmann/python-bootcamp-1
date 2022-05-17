from Game.py import Game


def get_user_menu_choice():
    print("simple Menu")
    print("(g) Play a new game")
    print("(x) Show scores and exit ")
    print("(q) quit the game !!!  ")


def print_results(results):
    results = {
        "win": 0,
        "loss": 0,
        "draw": 0
    }


def main():
    new_game = Game('user')
    new_game.play()


def play():
    pass
