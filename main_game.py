from model.game.board import Board
from model.strategies.position  import Number
from model.strategies.sequential_vs_space import SequentialvsSpace
def main():
    b = [[1,0,1,1,0,0,0],
         [0,0,0,1,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
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


if __name__ == "__main__":
    main()


