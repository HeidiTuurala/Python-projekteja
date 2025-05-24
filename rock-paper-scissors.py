import random

while True:
    #User makes a choice
    user_action = input("Enter a choice (rock, paper, scissors): ")

    #Computer gives random choice
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)

    print(f"\nYou chose {user_action}, computer chose {computer_action}. \n")

    #Winner

    if user_action == computer_action:
        print(f"Both palyers selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "paper":
            print(f"Paper covers rock! You lose.")
        else:
            print(f"Rock smashes scissors! You win!")
    elif user_action == "paper":
        if computer_action == "scissors":
            print("Scissors cuts paper! You lose.")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print(f"Rock smashes scissors! You lose.")
    
    play_again = input("Do you want to play again? (yes / no): ")
    if play_again == "no":
        print("Thanks for a game. Hope we see you soon!")
        break
    if play_again == "yes":
        continue