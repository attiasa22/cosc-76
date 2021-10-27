import chess
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI

class IterativeAI():

    def __init__(self, method, depth):
        self.depth = depth
        self.method = method

    def choose_move(self, board): 
        best_move = None
        best_value = float("-inf")

        for i in range(self.depth):
            self.method.depth = i
            value, move = self.method.Search(board)

            print(move)

            if value > best_value:
                best_move = move
                best_value = value

        
        return move

