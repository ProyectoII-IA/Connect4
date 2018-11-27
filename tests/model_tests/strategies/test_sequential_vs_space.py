# Package: tests.model_tests.startegies
# Description: tests of strategy sequential_vs_space

# Artificial Intelligence, II Semester 2018
# Project: Connect 4
# Author : Mariana Rojas S. 
# E-mail: mari.semeraro27@gmail.com
# Version: 0.0.0 

# IMPORT SECTION
from model.game.board import Board
from model.strategies.position import Number
from model.strategies.sequential_vs_space import SequentialvsSpace
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

array_real = []

test_sequential = SequentialvsSpace(0.50,1)


# VALIDATE_SEQUENTIAL_POSICION-----------------------------------------

def test_validate_secuential_posicion_negative():
    result = test_sequential.validate_sequential_position(-1,0)
    assert(result == False)

def test_validate_secuential_posicion_no_found_index():
    result = test_sequential.validate_sequential_position(1,3)
    assert(result == False)

def test_validate_secuential_posicion_found_index():
    result = test_sequential.validate_sequential_position(1,2)
    assert(result == True)


# GET_NEIGHBORS_TESTS--------------------------------------------------

def test_get_neighbors_success():
    array_real.append(Board.get_cells_symbol)
    array_real.append(Board.get_empty_element)
    array_real.append(SequentialvsSpace.validate_sequential_position)

    Board.get_cells_symbol = lambda x,y: [(1,2)] # Get available neighbors of posicion 2 
    Board.get_empty_element = lambda x,y: 1
    SequentialvsSpace.validate_sequential_position = lambda x,y,z: True

    result = test_sequential.get_neighbors(board)
    assert(result == [(0, 0), (1, 1), (2, 1), (3, 1), (4, 0), (5, 0),(6,0)])
    SequentialvsSpace.validate_sequential_position = array_real.pop()
    Board.get_empty_element = array_real.pop()
    Board.get_cells_symbol = array_real.pop()

# GET SEQUENTIAL ACTION TESTS-----------------------------------------

def test_get_sequential_action_success():
    array_real.append(SequentialvsSpace.get_neighbors)
    SequentialvsSpace.get_neighbors = lambda x,y: [(0, 3), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0),(6,0)]

    result = test_sequential.get_sequential_action(board,array_number)
    array_number[0].increase_amount
    array_number[0].increase_strategy

    assert(result[0].strategies_number == 1)
    assert(result[0].amount == 3)
    assert(result[0] == array_number[0])

    SequentialvsSpace.get_neighbors = array_real.pop()

# GET_SPACE_ACTION TESTS------------------------------------------------

def test_get_space_action_success():
    array_real.append(SequentialvsSpace.get_neighbors)
    SequentialvsSpace.get_neighbors = lambda x,y: [(0,0), (1,1), (2, 1), (3,1), (4,1), (5,1),(6,1)]
    test_array = []
    for i in range(0, 7):
        test_array.append(Number(i))

    result = test_sequential.get_space_action(board,test_array)

    assert(result[0].position == 0)
    assert(result[0].strategies_number == 1)
    assert(result[0].amount == 1)

    assert(result[1].strategies_number == 0)
    assert(result[1].amount == 0)

    SequentialvsSpace.get_neighbors = array_real.pop()

# GET_ACTION TESTS-------------------------------------------------

def test_get_action_sequential():
    array_real.append(SequentialvsSpace.get_random_number)
    array_real.append(SequentialvsSpace.get_sequential_action)
    SequentialvsSpace.get_sequential_action = lambda x,y,z: "SEQUENTIAL STRATEGY"
    SequentialvsSpace.get_random_number = lambda _: 0.5
    test_sequential.probability = 0.6
    
    result = test_sequential.get_action(board,array_number)
    assert(result == "SEQUENTIAL STRATEGY")

    SequentialvsSpace.get_sequential_action = array_real.pop()
    SequentialvsSpace.get_random_number = array_real.pop()

def test_get_action_space():
    array_real.append(SequentialvsSpace.get_random_number)
    array_real.append(SequentialvsSpace.get_space_action)
    
    SequentialvsSpace.get_space_action = lambda x,y,z: "SPACE STRATEGY"
    SequentialvsSpace.get_random_number = lambda _: 0.6
    test_sequential.probability = 0.5
    
    result = test_sequential.get_action(board,array_number)
    assert(result == "SPACE STRATEGY")

    SequentialvsSpace.get_space_action = array_real.pop()
    SequentialvsSpace.get_random_number = array_real.pop()











