import random


def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "user"
    else:
        return "computer"


def play_game(best_of):
    rounds_needed = (best_of // 2) + 1
    user_wins = 0
    computer_wins = 0
    ties = 0

    print(f"\n=== Rock, Paper, Scissors: Best of {best_of} ===")

    while user_wins < rounds_needed and computer_wins < rounds_needed:
        user_choice = input("\nChoose rock, paper, or scissors: ").lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        if winner == "user":
            user_wins += 1
            print("You win this round!")
        elif winner == "computer":
            computer_wins += 1
            print("Computer wins this round!")
        else:
            ties += 1
            print("It's a tie!")

        print(f"Score: You {user_wins} - {computer_wins} Computer (Ties: {ties})")

        if user_wins > computer_wins:
            print("\nCongratulations! You are the overall winner!")


def main():
    """Main function to run the game."""
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        best_of = input("Do you want to play best of 3 or best of 5? (Enter 3 or 5): ")
        if best_of in ["3", "5"]:
            play_game(int(best_of))
            break
        else:
            print("Invalid input! Please enter 3 or 5.")


if __name__ == "__main__":
    main()
