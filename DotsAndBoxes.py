def print_board(board):
    print("\n")
    for i in range(5):
        if i%2 == 0:
            print (".", board[i][0], ".", board[i][1], ".", board[i][2], ".")
        else:
            print (board[i][0], " ", board[i][1], " ", board[i][2], " ", board[i][3])
    print("\n")


def complete_box():
    print("counting completed boxes ...")

if __name__ == '__main__':
    print("Dots and Boxes")

    array_1 = [["_", "_", "_"],
               ["|", "|", " ", "|"],
               ["_", " ", " "],
               ["|", " ", " ", " "],
               [" ", " ", " "]]

    array_2 = [["_", "_", "_"],
               ["|", "|", "|", "|"],
               ["_", "_", "_"],
               ["|", "|", " ", " "],
               ["_", " ", " "]]

    print_board(array_1)

    complete_box(array_1)


