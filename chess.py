# chess.py
#
# Implement a chess board
#
# Muhammad Nauman
# UIN: 927008027
# Oct 8 2018
# ENGR 102-213
#
# Lab 7b - 3

# Pre-processor
board = {"8": "RNBQKBNR",
         "7": "PPPPPPPP",
         "6": "........",
         "5": "........",
         "4": "........",
         "3": "........",
         "2": "pppppppp",
         "1": "rnbqkbnr"}
setup = board["8"] + "\n" + board["7"] + "\n" + board["6"] + "\n" + board["5"] + "\n" + board["4"] + "\n" + board["3"] + "\n" + board["2"] + "\n" + board["1"]
print(setup)
game = True
print()

# Processor
while game:
    move = input("Input a move in standard chess notation: ")
    move2 = ''
    if move[0] == "a":
        move2 += "0"
    elif move[0] == "b":
        move2 += "1"
    elif move[0] == "c":
        move2 += "2"
    elif move[0] == "d":
        move2 += "3"
    elif move[0] == "e":
        move2 += "4"
    elif move[0] == "f":
        move2 += "5"
    elif move[0] == "g":
        move2 += "6"
    elif move[0] == "h":
        move2 += "7"
    else:
        print("Incorrect move")
        exit()
    move2 += move[1]
    if move[2] == "a":
        move2 += "0"
    elif move[2] == "b":
        move2 += "1"
    elif move[2] == "c":
        move2 += "2"
    elif move[2] == "d":
        move2 += "3"
    elif move[2] == "e":
        move2 += "4"
    elif move[2] == "f":
        move2 += "5"
    elif move[2] == "g":
        move2 += "6"
    elif move[2] == "h":
        move2 += "7"
    else:
        print("Incorrect move")
        exit()
    move2 += move[3]

    if int(move[1]) > 8:
        print("Error: Piece non-existent")
        exit()
        game = False
    row = board[move[1]]
    piece = row[int(move2[0])]
    if piece == ".":
        print("Error: Piece non-existent")
        exit()
        game = False
    newrow = row[0:int(move2[0])] + "." + row[int(move2[0])+1:]
    board[move2[1]] = newrow
    row2 = row
    if int(move[3]) > 8:
        print("The piece will be moved off the board")
    else:
        row2 = board[move[3]]
    newrow2 = row2[0:int(move2[2])] + piece + row2[int(move2[2])+1:]
    board[move[3]] = newrow2
    setup = board["8"] + "\n" + board["7"] + "\n" + board["6"] + "\n" + board["5"] + "\n" + board["4"] + "\n" + board["3"] + "\n" + board["2"] + "\n" + board["1"]
    print(setup)
    print()
