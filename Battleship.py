def print_board(board):
    extra_line = "     |     |     |     |"
    new_line = "-----|-----|-----|-----|-----"
    
    print(extra_line)

    for i in range(5):
        print(" ", board[i][0], " | ", board[i][1], " | ", board[i][2], " | ", board[i][3], " | ", board[i][4])
        print(new_line)

    print(extra_line)


def place_ship():
    print("placing ship ...")



if __name__ == '__main__':
    print("Battleship")

    array_1 = [["S", " ", " ", " ", " "],
               ["S", " ", " ", " ", " "],
               [" ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " "]]

    array_2 = [[" ", " ", " ", " ", " "],
               [" ", " ", " ", "S", "S"],
               [" ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " "]]

    print_board(array_1)
    
    place_ship(array_1, 15, "R")
