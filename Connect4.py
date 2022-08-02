def print_board(board):
    extra_line = "     |     |     |     |"
    new_line = "-----|-----|-----|-----|-----"
    
    print(extra_line)

    for i in range(5):
        print(" ", board[i][0], " | ", board[i][1], " | ", board[i][2], " | ", board[i][3], " | ", board[i][4])
        print(new_line)

    print(extra_line)

def add_to_column():
    print("adding to column ...")


if __name__ == '__main__':
    print("Connect 4")

    array_1 = [[" ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " "],
               [" ", "B", "R", " ", " "],
               ["R", "B", "B", "R", " "]]

    array_2 = [[" ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " "],
               [" ", "B", "R", " ", " "],
               ["R", "B", "B", "R", " "]]

    print_board(array_1)

    add_to_column(array_1, 3, "R")
