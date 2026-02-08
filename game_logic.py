import random
import os

from ascii_art import STAGES


WORDS = ["python", "git", "github", "snowman", "meltdown"]

GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_random_word():
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    clear_screen()
    print(BLUE + "-" * 20 + RESET)
    print(YELLOW + STAGES[mistakes] + RESET)
    display_word = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
    print(f"Word: {GREEN}{display_word}{RESET}")
    print(f"Guessed: {RED}{', '.join(guessed_letters)}{RESET}")
    print(BLUE + "-" * 20 + RESET)


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    clear_screen()
    print(GREEN + "Welcome to Snowman Meltdown!" + RESET)

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print(RED + "Invalid input. Please enter a single alphabetical character." + RESET)
            continue

        if guess in guessed_letters:
            print(YELLOW + "You already guessed that letter!" + RESET)
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(GREEN + "Good guess!" + RESET)

            if all(letter in guessed_letters for letter in secret_word):
                display_game_state(mistakes, secret_word, guessed_letters)
                print(GREEN + "Congratulations! You saved the snowman!" + RESET)
                return
        else:
            mistakes += 1
            print(RED + "Wrong guess!" + RESET)

    display_game_state(mistakes, secret_word, guessed_letters)
    print(RED + f"Oh no! The snowman has melted. The word was: {secret_word}" + RESET)
