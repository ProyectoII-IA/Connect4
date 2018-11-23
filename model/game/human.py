from .player import Player


class Human(Player):


    def __init__(self):
        pass

    def next_action(self, board):
        col = int(input("Ingrese la columna a jugar: "))
        if (self.validate_action(board, col)):
            return col
        return self.next_action(board)
    
    def validate_action(self, board, col):
        if (board.is_fill_column(col)):
            return False
        else:
            return True

        