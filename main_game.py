from model.game.board import Board
from model.strategies.position  import Number
from model.strategies.sequential_vs_space import SequentialvsSpace

from model.game.human import Human
from model.game.agent import Agent
from model.game.game import Game
from model.strategies.center_vs_extremity import Center_vs_extremity
from model.strategies.horizontal_vs_vertical import Horizontal_vertical
from model.strategies.blocking2_vs_1 import Blocking2vsBlocking1

def main():

    b = [[1, 0, 1, 2, 1, 1, 0],
     [2, 0, 0, 2, 1, 2, 0],
     [1, 0, 0, 1, 2, 2, 0],
     [2, 0, 0, 0, 1, 0, 0],
     [2, 0, 0, 0, 1, 0, 0],
     [1, 0, 0, 0, 2, 0, 0]]

    board = Board()
    board.board = b

    array_number = []
    for i in range(0,7):
        var_number = Number(i)
        array_number.append(var_number)

    strategy = Blocking2vsBlocking1(0,1,2)
    array_blocker = [3, 5, 6]
    var_action = strategy.fill_numbers_value(array_blocker,array_number)
    print("***")
    for x in var_action: 
        print(x.position,x.amount, x.strategies_number)
""" 
    player_1 = Agent(1, 2, False)
    player_2 = Agent(2, 1) # 2 es el symb del agente, 1 el del oponente
    game = Game(player_1, player_2)
    game.play_game()
    
    b = [[0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0]]

    player_1 = Human()
    player_2 = Agent(2, 1) # 2 es el symb del agente, 1 el del oponente
    game = Game(player_1, player_2)  """

    #game.play_game()
    #game.board.board = b
    #player_2.win(game.board, 1)
    #player_2.win(game.board, 1)
    #game.board.print_board()
    
"""  
    b = [[0,0,1,2,1,0,0],
         [0,0,0,1,1,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [1,1,1,1,1,1,1]]

    board = Board()
    board.board = b

    array_number = []
    for i in range(0,7):
        var_number = Number(i)
        array_number.append(var_number)


    strategy = Blocking2vsBlocking1(0.01,1,2)
    var_action = strategy.get_action(board,array_number)
    print("***")
    for x in var_action: 
        print(x.position,x.amount, x.strategies_number)
  
    strategy = SequentialvsSpace(0.80,1)
    var_action = strategy.get_action(board,array_number)
    print("***")
    for x in var_action: 
        print(x.position,x.amount, x.strategies_number)

    strategy_2 = Center_vs_extremity(0.8, 1)
    var_action = strategy_2.get_action(board, array_number)
    print("***")
    for x in var_action: 
        print(x.position,x.amount, x.strategies_number)

    strategy_3 = Horizontal_vertical(0.8, 1)
    var_action= strategy_3.get_action(board, array_number)
    print("***")
    for x in var_action: 
        print(x.position,x.amount, x.strategies_number)  """
    
   

if __name__ == "__main__":
    main()


