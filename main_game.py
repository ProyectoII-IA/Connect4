from model.game.board import Board

def main():
    b = [[1,0,1,0,0,0,1],
         [1,0,0,0,0,0,1],
         [1,0,0,0,0,1,1],
         [1,0,0,1,0,0,1],
         [1,1,0,0,0,0,1],
         [1,0,0,0,1,0,1]]


    board = Board()
    board.board = b

 

    print(board.get_empty_element(0))
    print(board.get_column(0))
    print(board.get_cells_symbol(1))
    print(board.is_fill_column(6))


if __name__ == "__main__":
    main()


