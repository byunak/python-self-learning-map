import random

hands = ['Rock','Paper','Scissors']



while True:
    player_input = input("Please write your selection (Rock,Paper,Scissors)")
    computer_selection = random.choice(hands)

    if player_input == "Rock" and computer_selection == hands[0]:
        print("You chose ",player_input,"and Computer chose", hands[0],"which means DRAW")
        continue
    elif player_input == "Rock" and computer_selection == hands[1]:
        print("You chose ",player_input,"and Computer chose", hands[1],"which means YOU LOST")
        continue
    elif player_input == "Rock" and computer_selection == hands[2]:
        print("You chose ",player_input,"and Computer chose", hands[2],"which means YOU WIN!")
        continue
    elif player_input == "Paper" and computer_selection == hands[0]:
        print("You chose ",player_input,"and Computer chose", hands[0],"which means YOU WIN!")
        continue
    elif player_input == "Paper" and computer_selection == hands[1]:
        print("You chose ",player_input,"and Computer chose", hands[1],"which means DRAW")
        continue
    elif player_input == "Paper" and computer_selection == hands[2]:
        print("You chose ",player_input,"and Computer chose", hands[2],"which means YOU LOST")
        continue
    elif player_input == "Scissors" and computer_selection == hands[0]:
        print("You chose ",player_input,"and Computer chose", hands[0],"which means YOU LOST")
        continue
    elif player_input == "Scissors" and computer_selection == hands[1]:
        print("You chose ",player_input,"and Computer chose", hands[1],"which means YOU WIN")
        continue
    elif player_input == "Scissors" and computer_selection == hands[2]:
        print("You chose ",player_input,"and Computer chose", hands[2],"which means DRAW")
        continue
    elif player_input != "Scissors" or player_input != "Rock" or player_input != "Paper":
        print("Please make sure you type Rock, Paper or Scissors")
        continue


     
    