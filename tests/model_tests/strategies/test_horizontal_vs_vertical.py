# Package: tests.model_tests.startegies
# Description: tests of strategy horizontal_vs_vertical

# Artificial Intelligence, II Semester 2018
# Project: Connect 4
# Author : Mariana Rojas S. 
# E-mail: mari.semeraro27@gmail.com
# Version: 0.0.0 

# IMPORT SECTION
from ....model.game.board import Board
from ....model.strategies.position import Number
from ....model.strategies.horizontal_vs_vertical import Horizontal_vertical
from copy import deepcopy

b = [[1, 0, 1, 2, 1, 0, 0],
     [2, 0, 0, 2, 1, 0, 0],
     [1, 0, 0, 1, 2, 0, 0],
     [2, 0, 0, 0, 1, 0, 0],
     [2, 0, 0, 0, 1, 0, 0],
     [1, 0, 0, 0, 2, 0, 0]]
board = Board()
board.board = b
array_number = []

for i in range(0, 7):
    var_number = Number(i)
    array_number.append(var_number)


def test_get_action_horizontal():
    """ Check that get_action is working correctly
    """
    strategy = Horizontal_vertical(1, 1)  # Probability 1 (horizontal) 
    var_action = strategy.get_action(board, deepcopy(array_number))
    array_result = [[0, 0, 0], [1, 9, 1], [2, 8, 1], 
                    [3, 8, 1], [4, 0, 0], [5, 9, 1], [6, 9, 1]]
    result = True
    for x in var_action: 
        position = array_result[x.position][0]
        amount = array_result[x.position][1]
        strategies_number = array_result[x.position][2]
        if not(x.position == position and x.amount == amount 
                and strategies_number == x.strategies_number):
            result = False
    assert(result)


def test_get_action_vertical():
    """ Check that get_action is working correctly
    """
    strategy = Horizontal_vertical(0, 1)  # Probability 1 (vertical) 
    var_action = strategy.get_action(board, deepcopy(array_number))
    array_result = [[0, 0, 0], [1, 0, 0], [2, 1, 1], 
                    [3, 1, 1], [4, 0, 0], [5, 0, 0], [6, 0, 0]]
    result = True
    for x in var_action: 
        position = array_result[x.position][0]
        amount = array_result[x.position][1]
        strategies_number = array_result[x.position][2]
        if not(x.position == position and x.amount == amount 
                and strategies_number == x.strategies_number):
            result = False
    assert(result)
