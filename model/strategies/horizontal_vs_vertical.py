# Package: model.strategies
# Description: Abstract class of strategies

# Artificial Intelligence, II Semester 2018
# Project: Connect 4
# Author : Mariana Rojas S. 
# E-mail: mari.semeraro27@gmail.com
# Version: 0.0.0 

# IMPORT SECTION
import random as rd


class Horizontal_vertical(Strategy): 
    # Attributes------------------------
    name: ""
    probability: ""
    # Methods--------------------------
    # @Method:GET_ACTION
    # @Description: return new movement using the board as reference.
    # @return: array of numbers

    def get_action(self, board, array_number):
        random = this.get_random_number()
        positions_symbol = board.get_cells_symbol()
        flags = [False, False, False, False, False, False, False]
        for row, column in positions_symbol:
            if (random <= this.probability):  # Horizontal (!column)
                for i in range(0, 7):
                    if !(i == column):
                        if !(board.is_full(i)):
                            array_number[i][2] += 1
                            flags[i] = True
            else:  # Vertical (column)
                if !(board.is_full(column)):
                    array_number[column][2] += 1
                    flags[column] = True

        for i in range(0, 7):
            if (flags[i]):
                array_number[i][1] += 1  # if column i satisfy the strategy
