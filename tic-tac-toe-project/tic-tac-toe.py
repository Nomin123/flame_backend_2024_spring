board = []

# index=1
for index in range(1, 10):
    board.append(index)

print(board)

print("board layout")


def printBoard():
    print("\n")
    print("-------------")
    print("| " + str(board[0]) + " | " + str(board[1]) + " | " + str(board[2]) + " |")
    print("-------------")
    print("| " + str(board[3]) + " | " + str(board[4]) + " | " + str(board[5]) + " |")
    print("-------------")
    print("| " + str(board[6]) + " | " + str(board[7]) + " | " + str(board[8]) + " |")
    print("-------------")


printBoard()
Is_Current_One = True
won = False
while not won:
    printBoard()
    if Is_Current_One:
        print("Player X")
    else:
        print("Player O")
    inp = input(">")
    try:
        if inp == "done":
            break
        choice = int(inp)
    except:
        print("Please enter only valid fields from board (0-8)")

    if Is_Current_One:
        board[choice - 1] = "X"
    else:
        board[choice - 1] = "O"
    # code to toggle between True and False
    Is_Current_One = not Is_Current_One
    

    

    

    for pos_x in range(0, 3):
        pos_y = pos_x * 3
    # for row condition:
        if (board[pos_y] == board[(pos_y + 1)] and board[pos_y] == board[(pos_y + 2)]):
            printBoard()
            won = True
            
    # for column condition:
        if (board[pos_x] == board[(pos_x + 3)] and board[pos_x] == board[(pos_x + 6)]):
            printBoard()
            won = True
            
        if board[0]==board[4] and board[8]==board[0]:
            printBoard()
            won=True
            
        if board[2]==board[4] and board[6]==board[2]:
            printBoard()
            won=True
            

print("Player " + str(int(Is_Current_One + 1)) + " won, Congratulations!")
