import random

def number_guessing_game():
  number_to_guess = random.randint(1, 100)
  attempts = 0

  print("=== Welcome to the number guessing game! ===")
  print("Try to guess the number I picked! It is between 1 and 100!")

  while True:
    user_guess = input("Enter your guess: ")
    try:
      user_guess = int(user_guess)
    except ValueError:
      print("Please enter a valid number.")
      continue

    attempts += 1

    if user_guess < number_to_guess:
      print("Too low!")
    elif user_guess > number_to_guess:
      print("Too high!")
    else: 
      print(f"Congrats you guessed the number on {attempts} attempts!")
      break


if __name__ == "__main__":
  number_guessing_game()