# Package: model.game
# Description: structure of board

# Artificial Intelligence, II Semester 2018
# Project: Connect 4
# Author : Jonathan Martinez C.
# E-mail: jonathan.gerad@hotmail.com
# Version: 0.0.0

# IMPORT SECTION
import argparse
from ..model.game.agent import Agent
from ..model.game.human import Human
from ..model.game.player import Player



class Game_Controller():
    
    def __init__(self):
        self.player_1 = Player()
        self.player_2 = Player()

    # Methods-------------------------
    # @Method: CONFIG_PLAYERS
    # @Description: 
    def config_players(self):
        parser = argparse.ArgumentParser(description='Configuración del ' + 
                                        'Juego.')
        parser.add_argument("-gt", "--game-type", type=int,
                            help="Define el tipo de juego. ")
        parser.add_argument("-a1c", "--agent1c",type=str,
                            help="Características del agente 1")
        parser.add_argument("-a2c", "--agent2c",type=str,
                            help="Características del agente 2")                        
        parser.add_argument("-p1c", "--agentec", type=str,
                            help="Características del agente")
        args = parser.parse_args()

        # 0 -> H vs A, 1 -> A vs A
        # player 2 symbol = 2, and oponent = 1
        self.player_2 = Agent(2,1)
        if(args.game_type == 0):
            self.player_2.set_strategies(eval(args.agentec))
            self.player_1 = Human()
        else:
            self.player_2.set_strategies(eval(args.agent1c))
            self.player_1 = Agent(1,2)
            self.player_1.set_strategies(eval(args.agent2c))

    # Methods-------------------------
    # @Method: GET_CONFIG_PLAYERS
    # @Description: Return the players, and the game type
    def get_config_players(self):
        if(isinstance(self.player_1, Human)):
            return [self.player_1, self.player_2, 0]
        else:
            return [self.player_1, self.player_2, 1]