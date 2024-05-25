import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Enter Rock/Paper/Scissors or Q to exit the game: ").lower()
    
    if user_input == "q":
        break
    elif user_input not in options:
        print("Invalid input, please try again.")
        continue

    random_no = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_input = options[random_no]
    print("Computer picked:", computer_input)

    if user_input == "rock" and computer_input == "scissors":
        print("You win!")
        user_wins += 1 
    elif user_input == "paper" and computer_input == "rock":
        print("You win!")
        user_wins += 1 
    elif user_input == "scissors" and computer_input == "paper":
        print("You win!")
        user_wins += 1 
    elif user_input == computer_input:
        print("It's a tie!")
    else:
        print("Computer wins!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.")
print("Goodbye!")
