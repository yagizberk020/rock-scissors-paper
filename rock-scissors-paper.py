import random
from secrets import choice
choices = ["r" , "p" , "s" ]
num_games = 3

def did_win(you, computer):
    if you == computer:
        return 0
    elif you == "r" and computer == "s":
        return 1
    elif you == "s" and computer == "p":
        return 1
    elif you == "p" and computer == "r":
        return 1
    
    return -1    


def print_results(result):
    if result == 1:
        print("You win")
    elif result == 0:
        print("Tie")
    else:
        print("You lose") 


def print_choices(you, computer):

    table = {
        's': 'scissors',
        'r': 'rock',
        'p': 'paper'
    }

    print("--------------------------------------")
    print(f"YOU: {table[you]},  COMPUTER: {table[computer]}")
    print("--------------------------------------")


def main():
    game_no = 0
    while game_no <= num_games:
        computer_choice = random.choice(choices)
        your_choice = input("Please enter 'r', 's', or 'p'?")

        result = did_win(your_choice, computer_choice)

        print_choices(your_choice, computer_choice)

        print_results(result)

        game_no += 1



main()