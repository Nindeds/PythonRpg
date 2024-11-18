from gameplay import Game

def main():
    while True:
        print("\nMain Menu:")
        print("1. New Game\n2. Load Game\n3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            print("Starting new game...")
            game = Game() 
            game.start_game()
        elif choice == "2":
            print("Loading game (placeholder)...")
            loaded_game = game.load_game() if 'game' in locals() else None
            if loaded_game:
                game = loaded_game
                game.game_loop()
            else:
                print("No game to load.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
