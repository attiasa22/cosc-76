import chess
from math import inf


class AlphaBetaAI():
    def __init__(self, depth):
        self.depth = depth
        self.nodes_traveled = 0 
        #906 nodes travelled d2d4 first move, depth 3
    def choose_move(self, board):   
        value, move = self.Search(board)
        return move

    def CutoffTest(self, board, current_depth):
            return board.is_game_over() or current_depth > self.depth
    
    def Search(self, board):
        value, move = self.MaxValue(board, 0, float("-inf"), float("inf"))
        print(self.nodes_traveled)
        print(value)
        return value, move

    def MaxValue(self, board, current_depth, alpha, beta):
        current_depth += 1
        self.nodes_traveled+=1 
        if self.CutoffTest(board, current_depth):
            if board.is_checkmate():
                return float("-inf"), board.peek()
            return self.heuristic(board), board.peek()

        moves = list(board.legal_moves)
        moves.sort(key = lambda move: self.heuristic(board, move = move))
        value = float("-inf")
        best_move = None
        value = alpha

        for move in moves:
            board.push(move)
            val2, move2 = self.MinValue(board, current_depth, value, beta )
            board.pop()
            if val2 > value:
                
                value = val2
                best_move = move

            if val2 >= beta:
                return value, move
                
        return value, best_move

    def MinValue(self, board, current_depth, alpha, beta):
        current_depth += 1
        self.nodes_traveled+=1 
        if self.CutoffTest(board, current_depth):
            if board.is_checkmate():
                return float("inf"), board.peek()
            return self.heuristic(board), board.peek()

        moves = list(board.legal_moves)
        moves.sort(key = lambda move: self.heuristic(board, move = move))
        value = beta
        best_move = None

        for move in moves:
            board.push(move)
            val2, move2 = self.MaxValue(board, current_depth, alpha, value)
            board.pop()
            if val2 < value:
                value = val2
                best_move = move

            if val2 <= alpha:
                 return value, best_move

        return value, best_move

    def heuristic(self, board, move = None):
        piece_scores = {1: 1, 2: 3, 3: 3, 4: 5, 5: 9, 6: 0}
        score = 0
        if move != None:
            board.push(move)

        pieces= board.piece_map()

        for piece in pieces.values():
            if piece.color:
                score-=piece_scores[piece.piece_type]
            else:
                score+=piece_scores[piece.piece_type]
        
        if move != None:
            board.pop()

        return score

        