from model.game.player import Player
from model.game.board import Board
#from model.strategies.blocking1_vs_2 import Blocking1_vs_2
#from model.strategies.center_vs_extremity import Center_vs_Extremity
#from model.strategies.horizontal_vs_vertical import Horizontal_vs_Vertical
#from model.strategies.sequential_vs_space import Sequential_vs_Space
#from model.strategies.strategy import Strategy 


class Agent(Player):

    strategies = []

    def __init__(self, symb, symb_opp):
        self.symb = symb
        self.symb_opp = symb_opp
        pass

    def next_action(self, board):
        win = self.win(board, self.symb)
        block = self.block(board, self.symb_opp)
        if (win >= 0):
            print("Ganar")
            col = win
        elif (block >= 0):
            print("Bloquear")
            col = block
        else:
            col = int(input("Ingrese la columna a jugar: "))
        return col

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