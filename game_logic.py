from q_learning import choose_action, update_q_values, load_q_values, save_q_values
from config import MAX_STICKS, MAX_MOVE, EPSILON, EPSILON_DECAY

def player_move(sticks_left):
    while True:
        try:
            action = int(input(f"Your turn. How many sticks do you want to take (1-{min(MAX_MOVE, sticks_left)})? "))
            if 1 <= action <= min(MAX_MOVE, sticks_left):
                return action
            else:
                print(f"Invalid move. Please choose a number between 1 and {min(MAX_MOVE, sticks_left)}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def computer_move(q_values, sticks_left, epsilon):
    action = choose_action(q_values, sticks_left, epsilon)
    print(f"Computer takes {action} sticks.")
    return action

def play_round(q_values, epsilon):
    move_history = []
    sticks_left = MAX_STICKS
    is_computer_turn = True

    while sticks_left > 0:
        print(f"Sticks left: {sticks_left}")

        if is_computer_turn:
            action = computer_move(q_values, sticks_left, epsilon)
        else:
            action = player_move(sticks_left)

        move_history.append((sticks_left, action, sticks_left - action, is_computer_turn))
        sticks_left -= action

        if sticks_left == 0:
            winner = "Computer" if is_computer_turn else "You"
            print(f"{winner} wins!")
            reward = 1 if winner == "Computer" else -1
            update_q_values(q_values, move_history, reward)
            save_q_values(q_values)
            return epsilon * EPSILON_DECAY

        is_computer_turn = not is_computer_turn
