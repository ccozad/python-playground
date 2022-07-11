from games.boards.grid_2d import Grid2D

class TicTacToeBoard(Grid2D):
    def __init__(self):
        super().__init__(3, 3, "?")
    
    def is_cats_game(self) -> bool:
        # TODO Implement
        return False
    
    def is_cell_open(self, row: int, column: int):
        if row >=0 and row < 3 and column >= 0 and column <= 3:
            return self.board[row * 3 + column] == "?"
        else:
            return False
    
    def make_move(self, turn: str, row: int, column: int):
        self.board[row * 3 + column] = turn
    
    def winner(self) -> None | str:
        # Row 0
        if self._row_has_winner(0):
            return self.board[0]
        # Row 1
        elif self._row_has_winner(1):
            return self.board[3]
        # Row 2
        elif self._row_has_winner(2):
            return self.board[6]
        # Column 0
        elif self._column_has_winner(0):
            return self.board[0]
        # Column 1
        elif self._column_has_winner(1):
            return self.board[1]
        # Column 2
        elif self._column_has_winner(2):
            return self.board[2]
        # Diagonal 0
        elif self._diagonal_has_winner(0):
            return self.board[0]
        # Diagonal 1
        elif self._diagonal_has_winner(1):
            return self.board[2]
        else:
            return None
    
    def _row_has_winner(self, row: int) -> bool:
        if row >= 0 and row < 3:
            row_start = row * 3
            return self.board[row_start] != "?" and self.board[row_start] == self.board[row_start + 1] and self.board[row_start] == self.board[row_start + 2]
        else:
            return False
    
    def _column_has_winner(self, column: int) -> bool:
        if column >= 0 and column < 3:
            return self.board[column] != "?" and self.board[column] == self.board[column + 3] and self.board[column] == self.board[column + 6]
        else:
            return False

    def _diagonal_has_winner(self, diagonal: int) -> bool:
        if diagonal == 0:
            return self.board[0] != "?" and self.board[0] == self.board[4] and self.board[0] == self.board[8]
        if diagonal == 1:
            return self.board[2] != "?" and self.board[2] == self.board[4] and self.board[2] == self.board[6]
        else:
            return False
    
    def __str__(self):
        board_state = []
        board_state.append(" {} | {} | {}".format(self.board[0], self.board[1], self.board[2])) 
        board_state.append("---+---+---")
        board_state.append(" {} | {} | {}".format(self.board[3], self.board[4], self.board[5]))
        board_state.append("---+---+---")
        board_state.append(" {} | {} | {}".format(self.board[6], self.board[7], self.board[8]))
        return "\n".join(board_state)