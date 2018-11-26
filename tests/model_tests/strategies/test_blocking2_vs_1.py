# Package: tests.model_tests.startegies
# Description: tests of strategy blocking1_vs_2

# Artificial Intelligence, II Semester 2018
# Project: Connect 4
# Author : Mariana Rojas S. 
# E-mail: mari.semeraro27@gmail.com
# Version: 0.0.0 

# IMPORT SECTION
from model.game.board import Board
from model.strategies.position import Number
from model.strategies.blocking2_vs_1 import Blocking2vsBlocking1
from copy import deepcopy

b = [[1, 0, 1, 2, 1, 1, 0],
     [2, 0, 0, 2, 1, 2, 0],
     [1, 0, 0, 1, 2, 2, 0],
     [2, 0, 0, 0, 1, 0, 0],
     [2, 0, 0, 0, 1, 0, 0],
     [1, 0, 0, 0, 2, 0, 0]]
board = Board()
board.board = b
array_number = []

for i in range(0, 7):
    var_number = Number(i)
    array_number.append(var_number)

def test_get_blockers_1():
    """ Check that get_blockers function is working correctly
    """
    strategy = Blocking2vsBlocking1(1, 1, 2)  # Probability 1 (blocking_1) 
    array = strategy.get_blockers(board,1)
    array_result = [1, 2, 3, 5, 6]
    assert(array == array_result)

def test_get_blockers_2():
    """ Check that get_blockers function is working correctly
    """
    strategy = Blocking2vsBlocking1(0, 1, 2)  # Probability 0 (blocking_2) 
    array = strategy.get_blockers(board,2)
    array_result = [3, 5, 6]
    assert(array == array_result)

def test_fill_numbers_value():
    """ Check that fill_numbers_value function is working correctly
    """
    strategy = Blocking2vsBlocking1(0, 1, 2)
    array_blocker = [3, 5, 6]
    var_action = strategy.fill_numbers_value(array_blocker, deepcopy(array_number))
    array_result = [[0, 0, 0], [1, 0, 0], [2, 0, 0], 
                    [3, 1, 1], [4, 0, 0], [5, 1, 1], [6, 1, 1]]
    result = True
    for x in var_action: 
        position = array_result[x.position][0]
        amount = array_result[x.position][1]
        strategies_number = array_result[x.position][2]
        if not(x.position == position and x.amount == amount 
                and strategies_number == x.strategies_number):
            result = False
    assert(result)

def test_get_action_blocking2():
    """ Check that get_action is working correctly
    """
    strategy = Blocking2vsBlocking1(1, 1, 2)  # Probability 1 (blocking_1) 
    var_action = strategy.get_action(board, deepcopy(array_number))
    array_result = [[0, 0, 0], [1, 0, 0], [2, 0, 0], 
                    [3, 1, 1], [4, 0, 0], [5, 1, 1], [6, 1, 1]]
    result = True
    for x in var_action: 
        position = array_result[x.position][0]
        amount = array_result[x.position][1]
        strategies_number = array_result[x.position][2]
        if not(x.position == position and x.amount == amount 
                and strategies_number == x.strategies_number):
            result = False
    assert(result)

def test_get_action_blocking1():
    """ Check that get_action is working correctly
    """
    strategy = Blocking2vsBlocking1(0, 1, 2)  # Probability 0 (blocking_2) 
    var_action = strategy.get_action(board, deepcopy(array_number))
    array_result = [[0, 0, 0], [1, 1, 1], [2, 1, 1], 
                    [3, 1, 1], [4, 0, 0], [5, 1, 1], [6, 1, 1]]
    result = True
    for x in var_action: 
        position = array_result[x.position][0]
        amount = array_result[x.position][1]
        strategies_number = array_result[x.position][2]
        if not(x.position == position and x.amount == amount 
                and strategies_number == x.strategies_number):
            result = False
    assert(result)
