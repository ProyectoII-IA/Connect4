# Package: model.strategies
# Description: 

# Artificial Intelligence, II Semester 2018
# Project: Connect 4 
# Author : Katerine Molina S. 
# E-mail: kanatalia95@gmail.com
# Version: 0.0.0 

#IMPORT SECTION
from model.strategies.position import Number
from model.strategies.strategy import Strategy

class Blocking2vsBlocking1(Strategy): 
    #Attributes------------------------
    name: ""
    probability: ""
    symbol  =  ""
    opponent_symbol = ""

    # Contructor----------------------
    def __init__(self, probability,symbol,opponent_symbol):
        self.probability =  probability
        self.name = "Sequential_vs_Space"
        self.symbol = symbol
        self.opponent_symbol = opponent_symbol
    # Methods-------------------------
    # @Method:GET_BLOCKERS
    # @Description: return all possible blockers near to opponent symbol
    # @return: array with tuples of columns
    def get_blockers(self,board, max_connect):
        array_blockers = []
        cols = board.get_cols()
        for col in range(cols):
            if(not(board.is_fill_column(col))):
                board.set_value_cell(col,self.opponent_symbol)
                if(board.winner(board.last_mov[0], board.last_mov[1],self.opponent_symbol,max_connect)):
                    board.clear_cell(board.last_mov[0], board.last_mov[1])
                    array_blockers.append(board.last_mov[1])
                board.clear_cell(board.last_mov[0], board.last_mov[1])
        return array_blockers

    # @Method: FILL_NUMBER_VALUE
    # @Description: set in the array of numbers the possible columns to choice
    # NOTE: the cost is 1, we can consider that this movement is important, and we can change this weight
    # @return: array of number object 
    def fill_numbers_value(self,array_blocker,array_number):
        for blocker in array_blocker:
            array_number[blocker].increase_amount() # cost of one
            array_number[blocker].increase_strategy()
        return array_number

    # @Method:GET_BLOCKING2_ACTION
    # @Description: get all possibilities of block the opponent with 2 sequential pieces
    # @return: array of numbers
    def get_blocking2_action(self,board,array_number):
        array_blockers = self.get_blockers(board,2)
        return self.fill_numbers_value(array_blockers,array_number)

    # @Method:GET_BLOCKING1_ACTION
    # @Description: get all possibilities of block the opponent when found any piece on the board 
    # @return: array of number object
    def get_blocking1_action(self,board,array_number):
        array_blockers = self.get_blockers(board,1)
        return self.fill_numbers_value(array_blockers,array_number)

    # @Method:GET_ACTION
    # @Description: return new movement using the board as reference.
    # @return: array of numbers
    def get_action(self,board,array_number):
        var_random =  self.get_random_number()
        if var_random < self.probability:
            return self.get_blocking2_action(board,array_number)
        else:
            return self.get_blocking1_action(board,array_number)

    # @Method: GET_STRATEGY
    # @Description: Get the strategy following the procedure assigned in each strategy
    # @Parameter
    # @return strategy value
    def get_strategy(self):
        return self.name