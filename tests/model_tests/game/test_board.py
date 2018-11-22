from ....model.game.board import Board

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

def test_is_full():

    array = [[1,1,2,2,2,1,1],
             [2,1,1,1,2,1,2],
             [1,1,2,1,1,1,2],
             [2,2,1,2,2,2,1],
             [1,1,2,2,1,1,2],
             [2,1,2,1,1,2,2]]
    pass

"""
def test_is_full_column():
    pass

def test_is_cell_valid():
    pass

def test_is_col_valid():
    pass

def test_is_symbol_in():
    pass

def test_winner():
    pass

def test_win_hzt():
    pass

def test_win_vrt():
    pass

def test_diag_slash():
    pass

def test_diag_back():
    pass

def test_get_cols():
    pass

def test_get_rows():
    pass

def test_get_cells_symbol():
    pass

def test_last_mov():
    pass

def test_get_empty_element():
    pass

def test_get_column():
    pass

def test_set_value_cell():
    pass

"""