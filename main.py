"""
University: University of Isfahan
Faculty: Mathematics and Statistics
Department: Computer Science
Course: Artificial Intelligence
Professor: Dr. Faria Nasiri Mofakham
TAs: MehrAzin Marzough, Mohammad Karimi, Anahita Honarmandian
Project: Adversarial Search in Othello (Minimax and Alpha-Beta Pruning)
"""

from agents.random_agent import RandomAgent
from agents.greedy_agent import GreedyAgent
from tournament import play_game
from agents.minimax_agent import MinimaxAgent
from agents.alphabeta_agent import AlphaBetaAgent


print(play_game(GreedyAgent(), RandomAgent()))
print(play_game(GreedyAgent(), AlphaBetaAgent()))
print(play_game(MinimaxAgent(depth=3), AlphaBetaAgent()))

