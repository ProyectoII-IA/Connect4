# Package: tests.model_tests.startegies
# Description: tests of strategy center_vs_extremity

# Artificial Intelligence, II Semester 2018
# Project: Connect 4
# Author : Mariana Rojas S. 
# E-mail: mari.semeraro27@gmail.com
# Version: 0.0.0 

# IMPORT SECTION
from model.game.board import Board
from model.strategies.position import Number
from model.strategies.center_vs_extremity import Center_vs_extremity
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


def test_get_action_center():
    """ Check that get_action is working correctly
    """
    strategy = Center_vs_extremity(1, 1)  # Probability 1 (center) 
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


def test_get_action_extremity():
    """ Check that get_action is working correctly
    """
    strategy = Center_vs_extremity(0, 1)  # Probability 0 (extremity) 
    var_action = strategy.get_action(board, deepcopy(array_number))
    array_result = [[0, 0, 0], [1, 1, 1], [2, 0, 0], 
                    [3, 0, 0], [4, 0, 0], [5, 1, 1], [6, 1, 1]]
    result = True
    for x in var_action: 
        position = array_result[x.position][0]
        amount = array_result[x.position][1]
        strategies_number = array_result[x.position][2]
        if not(x.position == position and x.amount == amount 
                and strategies_number == x.strategies_number):
            result = False
    assert(result)
