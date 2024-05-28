Description:

Stick Game
This is a simple command-line game where you play against the computer to remove sticks from a pile. The player and the computer take turns removing 1 to 4 sticks from the pile until there are no sticks left. The player who takes the last stick wins.

How to Play
At each turn, you'll be prompted to choose the number of sticks to remove.
You can remove 1 to 4 sticks per turn.
The computer will then take its turn automatically.
The game continues until there are no sticks left.
The player who takes the last stick wins.

Files
main.py: Entry point of the game. Orchestrates the game flow.
config.py: Contains configuration constants used throughout the game.
q_learning.py: Handles Q-learning functionality for the computer player.
game_logic.py: Implements the game logic, including player moves and determining the winner.
q_values.txt: Stores Q-values used by the computer player for decision-making.