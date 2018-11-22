from model.game.player import Player


class Human(Player):


    def __init__(self):
        pass

    def next_action(self):
        col = int(input("Ingrese la columna a jugar: "))
        return col

        