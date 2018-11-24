# Package: tests.model_tests.game
# Description: tests of structure agent

# Artificial Intelligence, II Semester 2018
# Project: Connect 4
# Author : Mariana Rojas S. 
# E-mail: mari.semeraro27@gmail.com
# Version: 0.0.0 

# IMPORT SECTION
from ....model.game.player import Player
from ....model.game.board import Board

array = [[1, 1, 1, 2, 1, 0, 0],
         [2, 1, 1, 1, 2, 0, 0],
         [0, 0, 1, 2, 2, 0, 0],
         [0, 0, 0, 2, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 2, 0, 0, 0]]
board = Board()
board.set_board(array)
player_1 = Player()

def test_validate_action_True():
    """ Check that validate_action is working correctly
    """
    result = player_1.validate_action(board, 0)
    assert(result)

def test_validate_action_False():
    """ Check that validate_action is working correctly
    """
    result = player_1.validate_action(board, 3)
    assert(not result)