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

    # Methods-------------------------
    # @Method: INCREASE_STRATEGY
    # @Description: Add 1 to strategy amount
    def increase_strategy(self):
        self.strategies_number+=1

    # Methods-------------------------
    # @Method: INCREASE_AMOUNT
    # @Description: Add 1 to  amount
    def increase_amount(self):
        self.amount+=1