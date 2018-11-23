# Package: model.strategies
# Description: structure of number

# Artificial Intelligence, II Semester 2018
# Project: Connect 4
# Author : Katerine Molina S. 
# E-mail: kanatalia95@gmail.com
# Version: 0.0.0 

#IMPORT SECTION


class Number:
    # Fields ----------------------------------
    position = 0 # position on the board
    strategies_number = 0 # each time that the number appear in each strategy
    amount = 0 # Repeated number amount

    # constructor-----------------------------
    def __init__(self,position):
        self.position = position
        self.strategies_number = 0
        self.amount = 0

    # Methods-------------------------
    # @Method: INCREASE_STRATEGY
    # @Description: Add 1 to strategy amount
    def increase_strategy(self,amount=1):
        self.strategies_number+=amount

    # Methods-------------------------
    # @Method: INCREASE_AMOUNT
    # @Description: Add 1 to  amount
    def increase_amount(self,amount=1):
        self.amount+=amount