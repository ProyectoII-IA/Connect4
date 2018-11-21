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

class SecuentialvsSpace(Strategy): 
    #Attributes------------------------
    name: ""
    probability: ""
    symbol  =  ""

    # Contructor----------------------
    def __init__(self, probability,symbol):
        self.probability =  probability
        self.name = "Secuential_vs_Space"
        self.symbol = symbol
    # Methods-------------------------
     # @Method:GET_SECUENTIAL_ACTION
    # @Description: return new movement using the board as reference.
    # @return: array of numbers
    def validate_secuential_position(self,row_prime,row):
        if row in [row_prime+1,row_prime-1,row_prime]:
            return True
        return False


    # @Method:GET_SECUENTIAL_ACTION
    # @Description: return new movement using the board as reference.
    # @return: array of numbers
    def get_secuential_action(self,board,array_number):
        array_positions =  board.get_cell_symbol(self.symbol)
        array_temp_position = []
        array_validated_positions = []
        for (row,col) in array_positions:
            for index in range(col-1,col+1):
                array_temp_position.append((board.get_empty_element(index),index))
            for (row_p,col_p) in array_temp_position:
                if validate_secuential_position(row_p,row):
                    array_validated_positions.append(col_p)
                    array_number[col_p].increase_amount()
        array_number = self.check_strategy_amount(array_validated_positions,array_number):
        return array_number 
            
                       

    # @Method:GET_ACTION
    # @Description: return new movement using the board as reference.
    # @return: array of numbers
    def get_action(self,board,array_number,symbol):
        var_random =  self.get_random_number()
        if var_random < self.probability:
            return self.get_secuential_action(board,array_number)
        else:
            return self.get_space_action(board,array_number)
        

    # @Method: GET_STRATEGY
    # @Description: Get the strategy following the procedure assined in each strategy
    # @Parameter
    # @return strategy value
    def get_strategy(self):
        pass