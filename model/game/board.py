


class Board():

    def __init__(self):
        self.board = []
        self.cols = 7
        self.rows = 6
        self.null_cell = 0

    def created_board(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.board[row][col] = self.null_cell
    
    def is_full(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if(self.board[row][col] == self.null_cell):
                    return False
        return True 

    def get_cells_symbol(self, symbol):
        cells = []
        self.board.reverse()
        for r, row in enumerate(self.board):
            for c, col in enumerate(row):
                if(col == symbol):
                    cells.append((r, c))
        return cells


    def set_value_cell(self, col, symbol):
        pass

    def get_empty_element(self, col): #retorna la casilla más proxima donde no hay nada
        if((col <= self.cols) and (not(self.is_fill_column(col)))):
            col = self.get_column(col)
            col.reverse()
            for pos, cell in enumerate(col):
                if(cell == self.null_cell):
                    return self.rows - pos
        else:
            return -1

    def get_column(self, col):
        column = []
        for row in self.board:
            column.append(row[col])
        return column

    def is_fill_column(self, col):
        col = self.get_column(col)
        for cell in col:
            if(cell == self.null_cell):
                return False
        return True
