#Rock-Paper-Scissors Build a Rock-Paper-Scissors game where the user plays against the computer.\import random
import random 
def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    
    # List of valid moves
    choices = ["rock", "paper", "scissors"]
    
    # Get the user's move
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    
    # Check if the user's input is valid
    if user_choice not in choices:
        print("Invalid choice, please choose rock, paper, or scissors.")
        return
    
    # Get the computer's move randomly
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

# Start the game
rock_paper_scissors()
