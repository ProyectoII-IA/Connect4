# Package: model.game
# Description: Interface to define player behavior

# Artificial Intelligence, II Semester 2018
# Project: Connect 4
# Author : Katerine Molina S. 
# E-mail: kanatalia95@gmail.com
# Version: 0.0.0 

#IMPORT SECTION


class Player:
    
    # Abstract Methods--------------------------
    # @Method: NEXT_ACTION
    # @Description: get the next action on the board
    # @Return: number
    def next_action(self,board):
        pass
        
    # @Method: VALIDATE_ACTION
    # @Description: validate_action
    # @Return: boolean
    def validate_action(self,board,position):
        if (board.is_fill_column(position)):
            return False
        else:
            return True




