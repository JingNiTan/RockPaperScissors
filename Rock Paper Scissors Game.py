import random

while True:
    User_action = input("Enter a choice (Rock, Paper, Scissors): ")
    Possible_actions = ["Rock", "Paper", "Scissors"]
    Computer_action = random.choice(Possible_actions)
    print(f"\nYou chose {User_action}, computer chose {Computer_action}.\n")

    if User_action == Computer_action:
        print(f"Both players selected {User_action}. It's a tie!")
    elif User_action == "Rock":
        if Computer_action == "Scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif User_action == "Paper":
        if Computer_action == "Rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif User_action == "Scissors":
        if Computer_action == "Paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    Play_again = input("Play again? (y/n): ")
    if Play_again.lower() != "y":
        break
