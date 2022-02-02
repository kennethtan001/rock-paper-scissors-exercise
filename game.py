
import os
import random

def determine_winner(choice_1, choice_2):

    if (choice_1 == choice_2):
        winner = "None"
    if(choice_1 == "rock" and choice_2 == "paper"):
        winner = "paper"
    if(choice_1 == "rock" and choice_2 == "scissors"):
        winner = "rock"
    if(choice_1 == "paper" and choice_2 == "rock"):
        winner = "paper"
    if(choice_1 == "paper" and choice_2 == "scissors"):
        winner = "scissors"
    if(choice_1 == "scissors" and choice_2 == "rock"):
        winner = "rock"
    if(choice_1 == "scissors" and choice_2 == "paper"):
        winner = "scissors"
    return winner


if __name__ == "__main__":
    player_name = os.getenv("PLAYER_NAME", default="Player One")
    print("-------------------")
    print("Welcome ",player_name," to my Rock-Paper-Scissors game...")
    print("-------------------")
    user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")
    user_choice = user_choice.lower()
    if (user_choice == "rock"):
        print("You chose: ",user_choice)
    elif (user_choice == "paper"):
        print("You chose: ",user_choice)
    elif (user_choice == "scissors"):
        print("You chose: ",user_choice)
    else:
        print("Sorry that is not a valid option")
        exit()


    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    print ("Computer Choice: ", computer_choice)
    print("-------------------")


    #if (userChoice == computerChoice):
    #    print("Game is a tie!")
    #    print("-------------------")
    #    print("Thanks for playing. Please play again!")
    #if((userChoice == "rock" and computerChoice == "paper") or (userChoice == "paper" and 
    #computerChoice == "scissors") or (userChoice == "scissors" and computerChoice == "rock")):
    #    print("Oh, the computer won. It's ok.")
    #    print("-------------------")
    #    print("Thanks for playing. Please play again!")
    #if((userChoice == "paper" and computerChoice == "rock") or (userChoice == "scissors" and 
    #computerChoice == "paper") or (userChoice == "rock" and computerChoice == "scissors")):
    #    print("Congrats, you won!")


    winner = determine_winner(userChoice,computerChoice)
    if (winner == user_choice):
        print("Congrats, you won!")
    if (winner == computer_choice):
        print("Oh, the computer won. It's ok.")
    if (winner == None):
        print("Game is a tie!")
    print("-------------------")
    print("Thanks for playing. Please play again!")