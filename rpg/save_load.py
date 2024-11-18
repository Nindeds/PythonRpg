import pickle

def save_game(game):
    with open("savefile.pkl", "wb") as f:
        pickle.dump(game, f)
    print("Game saved!")

def load_game():
    try:
        with open("savefile.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("No saved game found.")
        return None
