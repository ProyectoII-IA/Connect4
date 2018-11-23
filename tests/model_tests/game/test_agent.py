from ....model.game.agent import Agent
from ....model.game.board import Board

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


def test_validate_action():
    """ Check that validate_action is working correctly
    """
    pass


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
