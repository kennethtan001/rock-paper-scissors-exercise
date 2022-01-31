
import os
import random


player_name = os.getenv("PLAYER_NAME", default="Player One")
print("-------------------")
print("Welcome ",player_name," to my Rock-Paper-Scissors game...")
print("-------------------")
userChoice = input("Please choose either 'rock', 'paper', or 'scissors': ")
userChoice = userChoice.lower()
if (userChoice == "rock"):
    print("You chose: ",userChoice)
elif (userChoice == "paper"):
    print("You chose: ",userChoice)
elif (userChoice == "scissors"):
    print("You chose: ",userChoice)
else:
    print("Sorry that is not a valid option")
    exit()


randomizer = [1, 2, 3] 
if (random.choice(randomizer) == 1):
    computerChoice = "rock"
elif (random.choice(randomizer) == 2):
    computerChoice = "paper"
else:
    computerChoice = "scissors"
print ("Computer Choice: ", computerChoice)
print("-------------------")


if (userChoice == computerChoice):
    print("Game is a tie!")
    print("-------------------")
    print("Thanks for playing. Please play again!")
if((userChoice == "rock" and computerChoice == "paper") or (userChoice == "paper" and 
computerChoice == "scissors") or (userChoice == "scissors" and computerChoice == "rock")):
    print("Oh, the computer won. It's ok.")
    print("-------------------")
    print("Thanks for playing. Please play again!")
if((userChoice == "paper" and computerChoice == "rock") or (userChoice == "scissors" and 
computerChoice == "paper") or (userChoice == "rock" and computerChoice == "scissors")):
    print("Congrats, you won!")
    print("-------------------")
    print("Thanks for playing. Please play again!")