# Package: model.strategies
# Description: 

# Artificial Intelligence, II Semester 2018
# Project: Connect 4 
# Author : Katerine Molina S. 
# E-mail: kanatalia95@gmail.com
# Version: 0.0.0 

#IMPORT SECTION
from .position import Number
from .strategy import Strategy

class SequentialvsSpace(Strategy): 
    #Attributes------------------------
    name: ""
    probability: ""
    symbol  =  ""
    last_validated_position =  []

    # Contructor----------------------
    def __init__(self, probability,symbol):
        self.probability =  probability
        self.name = "Sequential_vs_Space"
        self.symbol = symbol
        self.last_validated_position = []
    # Methods-------------------------
     # @Method:VALIDATE SECUENTIAL POSICION
    # @Description: validate if each position given is right
    # @return: Boolean
    def validate_sequential_position(self,row_prime,row):
        if row_prime == -1:
            return False
        if row in [row_prime+1,row_prime-1,row_prime]:
            return True
        return False

    # @Method:GET_NEIGHBORS
    # @Description: return all neighbors close to own element on the board
    # @return: array with tuples of neighbors
    def get_neighbors(self,board):
        array_neighbors = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0)] #Array of numbers
        array_positions =  board.get_cells_symbol(self.symbol)
        array_temp_position = []
        for (row,col) in array_positions:
            for index in range(col-1,col+2): 
                array_temp_position.append((board.get_empty_element(index),index))
            for (row_p,col_p) in array_temp_position: #row prime and column prime
                if self.validate_sequential_position(row_p,row): # row validation
                    (temp_col,temp_amount) = array_neighbors[col_p]
                    array_neighbors[col_p] = (temp_col,temp_amount+1)
            array_temp_position.clear()
        return array_neighbors

    # @Method:GET_SEQUENTIAL_ACTION
    # @Description: return new movement using the board as reference.
    # @return: array of numbers
    def get_sequential_action(self,board,array_number):
        array_neighbors = self.get_neighbors(board)
        for neighbor in array_neighbors:
            if neighbor[1]!=0:
                array_number[neighbor[0]].increase_amount(neighbor[1]) # cost of one
                array_number[neighbor[0]].increase_strategy()
        return array_number

    # @Method:GET_SPACE_ACTION
    # @Description: return new movement using the board as reference.
    # @return: array of numbers
            
    def get_space_action(self,board,array_number):
        array_neighbors = self.get_neighbors(board)
        for neighbor in array_neighbors:
            if neighbor[1]==0:
                array_number[neighbor[0]].increase_amount()
                array_number[neighbor[0]].increase_strategy()
        return array_number


    # @Method:GET_ACTION
    # @Description: return new movement using the board as reference.
    # @return: array of numbers
    def get_action(self,board,array_number):
        var_random =  self.get_random_number()
        if var_random < self.probability:
            return self.get_sequential_action(board,array_number)
        else:
            return self.get_space_action(board,array_number)
        

    # @Method: GET_STRATEGY
    # @Description: Get the strategy following the procedure assigned in each strategy
    # @Parameter
    # @return strategy value
    def get_strategy(self):
        self.name