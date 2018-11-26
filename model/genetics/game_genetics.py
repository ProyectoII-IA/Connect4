# Package: model.game
# Description: Class to define the structure of the game

# Artificial Intelligence, II Semester 2018
# Project: Connect 4
# Author : Mariana Rojas S. 
# E-mail: mari.semeraro27@gmail.com
# Modified: Katerine Molina Sánchez
# Version: 0.0.1 

# IMPORT SECTION
from model.game.board import Board
from model.game.player import Player
from config.config import Config as cf 
from copy import deepcopy


class GameGenetics:

    def __init__(self, player_1, player_2):
        self.board = Board()
        self.player_1 = player_1
        self.player_2 = player_2
        self.turn_player_1 = False 

    def play_game(self):
        self.board.created_board()
        while (not self.is_winner()):
            if(self.board.is_full()):
                #print("Empate")
                return cf.TIE
            self.turn_player_1 = not self.turn_player_1
            if (self.turn_player_1):
                col = self.player_1.next_action(deepcopy(self.board))
                self.board.set_value_cell(col, 1)
            else:
                col = self.player_2.next_action(deepcopy(self.board))
                self.board.set_value_cell(col, 2)
        return self.who_is_winner()

    
    def who_is_winner(self):
        if (self.turn_player_1):
            return cf.WINNER_1
        else:
            return cf.WINNER_2

    def is_winner(self):
        last_mov = self.board.get_last_mov()
        if (self.turn_player_1):
            return self.board.winner(last_mov[0], last_mov[1], 1)
        else:
            return self.board.winner(last_mov[0], last_mov[1], 2)
