import random
options = ("rock", "paper", "scissor")


running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice between rock, paper or scissor: ")
    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissor":
        print("you win!")
    elif player == "paper" and computer == "rock":
        print("you win!")
    elif player == "scissor" and computer == "paper":
        print("you win!")
    else:
        print("you lose!")

    print(f"Player choice: {player}")
    print(f"Computer choice: {computer}")
    if not input("Do you want to play again? (y/n): ").lower() == "y":
         running = False


print("Thank you for playing!")

