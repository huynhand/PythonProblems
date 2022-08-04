def complete_box(array):
    print("counting completed boxes ...")
    
    box_count = 0

    for i in range (len(array)):
        for j in range (len(array[i])):
            if i == len(array) - 1 or j == (len(array[i+1]) - 1):
                break
            if array[i][j] == '_' and array[i+1][j] == '|' and array[i+1][j+1] == '|':
                box_count = box_count + 1

    return box_count

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

    array_3 = [["_", "_", "_"],
               ["|", "|", "|", "|"],
               ["_", "_", "_"],
               ["|", "|", "|", "|"],
               ["_", "_", "_"]]

    print(complete_box(array_2))

    print(complete_box(array_1))

    print(complete_box(array_3))
