# Package: tests.model_tests.game
# Description: tests of structure agent

# Artificial Intelligence, II Semester 2018
# Project: Connect 4
# Author : Mariana Rojas S. 
# E-mail: mari.semeraro27@gmail.com
# Version: 0.0.0 

# IMPORT SECTION
from model.game.agent import Agent
from model.game.board import Board
from model.strategies.position import Number
from model.strategies.strategy import Strategy
from model.strategies.sequential_vs_space import SequentialvsSpace
from model.strategies.center_vs_extremity import Center_vs_extremity
from model.strategies.horizontal_vs_vertical import Horizontal_vertical

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

def test_get_strategy_1():
    """ Check that get_strategy is working correctly
    """
    b = [[1, 0, 1, 2, 1, 1, 0],
     [2, 0, 0, 2, 1, 2, 0],
     [1, 0, 0, 1, 2, 2, 0],
     [2, 0, 0, 0, 1, 0, 0],
     [2, 0, 0, 0, 1, 0, 0],
     [1, 0, 0, 0, 2, 0, 0]]
    board = Board()
    board.board = b
    player_1.set_strategies([1,1,1,1])
    var_action = player_1.get_strategy(board)
    array_result = [[0, 0, 0], [1, 12, 2], [2, 12, 3], 
                    [3, 14, 4], [4, 0, 0], [5, 12, 3], [6, 12, 3]]
    result = True
    for x in var_action: 
        position = array_result[x.position][0]
        amount = array_result[x.position][1]
        strategies_number = array_result[x.position][2]
        if not(x.position == position and x.amount == amount 
                and strategies_number == x.strategies_number):
            result = False
    assert(result)


def test_get_strategy_0():
    """ Check that get_strategy is working correctly
    """
    b = [[1, 0, 1, 2, 1, 1, 0],
     [2, 0, 0, 2, 1, 2, 0],
     [1, 0, 0, 1, 2, 2, 0],
     [2, 0, 0, 0, 1, 0, 0],
     [2, 0, 0, 0, 1, 0, 0],
     [1, 0, 0, 0, 2, 0, 0]]
    board = Board()
    board.board = b
    player_1.set_strategies([0,0,0,0])
    var_action = player_1.get_strategy(board)
    array_result = [[0, 1, 1], [1, 2, 2], [2, 2, 2], 
                    [3, 2, 2], [4, 1, 1], [5, 3, 3], [6, 2, 2]]
    result = True
    for x in var_action: 
        position = array_result[x.position][0]
        amount = array_result[x.position][1]
        strategies_number = array_result[x.position][2]
        print(x.position,x.amount, x.strategies_number)
        if not(x.position == position and x.amount == amount 
                and strategies_number == x.strategies_number):
            result = False
    assert(result)


def test_get_column_number():
    """ Check that get_column_number is working correctly
    """
    array_number = []
    for i in range(0,7):
        var_number = Number(i)
        if(i == 2):
            var_number.increase_strategy()
            var_number.increase_strategy()
        var_number.increase_strategy()
        var_number.increase_amount()
        array_number.append(var_number)
    col = player_1.get_column_number(array_number)
    col_result = 2
    assert(col == col_result)

def test_get_array_number():
    """ Check that get_column_number is working correctly
    """
    array_result = [[0, 0, 0], [1, 0, 0], [2, 0, 0], 
                    [3, 0, 0], [4, 0, 0], [5, 0, 0], [6, 0, 0]]
    var_action = player_1.get_array_number()
    result = True
    for x in var_action: 
        position = array_result[x.position][0]
        amount = array_result[x.position][1]
        strategies_number = array_result[x.position][2]
        if not(x.position == position and x.amount == amount 
                and strategies_number == x.strategies_number):
            result = False
    assert(result)


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
