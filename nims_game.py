import os
import random

MAX_STICKS = 20
MAX_MOVE = 4
Q_VALUES_FILE = "q_values.txt"
LEARNING_RATE = 0.1
DISCOUNT_FACTOR = 0.9
EPSILON = 0.2  # Decreased epsilon for more exploitation
epsilon_decay = 0.95

def load_q_values():
    if os.path.exists(Q_VALUES_FILE):
        with open(Q_VALUES_FILE, 'r') as f:
            q_values = [list(map(float, line.strip().split())) for line in f.readlines()]
    else:
        q_values = [[0.0] * MAX_STICKS for _ in range(MAX_MOVE)]
    return q_values

def save_q_values(q_values):
    with open(Q_VALUES_FILE, 'w') as f:
        for row in q_values:
            f.write(' '.join(map(str, row)) + '\n')

def choose_action(q_values, sticks_left):
    if random.random() < EPSILON:
        return random.randint(1, min(MAX_MOVE, sticks_left))
    else:
        return max(range(1, min(MAX_MOVE, sticks_left) + 1), key=lambda x: q_values[x - 1][sticks_left - 1])

def update_q_values(q_values, move_history, reward):
    for state, action, next_state, is_computer_turn in move_history:
        if is_computer_turn:
            q_values[action - 1][state - 1] += LEARNING_RATE * reward

def play_game():
    q_values = load_q_values()
    epsilon = EPSILON
    move_history = []
    sticks_left = MAX_STICKS
    is_computer_turn = True

    while sticks_left > 0:
        print(f"Sticks left: {sticks_left}")

        if is_computer_turn:
            action = choose_action(q_values, sticks_left)
            print(f"Computer takes {action} sticks.")
            sticks_left -= action
        else:
            while True:
                action = int(input("Your turn. How many sticks do you want to take (1-3)? "))
                if 1 <= action <= min(MAX_MOVE, sticks_left):
                    break
                else:
                    print("Invalid move. Please choose 1, 2, or 3 sticks.")
            sticks_left -= action

        move_history.append((sticks_left + action, action, sticks_left, is_computer_turn))

        if sticks_left == 0:
            winner = "Computer" if is_computer_turn else "You"
            print(f"{winner} wins!")
            if winner == "Computer":
                reward = 1
            else:
                reward = -1

        is_computer_turn = not is_computer_turn

    update_q_values(q_values, move_history, reward)

    save_q_values(q_values)
    epsilon *= epsilon_decay

def main():
    play_again = True
    while play_again:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower().startswith('y')

if __name__ == "__main__":
    main()
