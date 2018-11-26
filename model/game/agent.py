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
from ..strategies.blocking2_vs_1 import Blocking2vsBlocking1
from .player import Player
from .board import Board


class Agent(Player):

    strategies = [0.80, 0.80, 0.80, 0.80]

    def __init__(self, symb, symb_opp, automatic = False):
        self.symb = symb
        self.symb_opp = symb_opp
        self.automatic= automatic
        pass

    def next_action(self, board):
        win = self.win(board, self.symb)
        block = self.block(board, self.symb_opp)
        if (not self.automatic):
            continue_game = input("Presione una tecla para continuar: ")
        if (win >= 0):
            print("Ganar")
            col = win
        elif (block >= 0):
            print("Bloquear")
            col = block
        else:
            array_number = self.get_strategy(board)
            col = self.get_column_number(array_number)
        return col

    def get_strategy(self, board):
        array_number = self.get_array_number()
        #STRATEGY 1 -> SequentialvsSpace
        strategy = SequentialvsSpace(self.strategies[0], self.symb)
        array_number = strategy.get_action(board,array_number)
        #STRATEGY 2 -> Center_vs_extremity
        strategy_2 = Center_vs_extremity(self.strategies[1], self.symb)
        array_number = strategy_2.get_action(board, array_number)
        #STRATEGY 3 -> Horizontal_vertical
        strategy_3 = Horizontal_vertical(self.strategies[2], self.symb)
        array_number = strategy_3.get_action(board, array_number)
        #STRATEGY 3 -> Horizontal_vertical
        strategy_4 = Blocking2vsBlocking1(self.strategies[3], self.symb,self.symb_opp)
        array_number = strategy_4.get_action(board, array_number)
        return array_number

    def get_column_number(self, array_number):
        max_strategies = 0
        max_amount = 0
        col_number = 0
        for x in array_number: 
            if (x.strategies_number > max_strategies):
                max_strategies = x.strategies_number
        for x in array_number: 
            if (x.strategies_number == max_strategies):
                if (x.amount > max_amount):
                    max_amount = x.amount
                    col_number = x.position
        return col_number

    def get_array_number(self):
        array_number = []
        for i in range(0,7):
            var_number = Number(i)
            array_number.append(var_number)
        return array_number

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

    def set_strategies(self, strategies):
        self.strategies = strategies