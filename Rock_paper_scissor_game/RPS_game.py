# Rock Paper and scissor Game
# Rule 1 - if(player chooses rock and computer paper)- computer wins
# Rule 2- if(player chooses rock and computer scissor)- player wins
# Rule 3- if(player as well as computer chooses same)- Tie
# Rule 4- if(player chooses paper  and computer chooses rock)- player wins
# Rule 6- if (player chooses paper and computer scissor)- player wins
# Rule 7- if(player chooses scissors and computer chooses rock)- computer wins
# Rule 8- if (player chooses scissors and computer chooses paper)- Player wins

import random
while True:
    choices = ["rock", "scissor", "paper"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Enter your choice : rock | paper | scissor ").lower()

    if player == computer:
        print("computer : "+computer)
        print("You : "+player)
        print("Tie")
    elif player == "rock":
        if computer == "paper":
            print("computer : " + computer)
            print("You : " + player)
            print("You Lose!")
        if computer == "scissor":
            print("computer : " + computer)
            print("You : " + player)
            print("You win!")
    elif player == "paper":
        if computer == "rock":
            print("computer : " + computer)
            print("You : " + player)
            print("You win!")
        if computer == "scissor":
            print("computer : " + computer)
            print("You : " + player)
            print("You Lose!")
    elif player == "scissor":
        if computer == "rock":
            print("computer : " + computer)
            print("You : " + player)
            print("You Lose!")
        if computer == "paper":
            print("computer : " + computer)
            print("You : " + player)
            print("You win")
    play_again = input("Play again ? (yes/no)").lower()

    if play_again != "yes":
        break

print("Bye")



