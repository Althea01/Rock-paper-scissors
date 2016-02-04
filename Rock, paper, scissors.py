__author__ = 'Lily'

import random
userChoice = raw_input("Do you choose rock, paper, or scissors?")
computerChoice = random.random()
print computerChoice

if (computerChoice < 0.34):
    computerChoice = "rock"
elif (computerChoice <= 0.67):
    computerChoice = "paper"
else:
    computerChoice = "scissors"

def compare(choice1, choice2):
    choice1 = userChoice
    choice2 = computerChoice
    if (choice1 == choice2):
        return "The result is a tie."
    elif (choice1 == "rock"):
        if (choice2 == "scissors"):
            return "Rock wins."
        else:
            return "Paper wins"
    elif (choice1 == "paper"):
        if (choice2 == "rock"):
            return "Paper wins."
        else:
            return "Scissors wins"
    elif (choice1 == "scissors"):
        if (choice2 == "paper"):
            return "Scissors wins."
        else:
            return "Rock wins"

print("Computer: " + computerChoice)
print compare(userChoice,computerChoice)
