from ....model.game.game import Game
from ....model.game.human import Human
from ....model.game.agent import Agent

player_1 = Human()
player_2 = Agent(2, 1)  # 2 symbol of the agent, 1 symbol of the opponent
game = Game(player_1, player_2)


def test_play_game():
    """ Check that game is working correctly
    """
    pass


def test_turn():
    """ Check that turn of the player is working correctly
    """
    pass


def test_who_is_winner_player_1():
    """ Check who is the winner of the game
    """
    game.turn_player_1 = True
    game.board.created_board()
    winner = "** Ganador Jugador 1 **"
    winner_game = game.who_is_winner()
    assert(winner == winner_game)


def test_who_is_winner_player_2():
    """ Check who is the winner of the game
    """
    game.turn_player_1 = False
    game.board.created_board()
    winner = "** Ganador Jugador 2 **"
    winner_game = game.who_is_winner()
    assert(winner == winner_game)


def test_is_winner_True():
    """ Check if exist a winner
    """
    array = [[1, 1, 1, 2, 1, 0, 0],
             [2, 1, 1, 1, 2, 0, 0],
             [0, 0, 1, 2, 2, 0, 0],
             [0, 0, 1, 2, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0]]
    game.board.last_mov = (3, 2)
    game.turn_player_1 = True
    game.board.board = array
    is_winner = game.is_winner()
    assert(is_winner)


def test_is_winner_False():
    """ Check if exist a winner
    """
    array = [[1, 1, 1, 2, 1, 0, 0],
             [2, 1, 1, 1, 2, 0, 0],
             [0, 0, 2, 2, 2, 0, 0],
             [0, 0, 1, 2, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0]]
    game.board.last_mov = (3, 2)
    game.turn_player_1 = True
    game.board.board = array
    is_winner = game.is_winner()
    assert(not is_winner)
