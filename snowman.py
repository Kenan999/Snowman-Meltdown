from game_logic import play_game

if __name__ == "__main__":
    while True:
        play_game()
        replay = input("Do you want to play again? (y/n): ").lower()
        if replay != 'y':
            print("Thanks for playing!")
            break
