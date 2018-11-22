


class Board():

    def __init__(self):
        self.board = []
        self.cols = 7
        self.rows = 6
        self.null_cell = 0
        self.last_mov = (0,0)
        self.line = 4

    def clear_cell(self, row, col):
        if(self.is_cell_valid(row, col)):
            self.board[row][col] = self.null_cell

    def get_cols(self):
        return self.cols

    def get_rows(self):
        return self.rows

    def created_board(self):
        for row in range(self.rows):
            sub_row = []
            for col in range(self.cols):
                sub_row.append(self.null_cell)
            self.board.append(sub_row)
    
    def is_full(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if(self.board[row][col] == self.null_cell):
                    return False
        return True 

    def get_cells_symbol(self, symb):
        cells = [] 
        for r, row in enumerate(self.board):
            for c, col in enumerate(row):
                if(col == symb):
                    cells.append((r, c))
        return cells

    def get_last_mov(self):
        return self.last_mov

    def set_value_cell(self, col, symb):
        row_empty = self.get_empty_element(col)
        for row in enumerate(self.board):
            if(row[0] == row_empty):
                self.board[row[0]][col] = symb
                self.last_mov = (row[0], col)
                
    def get_empty_element(self, col):
        if((self.is_col_valid(col)) and (not(self.is_fill_column(col)))):
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

    def is_cell_valid(self, row, col):
        return (self.is_row_valid(row) and self.is_row_valid(col))

    def is_row_valid(self, row):
        return (0 <= row < self.rows)

    def is_col_valid(self, col):
        return (0 <= col < self.cols)

    def is_symbol_in(self, row, col, symb):
        if(self.is_cell_valid(row, col)):
            return self.board[row][col] == symb
        return False

    def winner(self, row, col, symb):
        mov = 1
        fwd = True
        bhd = False

        hzt = sum([self.win_hzt(row, col - mov, bhd, symb),
                   self.win_hzt(row, col + mov, fwd, symb)]) 
        vrt = self.win_vrt(row - mov, col, symb)
        d_back = sum([self.win_diag_slash(row - mov, col - mov, bhd, symb),
                       self.win_diag_slash(row + mov, col + mov, fwd, symb)])
        d_slash = sum([self.win_diag_back(row + mov, col - mov, bhd, symb),
                      self.win_diag_back(row - mov, col + mov, fwd, symb)])
        
        if(max([hzt, vrt, d_back, d_slash]) >= 3):
            return True
        return False

    def win_hzt(self, row, col, sum_value, symb):
        if(self.is_symbol_in(row, col, symb)):
            if(sum_value):
                col = col + 1
            else:
                col = col - 1
            return 1 + self.win_hzt(row, col, sum_value, symb)
        else:
            return 0

    def win_vrt(self, row, col, symb):
        if(self.is_symbol_in(row, col, symb)):
            return 1 + self.win_vrt(row - 1, col, symb)
        else:
            return 0

    def win_diag_slash(self, row, col, sum_value, symb):
        if(self.is_symbol_in(row, col, symb)):
            if(sum_value):
                row = row + 1
                col = col + 1
            else:
                row = row - 1
                col = col - 1
            return 1 + self.win_diag_slash(row, col, sum_value, symb)
        else:
            return 0

    def win_diag_back(self, row, col, sum_value, symb):
        if(self.is_symbol_in(row, col, symb)):
            if(sum_value):
                row = row - 1
                col = col + 1
            else:
                row = row + 1
                col = col - 1
            return 1 + self.win_diag_back(row, col, sum_value, symb)
        else:
            return 0

    def set_board(self, array):
        self.board = array