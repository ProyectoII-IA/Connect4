# Package: model.game
# Description: structure of board

# Artificial Intelligence, II Semester 2018
# Project: Connect 4
# Author : Jonathan Martinez C.
# E-mail: jonathan.gerad@hotmail.com
# Version: 0.0.0

# IMPORT SECTION


class Board():

    def __init__(self):
        self.board = []          # array of the game
        self.cols = 7            # number of cols of board
        self.rows = 6            # number of rows of board
        self.null_cell = 0       # define a symbol for a empty cell
        self.last_mov = (0, 0)   # save the position of last symbol insert
        self.line = 4            # define the size of the line to search

    # Methods-------------------------
    # @Method: CLEAR_CELL
    # @Description: Put the null_cell symbol in specific pair (row, col)
    def clear_cell(self, row, col):
        if(self.is_cell_valid(row, col)):
            self.board[row][col] = self.null_cell

    # Methods-------------------------
    # @Method: GET_COLS
    # @Description: Return the number of cols of the board
    def get_cols(self):
        return self.cols

    # Methods-------------------------
    # @Method: GET_ROWS
    # @Description: Return the number of rows og the board
    def get_rows(self):
        return self.rows

    # Methods-------------------------
    # @Method: CREATED_BOARD
    # @Description: Put in all cells the null_cell symbol
    def created_board(self):
        for row in range(self.rows):
            sub_row = []
            for col in range(self.cols):
                sub_row.append(self.null_cell)
            self.board.append(sub_row)

    # Methods-------------------------
    # @Method: IS_FULL
    # @Description: Ask if one cell of board contains the null_cell symbol
    def is_full(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if(self.board[row][col] == self.null_cell):
                    return False
        return True

    # Methods-------------------------
    # @Method: GET_CELLS_SYMBOL
    # @Description: Return all cells (row,col) that contains a specific symbol
    def get_cells_symbol(self, symb):
        cells = []
        for r, row in enumerate(self.board):
            for c, col in enumerate(row):
                if(col == symb):
                    cells.append((r, c))
        return cells

    # Methods-------------------------
    # @Method: GET_LAST_MOV
    # @Description: Return the pair (row,col) of the last insert in board
    def get_last_mov(self):
        return self.last_mov

    # Methods-------------------------
    # @Method: SET_VALUE_CELL
    # @Description: Put in specific cell (row, col) a symbol
    def set_value_cell(self, col, symb):
        if(self.is_col_valid(col)):
            row_empty = self.get_empty_element(col)
            for row in enumerate(self.board):
                if(row[0] == row_empty):
                    self.board[row[0]][col] = symb
                    self.last_mov = (row[0], col)

    # Methods-------------------------
    # @Method: GET_EMPTY_ELEMENT
    # @Description: Return the next row to be inserted in a column
    def get_empty_element(self, col):
        if((self.is_col_valid(col)) and (not(self.is_fill_column(col)))):
            col = self.get_column(col)
            for pos, cell in enumerate(col):
                if(cell == self.null_cell):
                    return pos
        else:
            return -1

    # Methods-------------------------
    # @Method: GET_COLUMN
    # @Description: Return a specific column of the board
    def get_column(self, col):
        column = []
        if(self.is_col_valid(col)):
            for row in self.board:
                column.append(row[col])
        return column

    # Methods-------------------------
    # @Method: IS_FILL_COLUMN
    # @Description: Ask if a column not contain null_cell symbol
    def is_fill_column(self, col):
        if(self.is_col_valid(col)):
            col = self.get_column(col)
            for cell in col:
                if(cell == self.null_cell):
                    return False
            return True
        else:
            return False

    # Methods-------------------------
    # @Method: PRINT_BOARD
    # @Description: Print the board upside down
    def print_board(self):
        rows = self.rows
        while(rows > 0):
            print(self.board[rows - 1])
            rows = rows - 1

    # Methods-------------------------
    # @Method: IS_CELL_VALID
    # @Description: Ask if a cell (row,col) is valid
    def is_cell_valid(self, row, col):
        return (self.is_row_valid(row) and self.is_col_valid(col))

    # Methods-------------------------
    # @Method: IS_ROW_VALID
    # @Description: Ask if a row in the range of dimensions of board
    def is_row_valid(self, row):
        return (0 <= row < self.rows)

    # Methods-------------------------
    # @Method: IS_COL_VALID
    # @Description: Ask if a col in the range of dimensions of board
    def is_col_valid(self, col):
        return (0 <= col < self.cols)

    # Methods-------------------------
    # @Method: IS_SYMBOL_IN
    # @Description: Ask if a symbol is in a specific cell
    def is_symbol_in(self, row, col, symb):
        if(self.is_cell_valid(row, col)):
            return self.board[row][col] == symb
        return False

    # Methods-------------------------
    # @Method: WINNER
    # @Description: From a specific cell, ask if a line of 4 equal symbols
    #               is found in all directions
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

    # Methods-------------------------
    # @Method: WIN_HZT
    # @Description: From a specific cell, ask if a line of 4 equal symbols
    #               is found in horizontal direction
    def win_hzt(self, row, col, sum_value, symb):
        if(self.is_symbol_in(row, col, symb)):
            if(sum_value):
                col = col + 1
            else:
                col = col - 1
            return 1 + self.win_hzt(row, col, sum_value, symb)
        else:
            return 0

    # Methods-------------------------
    # @Method: WIN_VRT
    # @Description: From a specific cell, ask if a line of 4 equal symbols
    #               is found in vertical direction
    def win_vrt(self, row, col, symb):
        if(self.is_symbol_in(row, col, symb)):
            return 1 + self.win_vrt(row - 1, col, symb)
        else:
            return 0

    # Methods-------------------------
    # @Method: WIN_DIAG_SLASH
    # @Description: From a specific cell, ask if a line of 4 equal symbols
    #               is found in diagonal-slash direction
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

    # Methods-------------------------
    # @Method: WIN_DIAG_BACK
    # @Description: From a specific cell, ask if a line of 4 equal symbols
    #               is found in diagonal-back direction
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

    # Methods-------------------------
    # @Method: SET_BOARD
    # @Description: Set the board (array) to the class
    def set_board(self, array):
        self.board = array
