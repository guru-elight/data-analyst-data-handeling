import random

# Number Guessing Game

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print("You have 7 attempts to guess the number.\n")

# Generate a random number
secret_number = random.randint(1, 100)

# Set the maximum number of attempts
max_attempts = 7

# Game loop
for attempt in range(1, max_attempts + 1):

    print(f"Attempt {attempt} of {max_attempts}")

    # Get the user's guess
    guess = int(input("Enter your guess: "))

    # Check the user's guess
    if guess == secret_number:
        print("\nCongratulations!")
        print(f"You guessed the correct number: {secret_number}")
        print(f"You won in {attempt} attempt(s).")
        break

    elif guess < secret_number:
        print("Your guess is too low. Try again.\n")

    else:
        print("Your guess is too high. Try again.\n")

# Runs if the loop completes without a correct guess
else:
    print("\nGame Over!")
    print(f"The correct number was {secret_number}.")
    print("Better luck next time!")