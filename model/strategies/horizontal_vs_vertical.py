# Package: model.strategies
# Description: Abstract class of strategies

# Artificial Intelligence, II Semester 2018
# Project: Connect 4
# Author : Mariana Rojas S. 
# E-mail: mari.semeraro27@gmail.com
# Version: 0.0.0 

# IMPORT SECTION
from .position import Number
from .strategy import Strategy


class Horizontal_vertical(Strategy): 
    # Attributes------------------------
    name: ""
    probability: ""

    # Constructor----------------------
    def __init__(self, probability, symbol):
        self.probability =  probability
        self.name = "Horizontal_Vertical"
        self.symbol = symbol

    # Methods--------------------------
    # @Method:GET_ACTION
    # @Description: return new movement using the board as reference.
    # @return: array of numbers

    def get_action(self, board, array_number):
        random = self.get_random_number()
        positions_symbol = board.get_cells_symbol(1)
        flags = [False, False, False, False, False, False, False]
        for row, column in positions_symbol:
            if random <= self.probability:  # Horizontal (!column)
                for i in range(0, 7):
                    if not (i == column):
                        if not (board.is_fill_column(i)):
                            array_number[i].increase_amount(1) 
                            flags[i] = True
            else:  # Vertical (column)
                if not (board.is_fill_column(column)):
                    array_number[column].increase_amount(1) 
                    flags[column] = True

        for i in range(0, 7):
            if flags[i]:
                array_number[i].increase_strategy()
        return array_number
