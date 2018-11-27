# Package: model.game.human
# Description: Class of human

# Artificial Intelligence, II Semester 2018
# Project: Connect 4
# Author : Mariana Rojas S. 
# E-mail: mari.semeraro27@gmail.com
# Version: 0.0.0 

# IMPORT SECTION
from .player import Player


class Human(Player):


    def __init__(self):
        pass

    def next_action(self, board):
        col = input("Ingrese la columna a jugar: ")
        try:
            col = int(col)
        except ValueError:
            return self.next_action(board)
        col = col - 1
        if (self.validate_action(board, col)):
            return col
        return self.next_action(board)
