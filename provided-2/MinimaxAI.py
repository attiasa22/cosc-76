import chess

class MinimaxAI():
    def __init__(self, depth):
        self.depth = depth

    def choose_move(self, board):
        return self.MinimaxSearch(board)

    def MinimaxSearch(self, board):
        value, move = self.MaxValue(board, 0)
        print(move)
        return move

    def MaxValue(self, board, current_depth):
        current_depth += 1
        if self.CutoffTest(board, current_depth):
            print("1")
            if board.is_checkmate():
                return -1, board.pop()
                #return -1, board.move_stack[-1]
            return 0, board.pop()

        moves = list(board.legal_moves)
        value = float("-inf")
        best_move = None
        
        for move in moves:
            board.push(move)
            print(board.move_stack)
            val2, move2 = self.MinValue(board, current_depth)
            if val2 > value:
                value = val2
                best_move = move2
            #movehistory=board.move_stack
        #board.pop()
        return value, best_move

    def MinValue(self, board, current_depth):
        current_depth += 1

        if self.CutoffTest(board, current_depth):
            print("1")
            if board.is_checkmate():
                return -1, board.pop()
            return 0, board.pop()

        moves = list(board.legal_moves)
        value = float("inf")
        best_move = None

        for move in moves:
            board.push(move)
            print(board.move_stack)
            val2, move2 = self.MaxValue(board, current_depth)
            if val2 < value:
                value = val2
                best_move = move2
            #movehistory=board.move_stack
        #board.pop()
        return value, best_move

    def CutoffTest(self, board, current_depth):

        return board.is_game_over() or current_depth == self.depth
            