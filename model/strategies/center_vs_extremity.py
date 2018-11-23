# Package: model.strategies
# Description: Abstract class of strategies

# Artificial Intelligence, II Semester 2018
# Project: Connect 4
# Author : Mariana Rojas S. 
# E-mail: mari.semeraro27@gmail.com
# Version: 0.0.0 

# IMPORT SECTION
import random as rd
from model.strategies.strategy import Strategy

class Center_vs_extremity(Strategy): 
    # Attributes------------------------
    name: ""
    probability: ""

    # Constructor----------------------
    def __init__(self, probability, symbol):
        self.probability =  probability
        self.name = "Center_vs_Extremity"
        self.symbol = symbol

    # Methods--------------------------
    # @Method:GET_ACTION
    # @Description: return new movement using the board as reference.
    # @return: array of numbers

    def get_action(self, board, array_number):
        random = self.get_random_number()
        center_columns = [2, 3, 4]
        extremity_columns = [0, 1, 5, 6]
        columns = []
        if random <= self.probability:  # Center (2, 3, 4)
            columns = center_columns
        else:  # Extremity (0, 1, 5, 7)
            columns = extremity_columns
        for i in columns:
                if not (board.is_fill_column(i)):
                    array_number[i].increase_amount() 
                    array_number[i].increase_strategy()
        return array_number
