# Package: tests.model_tests.game
# Description: tests of structure board

# Artificial Intelligence, II Semester 2018
# Project: Connect 4
# Author : Jonathan Martinez C.
# E-mail: jonathan.gerad@hotmail.com
# Version: 0.0.0

# IMPORT SECTION
from model.game.board import Board

# ------ TEST_CLEAR_CELL ------

def test_clear_cell_exist():
    """ Check that cell is clear correctly
    """

    array = [[1,1,1,2,1,0,0],
             [2,1,1,1,2,0,0],
             [0,0,1,1,2,0,0],
             [0,0,2,2,1,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]]
    board = Board()
    board.set_board(array)
    position_test = [0,0] # at the begin of array

    # update position in array to compare
    array[position_test[0]][position_test[1]] = board.null_cell
    board.clear_cell(position_test[0], position_test[0])
    assert(array == board.board)

def test_clear_cell_not_exist():
    """ Check that the board not change with value out the range
    """
    
    array = [[1,1,1,2,1,0,0],
             [2,1,1,1,2,0,0],
             [0,0,1,1,2,0,0],
             [0,0,2,2,1,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]]
    board = Board()
    board.set_board(array)
    position_test = [9,9] # out the range of board

    # try to clear cell
    board.clear_cell(position_test[0], position_test[0])
    assert(array == board.board)


# ------ TEST_CREATED_BOARD ------

def test_created_board():
    """ Check that the board is created and all the cells
        contains the null_cell of the board 
    """

    array = [[0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]]
    board = Board()
    board.created_board()

    # compare the array with the new board created
    assert(array == board.board)


# ------ TEST_IS_FULL ------

def test_is_full_true():
    """ Check that the board is really full 
    """

    array = [[1,1,2,2,2,1,1],
             [2,1,1,1,2,1,2],
             [1,1,2,1,1,1,2],
             [2,2,1,2,2,2,1],
             [1,1,2,2,1,1,2],
             [2,1,2,1,1,2,2]]
    board = Board()
    board.board = array
    
    assert(board.is_full() == True)         

def test_is_full_false():
    """ Check that the board is not really full 
    """

    array = [[1,1,2,0,0,1,1],
             [2,1,1,1,2,1,2],
             [1,1,2,1,1,1,2],
             [2,2,1,2,2,2,1],
             [1,1,2,2,1,1,2],
             [2,1,2,1,1,2,2]]
    board = Board()
    board.board = array

    assert(board.is_full() == False)   


# ------ TEST_IS_FULL_COLUMN ------

def test_is_full_column_true():
    """ Check that the column of board is really full 
    """

    array = [[0,1,2,0,1,1,0],
             [0,1,1,0,2,1,0],
             [0,1,2,1,1,1,0],
             [2,2,1,2,2,2,0],
             [1,1,2,2,1,1,0],
             [2,1,2,1,1,2,0]]
    board = Board()
    board.board = array

    assert(board.is_fill_column(1) == True)
    assert(board.is_fill_column(2) == True)
    assert(board.is_fill_column(4) == True)
    assert(board.is_fill_column(5) == True)

def test_is_full_column_false():
    """ Check that the column of board is not really full 
    """

    array = [[0,1,2,0,1,1,0],
             [0,1,1,0,2,1,0],
             [0,1,2,1,1,1,0],
             [2,2,1,2,2,2,0],
             [1,1,2,2,1,1,0],
             [2,1,2,1,1,2,0]]
    board = Board()
    board.board = array

    # compare cases with valid column
    assert(board.is_fill_column(0) == False)
    assert(board.is_fill_column(3) == False)
    assert(board.is_fill_column(6) == False)

    # compare cases with column out the range
    assert(board.is_fill_column(9) == False)


# ------ TEST_IS_CELL_VALID ------

def test_is_cell_valid_true():
    """ Check that the cell (i,j) of board is valid 
    """

    # default value of dimensions is (6x7)
    board = Board()
    pos = [[1,2],[3,4],[0,1],[0,5]]

    assert(board.is_cell_valid(pos[0][0], pos[0][1]) == True)
    assert(board.is_cell_valid(pos[1][0], pos[1][1]) == True)
    assert(board.is_cell_valid(pos[2][0], pos[2][1]) == True)
    assert(board.is_cell_valid(pos[3][0], pos[3][1]) == True)
    

def test_is_cell_valid_false():
    """ Check that the cell (i,j) of board is not valid 
    """
    
    # default value of dimensions is (6x7)
    board = Board()
    pos = [[0,-2],[9,11],[0,7],[1,8]]

    assert(board.is_cell_valid(pos[0][0], pos[0][1]) == False)
    assert(board.is_cell_valid(pos[1][0], pos[1][1]) == False)
    assert(board.is_cell_valid(pos[2][0], pos[2][1]) == False)
    assert(board.is_cell_valid(pos[3][0], pos[3][1]) == False)
    

# ------ TEST_IS_COL_VALID ------

def test_is_col_valid_true():
    """ Check that the col of board is valid 
    """

    # default value of dimensions is (6x7)
    board = Board()
    pos = [0,1,2,3,4,5,6]

    assert(board.is_col_valid(pos[0]) == True)
    assert(board.is_col_valid(pos[1]) == True)
    assert(board.is_col_valid(pos[2]) == True)
    assert(board.is_col_valid(pos[3]) == True)
    assert(board.is_col_valid(pos[4]) == True)
    assert(board.is_col_valid(pos[5]) == True)
    assert(board.is_col_valid(pos[6]) == True)

def test_is_col_valid_false():
    """ Check that the col of board is not valid 
    """

    # default value of dimensions is (6x7)
    board = Board()
    pos = [-1,7,8,9,-2,-4,10]

    assert(board.is_col_valid(pos[0]) == False)
    assert(board.is_col_valid(pos[1]) == False)
    assert(board.is_col_valid(pos[2]) == False)
    assert(board.is_col_valid(pos[3]) == False)
    assert(board.is_col_valid(pos[4]) == False)
    assert(board.is_col_valid(pos[5]) == False)
    assert(board.is_col_valid(pos[6]) == False)
    

# ------ TEST_IS_SYMBOL_IN ------

def test_is_symbol_in_true():
    """ Check that one symbol is put in row, col valid of the board 
    """

    array = [[0,1,2,0,1,1,0],
             [0,1,1,0,2,1,0],
             [0,1,2,1,1,1,0],
             [2,2,1,2,2,2,0],
             [1,1,2,2,1,1,0],
             [2,1,2,1,1,2,0]]
    board = Board()
    board.board = array
    pos = [[0,1],[5,5],[2,2],[3,3],[4,4],[0,4]]
    symb_a = 1
    symb_b = 2
    
    assert(board.is_symbol_in(pos[0][0], pos[0][1], symb_a) == True)
    assert(board.is_symbol_in(pos[1][0], pos[1][1], symb_b) == True)
    assert(board.is_symbol_in(pos[2][0], pos[2][1], symb_b) == True)
    assert(board.is_symbol_in(pos[3][0], pos[3][1], symb_b) == True)
    assert(board.is_symbol_in(pos[4][0], pos[4][1], symb_a) == True)
    assert(board.is_symbol_in(pos[5][0], pos[5][1], symb_a) == True)

def test_is_symbol_in_false():
    """ Check that one symbol is not put in row, col valid of the board 
    """

    array = [[0,1,2,0,1,1,0],
             [0,1,1,0,2,1,0],
             [0,1,2,1,1,1,0],
             [2,2,1,2,2,2,0],
             [1,1,2,2,1,1,0],
             [2,1,2,1,1,2,0]]
    board = Board()
    board.board = array
    pos = [[0,1],[5,5],[2,2],[3,3],[4,4],[0,4]]
    symb_a = 1
    symb_b = 2
    symb_c = 3
    
    assert(board.is_symbol_in(pos[0][0], pos[0][1], symb_c) == False)
    assert(board.is_symbol_in(pos[1][0], pos[1][1], symb_a) == False)
    assert(board.is_symbol_in(pos[2][0], pos[2][1], symb_c) == False)
    assert(board.is_symbol_in(pos[3][0], pos[3][1], symb_a) == False)
    assert(board.is_symbol_in(pos[4][0], pos[4][1], symb_c) == False)
    assert(board.is_symbol_in(pos[5][0], pos[5][1], symb_b) == False)


# ------ TEST_GET_COLS ------

def test_get_cols():
    """ Check that the number of cols is exactly 7 
    """

    # default value of cols is 7
    board = Board()
    cols = 7

    assert(board.get_cols() == cols)


# ------ TEST_GET_ROWS ------

def test_get_rows():
    """ Check that the number of rows is exactly 6 
    """

    # default value of rows is 6
    board = Board()
    rows = 6

    assert(board.get_rows() == rows)


# ------ TEST_GET_CELLS_SYMBOL ------

def test_get_cells_symbol_one_or_more():
    """ Check there is at least one or more match 
    """

    array = [[0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,1,0,0,0,0,0],
             [2,2,1,0,2,0,0],
             [1,1,2,2,1,1,0],
             [2,1,2,1,1,2,2]]
    board = Board()
    board.board = array
    symb_a = 1
    symb_b = 2
    # positions of the symbol 1 and 2
    pos_a = [(2,1),(3,2),(4,0),(4,1),(4,4),(4,5),(5,1),(5,3),(5,4)]
    pos_b = [(3,0),(3,1),(3,4),(4,2),(4,3),(5,0),(5,2),(5,5),(5,6)]

    # compare all cells of each symbol with the respective array 
    assert(board.get_cells_symbol(symb_a) == pos_a)
    assert(board.get_cells_symbol(symb_b) == pos_b)

def test_get_cells_symbol_zero():
    """ Check there is zero match 
    """

    array = [[0,1,1,0,1,1,0],
             [0,1,1,0,1,1,0],
             [0,1,1,0,1,1,0],
             [0,1,1,0,1,1,0],
             [1,1,1,0,1,1,0],
             [1,1,1,1,1,1,0]]
    board = Board()
    board.board = array
    symb_a = 3
    symb_b = 2
    # positions of the symbol 3 and 2
    pos_a = []
    pos_b = []

    # compare all cells of each symbol with the respective array 
    assert(board.get_cells_symbol(symb_a) == pos_a)
    assert(board.get_cells_symbol(symb_b) == pos_b)


# ------ TEST_GET_COLUMN ------  

def test_get_column_exist():
    """ Check there is zero match 
    """

    array = [[0,1,1,0,1,1,0],
             [0,1,1,0,1,1,0],
             [0,1,1,0,1,1,0],
             [0,1,1,0,1,1,0],
             [1,1,1,0,1,1,0],
             [1,1,1,1,1,1,0]]
    board = Board()
    board.board = array
    col_0 = [0,0,0,0,1,1]
    col_1 = [1,1,1,1,1,1]
    col_2 = [1,1,1,1,1,1]
    col_3 = [0,0,0,0,0,1]
    col_4 = [1,1,1,1,1,1]
    col_5 = [1,1,1,1,1,1]
    col_6 = [0,0,0,0,0,0]

    assert(board.get_column(0) == col_0)
    assert(board.get_column(1) == col_1)
    assert(board.get_column(2) == col_2)
    assert(board.get_column(3) == col_3)
    assert(board.get_column(4) == col_4)
    assert(board.get_column(5) == col_5)
    assert(board.get_column(6) == col_6)

def test_get_column_not_exist():
    """ Check there is zero match 
    """
    array = [[0,1,1,0,1,1,0],
             [0,1,1,0,1,1,0],
             [0,1,1,0,1,1,0],
             [0,1,1,0,1,1,0],
             [1,1,1,0,1,1,0],
             [1,1,1,1,1,1,0]]
    board = Board()
    board.board = array
    col_7 = []
    col_8 = []
    col_20 = []

    assert(board.get_column(7) == col_7)
    assert(board.get_column(8) == col_8)
    assert(board.get_column(20) == col_20)


# ------ TEST_GET_EMPTY_ELEMENT ------ 
def test_get_empty_element_available_cell():
    """ Check that all the columns are available to insert
    """

    array = [[1,1,1,1,1,1,0],
             [1,1,1,0,1,1,0],
             [0,1,1,0,1,0,0],
             [0,1,0,0,1,0,0],
             [0,1,0,0,0,0,0],
             [0,0,0,0,0,0,0]]
    board = Board()
    board.board = array
    col_0 = 2 
    col_1 = 5
    col_2 = 3
    col_3 = 1
    col_4 = 4
    col_5 = 2
    col_6 = 0

    # compare with all columns of the board
    assert(board.get_empty_element(0) == col_0)
    assert(board.get_empty_element(1) == col_1)
    assert(board.get_empty_element(2) == col_2)
    assert(board.get_empty_element(3) == col_3)
    assert(board.get_empty_element(4) == col_4)
    assert(board.get_empty_element(5) == col_5)
    assert(board.get_empty_element(6) == col_6)

def test_get_empty_element_not_available_cell():
    """ Check that one o more columns are not available to insert 
    """

    array = [[1,1,1,1,1,1,0],
             [1,1,1,0,1,1,0],
             [0,1,1,0,1,1,0],
             [0,1,0,0,1,1,0],
             [0,1,0,0,1,1,0],
             [0,1,0,0,1,1,0]]
    board = Board()
    board.board = array
    col_1 = -1
    col_4 = -1
    col_5 = -1
    col_7 = -1
    col_8 = -1

    # compare with columns that not are available to insert
    assert(board.get_empty_element(1) == col_1)
    assert(board.get_empty_element(4) == col_4)
    assert(board.get_empty_element(5) == col_5)
    assert(board.get_empty_element(7) == col_7)
    assert(board.get_empty_element(8) == col_8)


# ------ TEST_SET_VALUE_CELL ------ 

def test_set_value_cell_correct_col():
    """ Check that a symbol is set correctly in column 
    """

    array = [[1,1,1,1,1,1,0],
             [1,1,1,0,1,1,0],
             [0,1,1,0,1,1,0],
             [0,1,0,0,1,1,0],
             [0,1,0,0,1,1,0],
             [0,1,0,0,1,1,0]]
    board = Board()
    board.board = array
    # insert value in col 0
    board.set_value_cell(0,1)
    # insert value in col 2
    board.set_value_cell(2,1)

    # verify that the cols are update
    assert(board.board == array)

def test_set_value_cell_wrong_col():
    """Check that the board no change with a wrong column 
    """

    array = [[1,1,1,1,1,1,0],
             [1,1,1,0,1,1,0],
             [0,1,1,0,1,1,0],
             [0,1,0,0,1,1,0],
             [0,1,0,0,1,1,0],
             [0,1,0,0,1,1,0]]
    board = Board()
    board.board = array
    # insert value in col 10
    board.set_value_cell(10,1)
    # insert value in col -1
    board.set_value_cell(-1,1)

    # verify that the cols are not update
    assert(board.board == array)


# ------ TEST_LAST_MOV ------ 

def test_last_mov():
    """Check that the board save correctly the last position
       of last movement 
    """

    array = [[1,1,1,1,1,1,0],
             [1,1,1,0,1,1,0],
             [0,1,1,0,1,1,0],
             [0,1,0,0,1,1,0],
             [0,1,0,0,1,1,0],
             [0,1,0,0,1,1,0]]
    board = Board()
    board.board = array
    # insert value in col 2
    board.set_value_cell(2,1)
    # position where 1 was insert
    last_position = (3,2)

    assert(board.last_mov == last_position)


# ------ TEST_WINNER ------

def test_winner_true():
    """Given a cell, check if there is win from it
    """

    array = [[1,2,1,1,2,2,2],
             [1,2,1,1,1,1,2],
             [0,2,2,1,2,2,2],
             [0,1,0,1,2,0,2],
             [0,0,0,2,0,0,0],
             [0,0,0,0,0,0,0]]
    board = Board()
    board.board = array
    test_pos = [[1,2],[1,5],[1,6],[4,3],[3,6],[3,3]]
    sym_p1 = 1
    sym_p2 = 2

    assert(board.winner(test_pos[0][0],test_pos[0][1],sym_p1) == True)
    assert(board.winner(test_pos[1][0],test_pos[1][1],sym_p1) == True)
    assert(board.winner(test_pos[2][0],test_pos[2][1],sym_p2) == True)
    assert(board.winner(test_pos[3][0],test_pos[3][1],sym_p2) == True)
    assert(board.winner(test_pos[4][0],test_pos[4][1],sym_p2) == True)
    assert(board.winner(test_pos[5][0],test_pos[5][1],sym_p1) == True)


def test_winner_false():
    """Given a cell, check if there is not win from it
    """

    array = [[1,2,1,1,2,2,2],
             [1,2,1,1,1,1,2],
             [0,2,2,1,2,2,2],
             [0,1,0,1,2,0,2],
             [0,0,0,2,0,0,0],
             [0,0,0,0,0,0,0]]
    board = Board()
    board.board = array
    test_pos = [[1,2],[1,5],[1,8],[4,5],[3,6],[3,3],[-4,3],[2,11]]
    sym_p1 = 1
    sym_p2 = 2
    sym_p3 = 3

    # compare with symbols valid
    assert(board.winner(test_pos[0][0],test_pos[0][1],sym_p2) == False)
    assert(board.winner(test_pos[1][0],test_pos[1][1],sym_p2) == False)
    assert(board.winner(test_pos[3][0],test_pos[3][1],sym_p1) == False)
    assert(board.winner(test_pos[4][0],test_pos[4][1],sym_p1) == False)
    assert(board.winner(test_pos[5][0],test_pos[5][1],sym_p2) == False)
    # compare with symbol not valid
    assert(board.winner(test_pos[3][0],test_pos[3][1],sym_p3) == False)
    assert(board.winner(test_pos[4][0],test_pos[4][1],sym_p3) == False)
    assert(board.winner(test_pos[5][0],test_pos[5][1],sym_p3) == False)
    # compare with cell (row, col) not valid
    assert(board.winner(test_pos[2][0],test_pos[2][1],sym_p1) == False)
    assert(board.winner(test_pos[6][0],test_pos[6][1],sym_p1) == False)
    assert(board.winner(test_pos[7][0],test_pos[7][1],sym_p1) == False)


# ------ TEST_WIN_HZT ------

def test_win_hzt_true():
    """Given a cell, check if there is win from it in horizontal line
    """

    array = [[1,2,1,1,2,2,2],
             [1,1,1,1,1,1,2],
             [0,2,2,2,2,2,2],
             [0,1,0,1,2,0,2],
             [0,0,0,2,0,0,0],
             [0,0,0,0,0,0,0]]
    board = Board()
    board.board = array
    test_pos_1 = [[1,0],[1,1],[1,2],[2,1],[2,2],[2,3]]
    test_pos_2 = [[1,5],[1,4],[1,3],[2,6],[2,5],[2,4]]
    size_line = 3
    sym_p1 = 1
    sym_p2 = 2

    # compare cases left to rigth
    assert(board.win_hzt(test_pos_1[0][0],test_pos_1[0][1],True,sym_p1) >= size_line)
    assert(board.win_hzt(test_pos_1[1][0],test_pos_1[1][1],True,sym_p1) >= size_line)
    assert(board.win_hzt(test_pos_1[2][0],test_pos_1[2][1],True,sym_p1) >= size_line)
    assert(board.win_hzt(test_pos_1[3][0],test_pos_1[3][1],True,sym_p2) >= size_line)
    assert(board.win_hzt(test_pos_1[4][0],test_pos_1[4][1],True,sym_p2) >= size_line)
    assert(board.win_hzt(test_pos_1[5][0],test_pos_1[5][1],True,sym_p2) >= size_line)
    # compare cases rigth to lef
    assert(board.win_hzt(test_pos_2[0][0],test_pos_2[0][1],False,sym_p1) >= size_line)
    assert(board.win_hzt(test_pos_2[1][0],test_pos_2[1][1],False,sym_p1) >= size_line)
    assert(board.win_hzt(test_pos_2[2][0],test_pos_2[2][1],False,sym_p1) >= size_line)
    assert(board.win_hzt(test_pos_2[3][0],test_pos_2[3][1],False,sym_p2) >= size_line)
    assert(board.win_hzt(test_pos_2[4][0],test_pos_2[4][1],False,sym_p2) >= size_line)
    assert(board.win_hzt(test_pos_2[5][0],test_pos_2[5][1],False,sym_p2) >= size_line)

def test_win_hzt_false():
    """Given a cell, check if there is not win from it in horizontal line
    """

    array = [[1,2,1,1,2,2,2],
             [1,2,1,1,1,1,2],
             [0,2,2,1,2,2,2],
             [0,1,0,1,2,0,2],
             [0,0,0,2,0,0,0],
             [0,0,0,0,0,0,0]]
    board = Board()
    board.board = array
    test_pos_1 = [[2,0],[2,1],[2,2],[1,1],[1,2],[1,3]]
    test_pos_2 = [[2,5],[2,4],[2,3],[1,6],[1,3],[1,4]]
    test_pos_3 = [[-1,0],[10,3],[5,-4],[9,0]]
    size_line = 3
    sym_p1 = 1
    sym_p2 = 2
    sym_p3 = 3
    
    # compare cases left to rigth
    assert(board.win_hzt(test_pos_1[0][0],test_pos_1[0][1],True,sym_p1) < size_line)
    assert(board.win_hzt(test_pos_1[1][0],test_pos_1[1][1],True,sym_p1) < size_line)
    assert(board.win_hzt(test_pos_1[2][0],test_pos_1[2][1],True,sym_p1) < size_line)
    assert(board.win_hzt(test_pos_1[3][0],test_pos_1[3][1],True,sym_p2) < size_line)
    assert(board.win_hzt(test_pos_1[4][0],test_pos_1[4][1],True,sym_p2) < size_line)
    assert(board.win_hzt(test_pos_1[5][0],test_pos_1[5][1],True,sym_p2) < size_line)
    # compare cases rigth to left
    assert(board.win_hzt(test_pos_2[0][0],test_pos_2[0][1],False,sym_p2) < size_line)
    assert(board.win_hzt(test_pos_2[1][0],test_pos_2[1][1],False,sym_p2) < size_line)
    assert(board.win_hzt(test_pos_2[2][0],test_pos_2[2][1],False,sym_p1) < size_line)
    assert(board.win_hzt(test_pos_2[3][0],test_pos_2[3][1],False,sym_p1) < size_line)
    assert(board.win_hzt(test_pos_2[4][0],test_pos_2[4][1],False,sym_p1) < size_line)
    assert(board.win_hzt(test_pos_2[5][0],test_pos_2[5][1],False,sym_p2) < size_line)
    # compare with symbol not valid
    assert(board.win_hzt(test_pos_1[4][0],test_pos_1[4][1],True,sym_p3) < size_line)
    assert(board.win_hzt(test_pos_1[5][0],test_pos_1[5][1],True,sym_p3) < size_line)
    assert(board.win_hzt(test_pos_2[4][0],test_pos_2[4][1],False,sym_p3) < size_line)
    assert(board.win_hzt(test_pos_2[5][0],test_pos_2[5][1],False,sym_p3) < size_line)
    # compare with cell (row, col) not valid
    assert(board.win_hzt(test_pos_3[0][0],test_pos_1[0][1],True,sym_p1) < size_line)
    assert(board.win_hzt(test_pos_3[1][0],test_pos_1[1][1],True,sym_p1) < size_line)
    assert(board.win_hzt(test_pos_3[2][0],test_pos_2[2][1],False,sym_p2) < size_line)
    assert(board.win_hzt(test_pos_3[3][0],test_pos_2[3][1],False,sym_p2) < size_line)

# ------ TEST_WIN_VRT ------

def test_win_vrt_true():
    """Given a cell, check if there is win from it in vertical line
    """
    
    array = [[1,2,1,1,2,2,2],
             [1,2,1,1,2,1,2],
             [1,2,2,1,2,2,2],
             [1,1,0,1,2,0,2],
             [0,0,0,1,2,0,0],
             [0,0,0,0,2,0,0]]
    board = Board()
    board.board = array
    test_pos_1 = [[3,0],[4,3],[3,3],[5,4],[4,4],[3,4],[3,6]]
    size_line = 3
    sym_p1 = 1
    sym_p2 = 2

    assert(board.win_vrt(test_pos_1[0][0],test_pos_1[0][1],sym_p1) >= size_line)
    assert(board.win_vrt(test_pos_1[1][0],test_pos_1[1][1],sym_p1) >= size_line)
    assert(board.win_vrt(test_pos_1[2][0],test_pos_1[2][1],sym_p1) >= size_line)
    assert(board.win_vrt(test_pos_1[3][0],test_pos_1[3][1],sym_p2) >= size_line)
    assert(board.win_vrt(test_pos_1[4][0],test_pos_1[4][1],sym_p2) >= size_line)
    assert(board.win_vrt(test_pos_1[5][0],test_pos_1[5][1],sym_p2) >= size_line)
    assert(board.win_vrt(test_pos_1[6][0],test_pos_1[6][1],sym_p2) >= size_line)
    
def test_win_vrt_false():
    """Given a cell, check if there is not win from it in vertical line
    """
    
    array = [[1,2,1,1,2,2,2],
             [1,2,1,1,2,1,2],
             [1,2,2,1,2,2,2],
             [1,1,0,1,2,0,2],
             [0,0,0,1,2,0,0],
             [0,0,0,0,2,0,0]]
    board = Board()
    board.board = array
    test_pos_1 = [[3,0],[4,3],[3,3],[5,4],[4,4],[3,4],[3,6]]
    test_pos_2 = [[-1,0],[9,10],[5,-5]]
    size_line = 3
    sym_p1 = 1
    sym_p2 = 2
    sym_p3 = 3

    assert(board.win_vrt(test_pos_1[0][0],test_pos_1[0][1],sym_p2) < size_line)
    assert(board.win_vrt(test_pos_1[1][0],test_pos_1[1][1],sym_p2) < size_line)
    assert(board.win_vrt(test_pos_1[2][0],test_pos_1[2][1],sym_p2) < size_line)
    assert(board.win_vrt(test_pos_1[3][0],test_pos_1[3][1],sym_p1) < size_line)
    assert(board.win_vrt(test_pos_1[4][0],test_pos_1[4][1],sym_p1) < size_line)
    assert(board.win_vrt(test_pos_1[5][0],test_pos_1[5][1],sym_p1) < size_line)
    assert(board.win_vrt(test_pos_1[6][0],test_pos_1[6][1],sym_p1) < size_line)
    # compare with symbol not valid
    assert(board.win_vrt(test_pos_1[4][0],test_pos_1[4][1],sym_p3) < size_line)
    assert(board.win_vrt(test_pos_1[5][0],test_pos_1[5][1],sym_p3) < size_line)
    assert(board.win_vrt(test_pos_1[6][0],test_pos_1[6][1],sym_p3) < size_line)
    # compare with cell (row, col) not valid
    assert(board.win_vrt(test_pos_2[0][0],test_pos_2[0][1],sym_p3) < size_line)
    assert(board.win_vrt(test_pos_2[1][0],test_pos_2[1][1],sym_p3) < size_line)
    assert(board.win_vrt(test_pos_2[2][0],test_pos_2[2][1],sym_p3) < size_line)


# ------ TEST_DIAG_BACK ------

def test_diag_back_true():
    """Given a cell, check if there is win from it in diagonal_back line
    """
    
    array = [[1,2,1,1,2,2,2],
             [1,2,1,2,2,1,2],
             [1,1,2,1,1,2,2],
             [1,2,2,1,2,2,2],
             [2,2,1,1,2,0,0],
             [0,1,0,2,2,0,0]]
    board = Board()
    board.board = array
    test_pos_1 = [[3,0],[4,0],[3,1],[5,1],[4,2],[5,3]]
    test_pos_2 = [[0,3],[0,4],[1,3],[1,5],[2,4],[2,6]]
    size_line = 3
    sym_p1 = 1
    sym_p2 = 2

    # compare cases left to rigth
    assert(board.win_diag_back(test_pos_1[0][0],test_pos_1[0][1],True,sym_p1) >= size_line)
    assert(board.win_diag_back(test_pos_1[1][0],test_pos_1[1][1],True,sym_p2) >= size_line)
    assert(board.win_diag_back(test_pos_1[2][0],test_pos_1[2][1],True,sym_p2) >= size_line)
    assert(board.win_diag_back(test_pos_1[3][0],test_pos_1[3][1],True,sym_p1) >= size_line)
    assert(board.win_diag_back(test_pos_1[4][0],test_pos_1[4][1],True,sym_p1) >= size_line)
    assert(board.win_diag_back(test_pos_1[5][0],test_pos_1[5][1],True,sym_p2) >= size_line)
    # compare cases rigth to left
    assert(board.win_diag_back(test_pos_2[0][0],test_pos_2[0][1],False,sym_p1) >= size_line)
    assert(board.win_diag_back(test_pos_2[1][0],test_pos_2[1][1],False,sym_p2) >= size_line)
    assert(board.win_diag_back(test_pos_2[2][0],test_pos_2[2][1],False,sym_p2) >= size_line)
    assert(board.win_diag_back(test_pos_2[3][0],test_pos_2[3][1],False,sym_p1) >= size_line)
    assert(board.win_diag_back(test_pos_2[4][0],test_pos_2[4][1],False,sym_p1) >= size_line)
    assert(board.win_diag_back(test_pos_2[5][0],test_pos_2[5][1],False,sym_p2) >= size_line)
    

def test_diag_back_false():
    """Given a cell, check if there is not win from it in diagonal_back line
    """

    array = [[1,2,1,1,2,2,2],
             [1,2,1,2,2,1,2],
             [1,1,2,1,1,2,2],
             [1,2,2,1,2,2,2],
             [2,2,1,1,2,0,0],
             [0,1,0,2,2,0,0]]
    board = Board()
    board.board = array
    test_pos_1 = [[3,0],[4,0],[3,1],[5,1],[4,2],[5,3]]
    test_pos_2 = [[0,3],[0,4],[1,3],[1,5],[2,4],[2,6]]
    test_pos_3 = [[-1,5],[7,8],[8,9],[-6,-5]]
    size_line = 3
    sym_p1 = 1
    sym_p2 = 2
    sym_p3 = 3

    # compare cases left to rigth
    assert(board.win_diag_back(test_pos_1[0][0],test_pos_1[0][1],True,sym_p2) < size_line)
    assert(board.win_diag_back(test_pos_1[1][0],test_pos_1[1][1],True,sym_p1) < size_line)
    assert(board.win_diag_back(test_pos_1[2][0],test_pos_1[2][1],True,sym_p1) < size_line)
    assert(board.win_diag_back(test_pos_1[3][0],test_pos_1[3][1],True,sym_p2) < size_line)
    assert(board.win_diag_back(test_pos_1[4][0],test_pos_1[4][1],True,sym_p2) < size_line)
    assert(board.win_diag_back(test_pos_1[5][0],test_pos_1[5][1],True,sym_p1) < size_line)
    # compare cases rigth to left
    assert(board.win_diag_back(test_pos_2[0][0],test_pos_2[0][1],False,sym_p2) < size_line)
    assert(board.win_diag_back(test_pos_2[1][0],test_pos_2[1][1],False,sym_p1) < size_line)
    assert(board.win_diag_back(test_pos_2[2][0],test_pos_2[2][1],False,sym_p1) < size_line)
    assert(board.win_diag_back(test_pos_2[3][0],test_pos_2[3][1],False,sym_p2) < size_line)
    assert(board.win_diag_back(test_pos_2[4][0],test_pos_2[4][1],False,sym_p2) < size_line)
    assert(board.win_diag_back(test_pos_2[5][0],test_pos_2[5][1],False,sym_p1) < size_line)
    # compare with symbol not valid
    assert(board.win_diag_back(test_pos_1[4][0],test_pos_1[4][1],True,sym_p3) < size_line)
    assert(board.win_diag_back(test_pos_1[5][0],test_pos_1[5][1],True,sym_p3) < size_line)
    assert(board.win_diag_back(test_pos_2[0][0],test_pos_2[0][1],False,sym_p3) < size_line)
    assert(board.win_diag_back(test_pos_2[1][0],test_pos_2[1][1],False,sym_p3) < size_line)
    # compare with cell (row, col) not valid
    assert(board.win_diag_back(test_pos_3[0][0],test_pos_3[0][1],True,sym_p3) < size_line)
    assert(board.win_diag_back(test_pos_3[1][0],test_pos_3[1][1],True,sym_p3) < size_line)
    assert(board.win_diag_back(test_pos_3[2][0],test_pos_3[2][1],False,sym_p3) < size_line)
    assert(board.win_diag_back(test_pos_3[3][0],test_pos_3[3][1],False,sym_p3) < size_line)


# ------ TEST_DIAG_SLASH ------

def test_diag_slash_true():
    """Given a cell, check if there is win from it in diagonal_slash line
    """
    
    array = [[2,2,1,2,2,2,2],
             [1,2,1,2,2,1,2],
             [1,1,2,1,2,2,2],
             [1,2,1,2,2,2,2],
             [2,2,1,1,2,0,2],
             [0,1,0,2,1,0,0]]
    board = Board()
    board.board = array
    test_pos_1 = [[0,0],[1,1],[1,0],[2,1],[1,3],[0,3]]
    test_pos_2 = [[5,4],[4,3],[4,4],[3,3],[4,6],[3,6]]
    size_line = 3
    sym_p1 = 1
    sym_p2 = 2

    # compare cases left to rigth
    assert(board.win_diag_slash(test_pos_1[0][0],test_pos_1[0][1],True,sym_p2) >= size_line)
    assert(board.win_diag_slash(test_pos_1[1][0],test_pos_1[1][1],True,sym_p2) >= size_line)
    assert(board.win_diag_slash(test_pos_1[2][0],test_pos_1[2][1],True,sym_p1) >= size_line)
    assert(board.win_diag_slash(test_pos_1[3][0],test_pos_1[3][1],True,sym_p1) >= size_line)
    assert(board.win_diag_slash(test_pos_1[4][0],test_pos_1[4][1],True,sym_p2) >= size_line)
    assert(board.win_diag_slash(test_pos_1[5][0],test_pos_1[5][1],True,sym_p2) >= size_line)
    # compare cases rigth to left
    assert(board.win_diag_slash(test_pos_2[0][0],test_pos_2[0][1],False,sym_p1) >= size_line)
    assert(board.win_diag_slash(test_pos_2[1][0],test_pos_2[1][1],False,sym_p1) >= size_line)
    assert(board.win_diag_slash(test_pos_2[2][0],test_pos_2[2][1],False,sym_p2) >= size_line)
    assert(board.win_diag_slash(test_pos_2[3][0],test_pos_2[3][1],False,sym_p2) >= size_line)
    assert(board.win_diag_slash(test_pos_2[4][0],test_pos_2[4][1],False,sym_p2) >= size_line)
    assert(board.win_diag_slash(test_pos_2[5][0],test_pos_2[5][1],False,sym_p2) >= size_line)


def test_diag_slash_false():
    """Given a cell, check if there is not win from it in diagonal_slash line
    """

    array = [[1,2,1,1,2,2,2],
             [1,2,1,2,2,1,2],
             [1,1,2,1,1,2,2],
             [1,2,2,1,2,2,2],
             [2,2,1,1,2,0,0],
             [0,1,0,2,2,0,0]]
    board = Board()
    board.board = array
    test_pos_1 = [[3,0],[4,0],[3,1],[5,1],[4,2],[5,3]]
    test_pos_2 = [[0,3],[0,4],[1,3],[1,5],[2,4],[2,6]]
    test_pos_3 = [[-1,5],[7,8],[8,9],[-6,-5]]
    size_line = 3
    sym_p1 = 1
    sym_p2 = 2
    sym_p3 = 3

    # compare cases left to rigth
    test_pos_1 = [[0,0],[1,1],[1,0],[2,1],[1,3],[0,3]]
    test_pos_2 = [[5,4],[4,3],[4,4],[3,3],[4,6],[3,6]]
    test_pos_3 = [[-1,5],[7,8],[8,9],[-6,-5]]
    size_line = 3
    sym_p1 = 1
    sym_p2 = 2
    sym_p3 = 3

    # compare cases left to rigth
    assert(board.win_diag_slash(test_pos_1[0][0],test_pos_1[0][1],True,sym_p1) < size_line)
    assert(board.win_diag_slash(test_pos_1[1][0],test_pos_1[1][1],True,sym_p1) < size_line)
    assert(board.win_diag_slash(test_pos_1[2][0],test_pos_1[2][1],True,sym_p2) < size_line)
    assert(board.win_diag_slash(test_pos_1[3][0],test_pos_1[3][1],True,sym_p2) < size_line)
    assert(board.win_diag_slash(test_pos_1[4][0],test_pos_1[4][1],True,sym_p1) < size_line)
    assert(board.win_diag_slash(test_pos_1[5][0],test_pos_1[5][1],True,sym_p1) < size_line)
    # compare cases rigth to left
    assert(board.win_diag_slash(test_pos_2[0][0],test_pos_2[0][1],False,sym_p2) < size_line)
    assert(board.win_diag_slash(test_pos_2[1][0],test_pos_2[1][1],False,sym_p2) < size_line)
    assert(board.win_diag_slash(test_pos_2[2][0],test_pos_2[2][1],False,sym_p1) < size_line)
    assert(board.win_diag_slash(test_pos_2[3][0],test_pos_2[3][1],False,sym_p1) < size_line)
    assert(board.win_diag_slash(test_pos_2[4][0],test_pos_2[4][1],False,sym_p1) < size_line)
    assert(board.win_diag_slash(test_pos_2[5][0],test_pos_2[5][1],False,sym_p1) < size_line)
    # compare with symbol not valid
    assert(board.win_diag_slash(test_pos_1[4][0],test_pos_1[4][1],True,sym_p3) < size_line)
    assert(board.win_diag_slash(test_pos_1[5][0],test_pos_1[5][1],True,sym_p3) < size_line)
    assert(board.win_diag_slash(test_pos_2[0][0],test_pos_2[0][1],False,sym_p3) < size_line)
    assert(board.win_diag_slash(test_pos_2[1][0],test_pos_2[1][1],False,sym_p3) < size_line)
    # compare with cell (row, col) not valid
    assert(board.win_diag_slash(test_pos_3[0][0],test_pos_3[0][1],True,sym_p3) < size_line)
    assert(board.win_diag_slash(test_pos_3[1][0],test_pos_3[1][1],True,sym_p3) < size_line)
    assert(board.win_diag_slash(test_pos_3[2][0],test_pos_3[2][1],False,sym_p3) < size_line)
    assert(board.win_diag_slash(test_pos_3[3][0],test_pos_3[3][1],False,sym_p3) < size_line)
