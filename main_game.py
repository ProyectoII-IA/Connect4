from model.game.board import Board
from model.strategies.position  import Number
from model.strategies.sequential_vs_space import SequentialvsSpace

from model.game.human import Human
from model.game.agent import Agent
from model.game.game import Game
from model.strategies.center_vs_extremity import Center_vs_extremity
from model.strategies.horizontal_vs_vertical import Horizontal_vertical

def main():


    b = [[0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0]]

    player_1 = Human()
    player_2 = Agent(2, 1) # 2 es el symb del agente, 1 el del oponente
    game = Game(player_1, player_2)
    game.play_game()
    #game.board.board = b
    #player_2.win(game.board, 1)
    #player_2.win(game.board, 1)
    #game.board.print_board()
"""
    b = [[0,1,2,0,0,0,0],
         [0,1,2,0,0,0,0],
         [0,1,2,0,0,0,0],
         [0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0]]

    board = Board()
    board.board = b

    array_number = []
    for i in range(0,7):
        var_number = Number(i)
        array_number.append(var_number)
    
    strategy = SequentialvsSpace(0.80,1)
    var_action = strategy.get_action(board,array_number)
    print(var_action)
    for x in var_action: 
        print(x.position,x.amount)
        
 

    print(board.get_empty_element(0))
    print(board.get_column(1))
    print(board.get_cells_symbol(2))
    print(board.is_fill_column(5))

    print(board.winner(3,1,1))

    b.reverse()
    for i in b:
        print(i)

    strategy = Center_vs_extremity()
    strategy.probability= 0.2
    array = [[0,0,0],[1,0,0],[2,0,0],[3,0,0],[4,0,0],[5,0,0],[6,0,0]]
    print(array[1][1])
    strategy.get_action(board, array)

    strategy = Horizontal_vertical()
    strategy.probability= 0.2
    array = [[0,0,0],[1,0,0],[2,0,0],[3,0,0],[4,0,0],[5,0,0],[6,0,0]]
    print(array[1][1])
    strategy.get_action(board, array)
"""

if __name__ == "__main__":
    main()


