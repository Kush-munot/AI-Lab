import math


def printGrid(grid, rows, cols):
    print("Current instance of The game is -\n\n")
    for i in range(rows):
        print(grid[i])


def checkWinner(grid, x):

    if x == 1:
        ch = '#'
    else:
        ch = '*'

    # Horizontal Wins
    if (grid[0][0] == ch and grid[0][1] == ch and grid[0][2] == ch):
        return True

    if (grid[1][0] == ch and grid[1][1] == ch and grid[1][2] == ch):
        return True

    if (grid[2][0] == ch and grid[2][1] == ch and grid[2][2] == ch):
        return True

    # Vertical Wins
    if (grid[0][0] == ch and grid[1][0] == ch and grid[2][0] == ch):
        return True

    if (grid[0][1] == ch and grid[1][1] == ch and grid[2][1] == ch):
        return True

    if (grid[0][2] == ch and grid[1][2] == ch and grid[2][2] == ch):
        return True

    # Diagonal Wins
    if (grid[0][0] == ch and grid[1][1] == ch and grid[2][2] == ch):
        return True

    if (grid[0][2] == ch and grid[1][1] == ch and grid[2][0] == ch):
        return True

    return False


def checkValidity(x, y, rows, cols):

    if (x >= 0 and x < rows and y >= 0 and y < cols):
        return True
    else:
        return False


def printChoices(grid, rows, cols):

    lst = []

    for i in range(rows):
        for j in range(cols):
            if (grid[i][j] == '0'):
                pair = (i+1, j+1)
                lst.append(pair)

    if (len(lst) == 0):
        print("No Choices Available")
    else:
        print("Choices Available : ")
        print(*sorted(lst))


# Starting main code
if __name__ == "__main__":
    print("Welcome to Tic Tac Toe")

    rows = 3
    cols = 3

    grid = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]

    max_loops = 9
    currPlayer = 1
    currPlayerName = input("Enter Your Name: ")
    currPlayer_Symbol = '#'

    for chance in range(max_loops):

        print("\n")
        printGrid(grid, rows, cols)
        print("\n")

        print("Player ", currPlayer, " chance \n\n")

        printChoices(grid, rows, cols)
        x, y = input("Enter where you want to play : ").split()

        x = int(x)
        y = int(y)

        x = x-1
        y = y-1

        if (checkValidity(x, y, rows, cols) == False):
            print("Invalid input")
            continue

        if (grid[x][y] == '0'):
            grid[x][y] = currPlayer_Symbol if currPlayer == 1 else '*'

            if (checkWinner(grid, currPlayer) == True):
                print("Player ", currPlayerName if currPlayer ==
                      1 else 'Kush', " Won")
                break

            currPlayer = currPlayer % 2
            currPlayer = currPlayer+1
        else:
            print("Invalid input")

        max_loops -= 1

    if max_loops == 0:
        print(".........T  I  E.........")
