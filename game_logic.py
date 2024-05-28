from q_learning import QLearningAgent
from config import EPSILON_DECAY


class Game:
    def __init__(self, agent = QLearningAgent()) -> None:
        self.agent = agent
        
    def player_move(self,sticks_left):
        while True:
            try:
                action = int(input(f"Your turn. How many sticks do you want to take (1-{min(self.agent.max_move, sticks_left)})? "))
                if 1 <= action <= min(self.agent.max_move, sticks_left):
                    return action
                else:
                    print(f"Invalid move. Please choose a number between 1 and {min(self.agent.max_move, sticks_left)}.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def computer_move(self, sticks_left):
        action = self.agent.choose_action(sticks_left)
        print(f"Computer takes {action} sticks.")
        return action

    def play_round(self):
        move_history = []
        sticks_left = self.agent.max_sticks
        is_computer_turn = True

        while sticks_left > 0:
            print(f"Sticks left: {sticks_left}")

            if is_computer_turn:
                action = self.computer_move(sticks_left)
            else:
                action = self.player_move(sticks_left)

            move_history.append((sticks_left, action, sticks_left - action, is_computer_turn))
            sticks_left -= action

            if sticks_left == 0:
                winner = "Computer" if is_computer_turn else "You"
                print(f"{winner} wins!")
                reward = 1 if winner == "Computer" else -1
                self.agent.update_q_values(move_history, reward)
                self.agent.save_q_values()
                self.agent.explore_decay()
                
            is_computer_turn = not is_computer_turn
