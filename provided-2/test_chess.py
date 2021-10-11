# pip3 install python-chess


import chess
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from IterativeAI import IterativeAI
from ChessGame import ChessGame


import sys


player1 = HumanPlayer()
player2 = RandomAI()
player3 = MinimaxAI(depth = 4)
player4 = AlphaBetaAI(depth = 4)
player5 = IterativeAI(player4, 5)

game = ChessGame(player1, player5)

while not game.is_game_over():
    print(game)
    game.make_move()


#print(hash(str(game.board)))
