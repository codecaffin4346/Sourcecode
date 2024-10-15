import random

def guess_the_number():
    print("Welcome to the 'Guess the Number' game!")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Set the number of attempts
    attempts = 7
    
    print(f"\nI have selected a number between 1 and 100. You have {attempts} attempts to guess it!")

    for attempt in range(1, attempts + 1):
        # Get player's guess
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        
        # Check the player's guess
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} correctly in {attempt} attempts!")
            break
    else:
        print(f"Sorry! You've used all {attempts} attempts. The correct number was {number_to_guess}.")

# Run the game
guess_the_number()
