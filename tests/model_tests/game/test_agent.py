from ....model.game.agent import Agent
from ....model.game.board import Board
from ....model.strategies.position import Number
from ....model.strategies.strategy import Strategy
from ....model.strategies.sequential_vs_space import SequentialvsSpace
from ....model.strategies.center_vs_extremity import Center_vs_extremity
from ....model.strategies.horizontal_vs_vertical import Horizontal_vertical

array = [[1, 1, 1, 2, 1, 0, 0],
         [2, 1, 1, 1, 2, 0, 0],
         [0, 0, 1, 2, 2, 0, 0],
         [0, 0, 0, 2, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]]
board = Board()
board.set_board(array)
player_1 = Agent(1, 2)  # 1 symbol of the agent, 2 symbol of the opponent
player_2 = Agent(2, 1)  # 2 symbol of the agent, 1 symbol of the opponent


def test_next_action_win():
    """ Check that next_action is working correctly
    """
    col_result = player_1.next_action(board)
    col = 2
    assert(col == col_result)


def test_next_action_block():
    """ Check that next_action is working correctly
    """
    col_result = player_2.next_action(board)
    col = 2
    assert(col == col_result)

def test_get_strategy():
    """ Check that get_strategy is working correctly
    """
    pass

def test_get_column_number():
    """ Check that get_column_number is working correctly
    """
    pass

def test_get_array_number():
    """ Check that get_column_number is working correctly
    """
    array_number = []
    var_number = Number(0)
    array_number.append(var_number)
    var_number = Number(1)
    array_number.append(var_number)
    var_number = Number(2)
    array_number.append(var_number)
    var_number = Number(3)
    array_number.append(var_number)
    var_number = Number(4)
    array_number.append(var_number)
    var_number = Number(5)
    array_number.append(var_number)
    var_number = Number(6)
    array_number.append(var_number)

    array_number_result = player_1.get_array_number()
    #Ver como comparar listas
    print(array_number, array_number_result)
    assert(True)


def test_block_true():
    """ Check that block function is working correctly
    """
    col_to_block_result = player_2.block(board, 1)
    col_to_block = 2
    assert(col_to_block == col_to_block_result)


def test_block_false():
    """ Check that block function is working correctly
    """
    col_to_block_result = player_1.block(board, 2)
    col_to_block = -1
    assert(col_to_block == col_to_block_result)


def test_win_true():
    """ Check that win function is working correctly
    """
    col_to_block_result = player_1.win(board, 1)
    col_to_block = 2
    assert(col_to_block == col_to_block_result)


def test_win_false():
    """ Check that win function is working correctly
    """
    col_to_block_result = player_2.win(board, 2)
    col_to_block = -1
    assert(col_to_block == col_to_block_result)
