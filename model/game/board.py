


class Board():

    def __init__(self):
        self.board = []
        self.cols = 7
        self.rows = 6
        self.null_cell = 0
        self.last_col = 0
        self.line = 4

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
        for r, row in enumerate(self.board):
            for c, col in enumerate(row):
                if(col == symbol):
                    cells.append((r, c))
        return cells


    def set_value_cell(self, col, symbol):
        row_empty = self.get_empty_element(col)
        print(row_empty)
        for row in enumerate(self.board):
            if(row[0] == row_empty):
                self.board[row[0]][col] = symbol

    def get_empty_element(self, col): #retorna la casilla más proxima donde no hay nada
        if((col>=0) and (col < self.cols) and (not(self.is_fill_column(col)))):
            col = self.get_column(col)
            for pos, cell in enumerate(col):
                if(cell == self.null_cell):
                    return pos
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

    def print_board(self):
        rows = self.rows
        while(rows>0):
            print(self.board[rows-1])
            rows = rows - 1

    def is_symbol_in(self, row, col, symbol):
        if(row < self.rows and col < self.cols and row >= 0 and col >= 0):
            return self.board[row][col] == symbol
        return False

    def winner(self, row, col, symbol):
        horizontal = self.winner_horizontal(row, col-1, False, symbol) + self.winner_horizontal(row, col+1, True, symbol)
        
        vertical = self.winner_vertical(row -1, col, symbol)

        diagonal_slash = self.winner_diagonal_slash(row-1, col-1, False, symbol) + self.winner_diagonal_slash(row+1, col+1, True, symbol)
        
        diagonal_back = self.winner_diagonal_back(row+1, col-1, False, symbol) + self.winner_diagonal_back(row-1, col+1, True, symbol)
        
        if((horizontal or vertical or diagonal_back or diagonal_slash) >= 4):
            return [True,symbol]
        else:
            return False
        


    def winner_horizontal(self, row, col, sum_value, symbol):
        if(self.is_symbol_in(row, col, symbol)):
            if(sum_value):
                col = col + 1
            else:
                col = col - 1
            return 1 + self.winner_horizontal(row, col, sum_value, symbol)
        else:
            return 0

    def winner_vertical(self, row, col, symbol):
        if(self.is_symbol_in(row, col, symbol)):
            return 1 + self.winner_vertical(row - 1, col, symbol)
        else:
            return 0

    def winner_diagonal_slash(self, row, col, sum_value, symbol):
        if(self.is_symbol_in(row, col, symbol)):
            if(sum_value):
                row = row + 1
                col = col + 1
            else:
                row = row - 1
                col = col - 1
            return 1 + self.winner_diagonal_slash(row, col, sum_value, symbol)
        else:
            return 0

    def winner_diagonal_back(self, row, col, sum_value, symbol):
        if(self.is_symbol_in(row, col, symbol)):
            if(sum_value):
                row = row - 1
                col = col + 1
            else:
                row = row + 1
                col = col - 1
            return 1 + self.winner_diagonal_back(row, col, sum_value, symbol)
        else:
            return 0



        



