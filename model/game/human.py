from .player import Player


class Human(Player):


    def __init__(self):
        pass

    def next_action(self, board):
        col = int(input("Ingrese la columna a jugar: "))
        col = col - 1
        if (self.validate_action(board, col)):
            return col
        return self.next_action(board)
