from .player import Player


class Human(Player):


    def __init__(self):
        pass

    def next_action(self, board):
        col = int(input("Ingrese la columna a jugar: "))
        return col

        