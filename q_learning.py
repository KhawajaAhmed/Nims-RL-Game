import os
import random
from config import MAX_MOVE, MAX_STICKS, Q_VALUES_FILE, LEARNING_RATE, EPSILON

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

def choose_action(q_values, sticks_left, epsilon):
    if random.random() < epsilon:
        return random.randint(1, min(MAX_MOVE, sticks_left))
    else:
        return max(range(1, min(MAX_MOVE, sticks_left) + 1), key=lambda x: q_values[x - 1][sticks_left - 1])

def update_q_values(q_values, move_history, reward):
    for state, action, next_state, is_computer_turn in move_history:
        if is_computer_turn:
            q_values[action - 1][state - 1] += LEARNING_RATE * reward
