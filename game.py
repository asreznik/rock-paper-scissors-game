import random
import os
from dotenv import load_dotenv

load_dotenv()

x = os.getenv("PLAYER_NAME")
print(x)

print("----------------")
#game.py
print("Welcome,", x, ", to Rock, Paper, Scissors, Shoot!")

#Prompt user input
user_choice = input("Choose 'rock' or 'paper' or 'scissors.': ").lower() 
print("----------------")
print("You chose:", user_choice)

#Computer choice at random
options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
print("The computer chose:", computer_choice)
print("----------------")
if(user_choice == "rock"):
    if(computer_choice == "rock"):
        print("You tie.")
    elif(computer_choice == "paper"):
        print("You lose.")
    else:
        print("You win!")
elif(user_choice == "paper"):
    if(computer_choice == "rock"):
        print("You win!")
    elif(computer_choice == "paper"):
        print("You tie.")
    else:
        print("You lose.")
elif(user_choice == "scissors"):
    if(computer_choice == "rock"):
        print("You lose.")
    elif(computer_choice == "paper"):
        print("You win!")
    else:
        print("You tie.")
else:
    print("Please enter a valid entry - 'rock' or 'paper' or 'scissors.'")

print("Thanks for playing. Please play again!")