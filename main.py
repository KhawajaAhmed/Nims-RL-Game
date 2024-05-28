from game_logic import Game

class GameManager:
    def __init__(self, game=Game() ) -> None:
        self.game = game

    def play_game(self):
        while True:
            self.game.play_round()
            play_again = input("Do you want to play again? (yes/no): ").lower().startswith('y')
            if not play_again:
                break

if __name__ == "__main__":
    GameManager().play_game()
