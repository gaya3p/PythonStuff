from itertools import permutations

rows = columns = 3
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]     

o = 'O'
x = 'X'

player1 = list()
player2 = list()
over = False

wins = [
    # horizontal
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),
    # vertical
    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),
    # digonal
    ((0, 0), (1, 1), (2, 2)),
    ((0, 2), (1, 1), (2, 0)),
]

char = 65

def printBoard():
    for i in range(rows+1):
        if i == 0:
            print('  | 1 | 2 | 3 |', end='')
        else:
            for j in range(columns+1):
                if j == 0:
                    print(chr(char+i-1), end=' | ')
                else:    
                    print(board[i-1][j-1], end=' | ')
        print()
    print()

def outOfRange(x, y):
    if x not in [0, 1, 2] or y not in [0, 1, 2]:
        return True
    else:
        return

def ifWon(stats):
    perms = list(permutations(stats, 3))
    for perm in perms:
        if perm in wins:
            return True
    else:
        return False
    

print('Tic-Tac-Toe')
print('Enter where to place your mark as [row][column]. Eg: 2c')
printBoard()

while True:
    m1 = input('First player: ').upper()
    m1row, m1column = int(m1[0]) - 1, ord(m1[1]) - char
    board[m1column][m1row] = x
    player1.append((m1column, m1row))
    if ifWon(player1):
        printBoard()
        print('\n**************\nPlayer A has won.')
        break
    else:
        printBoard()
    
    m2 = input('Second player: ').upper()
    m2row, m2column = int(m2[0]) - 1, ord(m2[1]) - char
    board[m2column][m2row] = o
    player2.append((m2column, m2row))
    if ifWon(player2):
        printBoard()
        print('\n**************\nPlayer B has won.')
        break
    else:
        printBoard()
