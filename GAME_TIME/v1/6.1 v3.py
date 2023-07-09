"""
    @conditional statement ..
    starting development of game with conditional .
    Improving the game with more coditional
    making the game more fun with conditionals
    @Introducing randint : randint is an inbuilt program for python
    that must be imported from python global library
    @randint is a function that let one generate random variable
    through it sub pack call random
    @random is the main sub pack in randint that enables generations
"""

from random import randint
print("Rock...")
print("Paper...")
print("Scissors...")

player = input("Player, make your move: \n").lower()
rand_num = randint(0, 2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"

print(f"Computer plays {computer}")

if player == computer:
    print("It's a tie!")
elif player == "rock":
    if computer == "scissors":
        print("player wins!")
    else:
        print("computer wins!")
elif player == "paper":
    if computer == "rock":
        print("player wins!")
    else:
        print("computer wins!")
elif player == "scissors":
    if computer == "paper":
        print("player wins!")
    else:
        print("computer wins!")
else:
    print("Please enter a valid move!")
