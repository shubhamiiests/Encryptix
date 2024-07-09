import random

def get_computer_choice():
    """Randomly selects 'rock', 'paper', or 'scissors' for the computer."""
    possible_actions = ["rock", "paper", "scissors"]
    return random.choice(possible_actions)

def determine_winner(user_action, computer_action):
    """Determines the winner based on the user and computer choices."""
    if user_action == computer_action:
        return "It's a tie!"
    elif (user_action == "rock" and computer_action == "scissors") or \
         (user_action == "paper" and computer_action == "rock") or \
         (user_action == "scissors" and computer_action == "paper"):
        return "You win!"
    else:
        return "You lose."

def display_choices(user_action, computer_action):
    """Displays the choices of the user and the computer."""
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

def play_game():
    user_score = 0
    computer_score = 0
    
    print("Welcome to Rock, Paper, Scissors!")
    print("Choose rock, paper, or scissors. Type 'quit' to exit.")
    
    while True:
        user_action = input("Enter your choice (rock, paper, scissors): ").lower()
        
        if user_action == 'quit':
            break
        
        if user_action not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        computer_action = get_computer_choice()
        display_choices(user_action, computer_action)
        
        result = determine_winner(user_action, computer_action)
        print(result)
        
        if result == "You win!":
            user_score += 1
        elif result == "You lose.":
            computer_score += 1
        
        print(f"Score: You - {user_score}, Computer - {computer_score}")
        
        play_again = input("Play again? (y/n): ").lower()
        if play_again != "y":
            break
    
    print("Thanks for playing!")
    print(f"Final Score: You - {user_score}, Computer - {computer_score}")

# Start the game
play_game()





# import random

# while True:
    
#     user_action = input("Enter a choice (rock, paper, scissors): ")
#     possible_actions = ["rock", "paper", "scissors"]
#     computer_action = random.choice(possible_actions)
#     print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

#     if user_action == computer_action:
#         print(f"Both players selected {user_action}. It's a tie!")
#     elif user_action == "rock":
#         if computer_action == "scissors":
#             print("Rock smashes scissors! You win!")
#         else:
#             print("Paper covers rock! You lose.")
#     elif user_action == "paper":
#         if computer_action == "rock":
#             print("Paper covers rock! You win!")
#         else:
#             print("Scissors cuts paper! You lose.")
#     elif user_action == "scissors":
#         if computer_action == "paper":
#             print("Scissors cuts paper! You win!")
#         else:
#             print("Rock smashes scissors! You lose.")

#     play_again = input("Play again? (y/n): ")
#     if play_again.lower() != "y":
#         break