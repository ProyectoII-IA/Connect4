from model.game.board import Board
from model.strategies.center_vs_extremity import Center_vs_extremity
from model.strategies.horizontal_vs_vertical import Horizontal_vertical

def main():
    b = [[1,0,1,0,0,1,1],
         [1,0,1,0,0,1,1],
         [1,0,1,0,0,1,1],
         [1,0,1,0,0,0,1],
         [1,0,1,0,0,0,1],
         [1,0,0,0,0,0,1]]

    board = Board()
    board.board = b
 
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


if __name__ == "__main__":
    main()


