# Use a function to determine the outcome: Instead of using a long series of if-elif statements to determine the outcome of the game, you could define a function that takes the player's selection and the computer's selection as arguments and returns the outcome. 
# This would make the code easier to read and maintain.

# Use a dictionary to store the possible outcomes: Instead of using a series of if-elif statements to determine the outcome of the game, you could use a dictionary to map the possible combinations of player and computer selections to the corresponding outcome. 
# This would make the code more concise and easier to understand.

# Use a loop to handle invalid input: Instead of using an elif statement to handle invalid input, you could use a while loop to keep prompting the player to enter a valid value until they do so. 
# This would make it easier for the player to correct their mistake and avoid having to run the script again.

## I also realized that even after ChatGPT revision, case-insensitivity was necessary so I made him add that feature too.
## It got little confused so I had to edit the code a little.

import random

def determine_outcome(player_choice, computer_choice):
    outcomes = {
        ("rock", "rock"): "Draw",
        ("rock", "paper"): "Computer wins",
        ("rock", "scissors"): "Player wins",
        ("paper", "rock"): "Player wins",
        ("paper", "paper"): "Draw",
        ("paper", "scissors"): "Computer wins",
        ("scissors", "rock"): "Computer wins",
        ("scissors", "paper"): "Player wins",
        ("scissors", "scissors"): "Draw"
    }
    return outcomes[(player_choice, computer_choice)]

while True:
    player_choice = input("Please write your selection (Rock,Paper,Scissors): ").lower()
    computer_choice = random.choice(["rock", "paper", "scissors"]).lower()

    while player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid input. Please enter a valid choice.")
        player_choice = input("Please write your selection (Rock,Paper,Scissors): ").lower()

    outcome = determine_outcome(player_choice, computer_choice)
    print(f"You chose {player_choice.upper()} and the computer chose {computer_choice.upper()}. {outcome}.")