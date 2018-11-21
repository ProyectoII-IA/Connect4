# Package: model.strategies
# Description: Abstract class of strategies

# Artificial Intelligence, II Semester 2018
# Project: Connect 4 
# Author : Katerine Molina S. 
# E-mail: kanatalia95@gmail.com
# Version: 0.0.0 

#IMPORT SECTION
import random as rd


class Strategy: 
    #Attributes------------------------
    name: ""
    probability: ""
    # Methods--------------------------
    # @Method: GET_RANDOM_NUMBER
    # @Description: get random number using python random generator
    # @Return: number between 0 to 0.999 
    def get_random_number(self):
        return rd.random()

    # @Method:GET_ACTION
    # @Description: return new movement using the board as reference.
    # @return: array of numbers
    def get_action(self,board,array_number):
        pass

    # @Method: GET_STRATEGY
    # @Description: Get the strategy following the procedure assined in each strategy
    # @Parameter
    # @return strategy value
    def get_strategy(self):
        pass