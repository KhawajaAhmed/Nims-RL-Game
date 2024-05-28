import os
import random
from config import MAX_MOVE, MAX_STICKS, Q_VALUES_FILE, LEARNING_RATE, EPSILON

class QLearningAgent:

    def __init__(self,max_move=MAX_MOVE, max_sticks=MAX_STICKS, q_values_file=Q_VALUES_FILE, learning_rate=LEARNING_RATE, epsilon=EPSILON) -> None:
        self.max_move = max_move
        self.max_sticks = max_sticks
        self.q_values_file = q_values_file
        self.learning_rate = learning_rate
        self.epsilon = epsilon
        self.q_values = self.load_q_values()

    def load_q_values(self):
        if os.path.exists(self.q_values_file):
            with open(self.q_values_file, 'r') as f:
                q_values = [list(map(float, line.strip().split())) for line in f.readlines()]
        else:
            q_values = [[0.0] * MAX_STICKS for _ in range(MAX_MOVE)]
        return q_values

    def save_q_values(self):
        with open(self.q_values_file, 'w') as f:
            for row in self.q_values:
                f.write(' '.join(map(str, row)) + '\n')

    def choose_action(self, sticks_left):
        if random.random() < self.epsilon:
            return random.randint(1, min(self.max_move, sticks_left))
        else:
            return max(range(1, min(self.max_move, sticks_left) + 1), key=lambda x: self.q_values[x - 1][sticks_left - 1])

    def update_q_values(self,move_history, reward):
        for state, action, next_state, is_computer_turn in move_history:
            if is_computer_turn:
                self.q_values[action - 1][state - 1] += self.learning_rate * reward
