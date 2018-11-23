# Package: model.game.agent
# Description: Class of agent

# Artificial Intelligence, II Semester 2018
# Project: Connect 4
# Author : Mariana Rojas S. 
# E-mail: mari.semeraro27@gmail.com
# Version: 0.0.0 

# IMPORT SECTION
from ..strategies.position import Number
from ..strategies.strategy import Strategy
from ..strategies.sequential_vs_space import SequentialvsSpace
from ..strategies.center_vs_extremity import Center_vs_extremity
from ..strategies.horizontal_vs_vertical import Horizontal_vertical
from .player import Player
from .board import Board


class Agent(Player):

    strategies = [0.80, 0.80, 0.80]

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
            self.get_strategy(board)
            col = int(input("Ingrese la columna a jugar: "))
        return col

    def get_strategy(self, board):
        array_number = self.get_array_number()
        #strategy = SequentialvsSpace(self.strategies[0], self.symb)
        #array_number = strategy.get_action(board,array_number)
        strategy_2 = Center_vs_extremity(self.strategies[1], self.symb)
        array_number = strategy_2.get_action(board, array_number)
        strategy_3 = Horizontal_vertical(self.strategies[2], self.symb)
        array_number = strategy_3.get_action(board, array_number)
        return array_number

    def get_array_number(self):
        array_number = []
        for i in range(0,7):
            var_number = Number(i)
            array_number.append(var_number)
        return array_number

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