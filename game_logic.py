import random

from ascii_art import STAGES


WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    print("-" * 20)
    print(STAGES[mistakes])
    display_word = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
    print(f"Word: {display_word}")
    print(f"Guessed: {', '.join(guessed_letters)}")
    print("-" * 20)


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Good guess!")

            if all(letter in guessed_letters for letter in secret_word):
                display_game_state(mistakes, secret_word, guessed_letters)
                print("Congratulations! You saved the snowman!")
                return
        else:
            mistakes += 1
            print("Wrong guess!")

    display_game_state(mistakes, secret_word, guessed_letters)
    print(f"Oh no! The snowman has melted. The word was: {secret_word}")
