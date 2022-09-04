import os
import random

# Parse the int from user input
def inp(text):
    return int(input(text))


def game_loop():
    # Clears the screen
    os.system("cls")

    # Get player input and number to guess
    to_guess = random.randint(1, 100)
    p1guess = inp("Player 1 Guess: ")
    p2guess = inp("Player 2 Guess: ")

    # Find the distance of player guess to the number to guess
    p1diff = abs(to_guess - p1guess)
    p2diff = abs(to_guess - p2guess)

    print("\n")
    print(f"The number was {to_guess}.")

    # Compare differences to see who got the number closer
    if p1diff < p2diff:
        print("Player 1 guessed closer.")
    elif p1diff > p2diff:
        print("Player 2 guessed closer.")
    elif p1diff == p2diff:
        print("It's a tie!")

    # Ask the player if they want to play agian
    play_again()


def play_again():
    print("\n")
    ans = input("Play again? (y/n): ")

    # Restart the game loop if they want to play again, exit the script if no.
    if ans == "y":
        game_loop()
    elif ans == "n":
        quit()
    else:
        play_again()


# Initiate the game loop
game_loop()