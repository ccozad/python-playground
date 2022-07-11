from typing import Any


class Grid2D:
    def __init__(self, width: int, height: int, initial_value):
        self.width = width
        self.height = height
        self.board = [initial_value] * (width * height)
    
    def get_cell(self, row: int, column: int) -> Any | None:
        if row >= 0 and row < self.height:
            if column >=0 and column < self.width:
                index = (row * self.width) + column
                return self.board[index]
            else:
                return None
        else:
            return None
    
    def set_cell(self, row: int, column: int, value: Any):
        if row >= 0 and row < self.height:
            if column >=0 and column < self.width:
                index = (row * self.width) + column
                self.board[index] = value
            else:
                return
        else:
            return
    
    def print(self,separator = ", "):
        for row in self.height:
            start = row * self.width
            print(separator.join(self.board[start, start + self.width]))
            

