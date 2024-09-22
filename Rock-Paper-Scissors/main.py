import random

def game():
    choices = {"r": "rock", "p": "paper", "s": "scissors"}
    score_user = 0
    score_computer = 0

    print("Welcome to Rock-Paper-Scissors Game!")
    print("-------------------------------")

    while True:
        print("\nChoose your move:")
        print("R. Rock")
        print("P. Paper")
        print("S. Scissors")
        user_choice_abbr = input("Enter your choice (R/P/S): ").lower()
        while user_choice_abbr not in choices:
            user_choice_abbr = input("Invalid input. Enter your choice (R/P/S): ").lower()
        user_choice = choices[user_choice_abbr]

        computer_choice_abbr = random.choice(list(choices.keys()))
        computer_choice = choices[computer_choice_abbr]
        print(f"\nComputer chose {computer_choice}.\n")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
            score_user += 1
        else:
            print("Computer wins!")
            score_computer += 1

        print(f"Score - You: {score_user}, Computer: {score_computer}\n")

        print("Do you want to play again?")
        print("1. Yes")
        print("2. No")
        play_again_num = input("Enter your choice (1/2): ")
        while play_again_num not in ["1", "2"]:
            play_again_num = input("Invalid input. Enter your choice (1/2): ")
        if play_again_num == "2":
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    game()
