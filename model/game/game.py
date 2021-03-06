# Package: model.game
# Description: Class to define the structure of the game

# Artificial Intelligence, II Semester 2018
# Project: Connect 4
# Author : Mariana Rojas S. 
# E-mail: mari.semeraro27@gmail.com
# Version: 0.0.0 

# IMPORT SECTION
from .board import Board
from .player import Player
from copy import deepcopy


class Game():

    def __init__(self, player_1, player_2):
        self.board = Board()
        self.player_1 = player_1
        self.player_2 = player_2
        self.turn_player_1 = False 

    def play_game(self):
        self.board.created_board()
        while (not self.is_winner()):
            if(self.board.is_full()):
                print("** Empate **")
                return
            self.turn_player_1 = not self.turn_player_1
            if (self.turn_player_1):
                print(self.turn("1"))
                col = self.player_1.next_action(deepcopy(self.board))
                self.board.set_value_cell(col, 1)
            else:
                print(self.turn("2"))
                col = self.player_2.next_action(deepcopy(self.board))
                self.board.set_value_cell(col, 2)
        print(self.who_is_winner())

    def turn(self, num_player):
        self.board.print_board()
        return "Turno del Jugador " + num_player

    def who_is_winner(self):
        print("** Se acabo el juego **")
        self.board.print_board()
        if (self.turn_player_1):
            return "** Ganador Jugador 1 **"
        else:
            return "** Ganador Jugador 2 **"

    def is_winner(self):
        last_mov = self.board.get_last_mov()
        if (self.turn_player_1):
            return self.board.winner(last_mov[0], last_mov[1], 1)
        else:
            return self.board.winner(last_mov[0], last_mov[1], 2)
