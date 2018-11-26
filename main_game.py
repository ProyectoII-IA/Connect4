# Package: 
# Description: Main of the game

# Artificial Intelligence, II Semester 2018
# Project: Connect 4
# Authors : Jonathan Martinez C., Katherine Molina S., Mariana Rojas Semeraro
# E-mail: jonathan.gerad@hotmail.com, kanatalia95@gmail.com, mari.semeraro27@gmail.com
# Version: 0.0.0

# IMPORT SECTION
from controllers.game_controller import Game_Controller

def main():
    controller_game = Game_Controller()
    controller_game.config_players()
    controller_game.play_game()

if __name__ == "__main__":
    main()   
