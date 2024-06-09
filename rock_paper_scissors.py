import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

user_score = 0
computer_score = 0

while True:
    user_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
    if user_choice == 'quit':
        break
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please try again.")
        continue
    
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1
    
    print(f"Score: You {user_score} - Computer {computer_score}")

print("Thanks for playing!")

# OUTPUT

# Enter rock, paper, or scissors (or 'quit' to exit): rock
# You chose: rock
# Computer chose: scissors
# You win!
# Score: You 1 - Computer 0
# Enter rock, paper, or scissors (or 'quit' to exit): paper
# You chose: paper
# Computer chose: rock
# You win!
# Score: You 2 - Computer 0
# Enter rock, paper, or scissors (or 'quit' to exit): scissors
# You chose: scissors
# Computer chose: scissors
# It's a tie!
# Score: You 2 - Computer 0
# Enter rock, paper, or scissors (or 'quit' to exit): quit
# Thanks for playing!
