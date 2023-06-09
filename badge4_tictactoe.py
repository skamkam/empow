# 2 gamemodes, one prints board every time and one doesnt
# dif gameboard sizes

def getsize():
    size = ""
    while (type(size) != int):
        try:
            size = int(input("How large do you want your tic-tac-toe board to be? Enter an integer >= 1: "))
        except:
            size = int(input("Not an integer, try again: "))
    return size

def createboard(size):
    board = []
    for r in range(size):
        row = []
        for c in range(size):
            row.append(" ") # initializes all entries with " "
        board.append(row) # adds the newly initialized row to the board
    return board

def printboard(board, size):
    divider = "-" * (4 * size) + "-"
    print(divider)
    for r in range(size):
        print("| ", end="")
        for c in range(size):
            print(board[r][c]+" | ", end="")
        print("\n" + divider)

def userplay(board, size, player):
    print("Player " + player + "'s turn.")
    user = input("Enter your row and column choice, from 1 to board of size. Example: 2 3 chooses second row, third column: ")
    usersplit = user.split(sep=" ")
    row = int(usersplit[0])
    col = int(usersplit[1])

    if board[row-1][col-1] != " ":
        user = input("Error, chose a spot that was already taken. Re-enter your row and column choice, from 1 to board of size: ")
        usersplit = user.split(sep=" ")
        row = int(usersplit[0])
        col = int(usersplit[1])

    board[row-1][col-1] = player
    return board

def checkwin(board, size, player):
    # diagonals
    diag = 0
    counterdiag = 0
    for i in range(size):
        if board[i][i] == player:
            diag+=1
        if board[i][size-i-1] == player:
            counterdiag+=1
        if diag==size or counterdiag==size:
            return True

    # horizontals/by row
    for i in range(size):
        horiz = 0
        for j in range(size):
            if board[i][j] == player: # counts how many in a row match the player
                horiz+=1
        if horiz==size:
            return True
    
    # verticals/by col
    for i in range(size):
        vert = 0
        for j in range(size):
            if board[j][i] == player: # counts how many in col match player
                vert+=1
        if vert==size:
            return True
    
    return False

def pvp(board, size):

    turns = size*size

    win = False
    player = "X"
    while not win:
        board = userplay(board, size, player)
        printboard(board, size)

        turns-=1
        win = checkwin(board, size, player)

        if win == True:
            print("Player " + player + " won!")
            raise SystemExit
        if win == False and player == "X":
            player = "O"
        elif win == False and player == "O":
            player = "X"
        if turns==0: # board is full and no one won
            print("Tie game, no one won.")
            raise SystemExit

def main():
    size = getsize()
    board = createboard(size)
    printboard(board, size)
    pvp(board, size)

if __name__ == "__main__":
    main()