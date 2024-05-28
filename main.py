from q_learning import load_q_values
from game_logic import play_round
from config import EPSILON

def play_game():
    q_values = load_q_values()
    epsilon = EPSILON

    while True:
        epsilon = play_round(q_values, epsilon)
        play_again = input("Do you want to play again? (yes/no): ").lower().startswith('y')
        if not play_again:
            break

if __name__ == "__main__":
    play_game()
