from game_logic import play_game


def main():
    while True:
        play_game()
        replay = input("\nDo you want to play again? (y/n): ").lower()
        if replay != 'y':
            print("\033[94mThanks for playing!\033[0m")
            break


if __name__ == "__main__":
    main()
