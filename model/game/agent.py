from model.game.player import Player
from model.game.board import Board
#from model.strategies.blocking1_vs_2 import Blocking1_vs_2
#from model.strategies.center_vs_extremity import Center_vs_Extremity
#from model.strategies.horizontal_vs_vertical import Horizontal_vs_Vertical
#from model.strategies.sequential_vs_space import Sequential_vs_Space
#from model.strategies.strategy import Strategy 


class Agent(Player):

    strategies = []

    def __init__(self):
        pass

    def next_action(self):
        pass

    def validate_action(self):
        pass

    def block(self, board, symb):
        return self.win(board, symb)

    def win(self, board, symb):
        cols = board.get_cols()
        for col in range(cols):
            if(not(board.is_fill_column(col))):
                board.set_value_cell(col,symb)
                if(board.winner(board.last_mov[0], board.last_mov[1], symb)):
                    board.clear_cell(board.last_mov[0], board.last_mov[1])
                    return board.last_mov[1]
                board.clear_cell(board.last_mov[0], board.last_mov[1])
        return -1