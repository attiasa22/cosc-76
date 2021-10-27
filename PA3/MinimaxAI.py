import chess

class MinimaxAI():
    def __init__(self, depth):
        self.depth = depth
        self.nodes_traveled = 0 
    def choose_move(self, board):   
        value, move = self.Search(board)
        return move

    def CutoffTest(self, board, current_depth):
            return board.is_game_over() or current_depth > self.depth
    
    def Search(self, board):
        value, move = self.MaxValue(board, 0)
        print(self.nodes_traveled)
        return value, move

    def MaxValue(self, board, current_depth):
        current_depth += 1
        self.nodes_traveled += 1 
        if self.CutoffTest(board, current_depth):
            if board.is_checkmate():
                return float("-inf"), board.peek()
            return self.heuristic(board), board.peek()
        moves = list(board.legal_moves)
        value = float("-inf")
        best_move = None
        
        for move in moves:
            board.push(move)
            val2, move2 = self.MinValue(board, current_depth)
            board.pop()
            if val2 > value:
                value = val2
                best_move = move

        return value, best_move

    def MinValue(self, board, current_depth):
        current_depth += 1
        self.nodes_traveled += 1 

        if self.CutoffTest(board, current_depth):
            if board.is_checkmate():
                return float("inf"), board.peek()
            return self.heuristic(board), board.peek()

        moves = list(board.legal_moves)
        value = float("inf")
        best_move = None

        for move in moves:
            board.push(move)
            val2, move2 = self.MaxValue(board, current_depth)
            board.pop()
            if val2 < value:
                value = val2
                best_move = move
            #movehistory=board.move_stack
        return value, best_move

    def heuristic(self, board):
        piece_scores = {1: 1, 2: 3, 3: 3, 4: 5, 5: 9, 6: 0}
        score = 0
        pieces= board.piece_map()
        for piece in pieces.values():
            if piece.color:
                score-=piece_scores[piece.piece_type]
            else:
                score+=piece_scores[piece.piece_type]
        return score
        
        


