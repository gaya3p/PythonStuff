from colored import fg, bg, attr
import os

# initialization
ROWS, COLUMNS = 4, 7 # should be < 10
board = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]

# colored pieces
RESET = attr(0)
PIECE = 'o'
A = fg(190) + PIECE + RESET
B = fg(198) + PIECE + RESET
C = fg(240) + PIECE + RESET

def print_board(board, error_code=0):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('==== Connect Four ====')

    if error_code == 1:
        print('Please enter a valid position in the range 1-6')
    elif error_code == 2:
        print('The column is filled. Pick another column.')

    print('\n     ', end='')
    for i in range(COLUMNS):
        print(i+1, end='  ')
    
    dashes = 3*COLUMNS + 2
    print('\n  +', '-'*dashes, '+', sep='')

    for i in range(len(board)):
        print(end='  |')
        for item in board[i]:
            if item == 0:
                print(' ', C, end='')
            else:
                ch = A if item == 1 else B
                print(' ', ch, end='')
        print('  |')
        
    print('  +', '-'*dashes, '+', sep='')

def game_over(board):
    for i in range(ROWS):
        for j in range(COLUMNS):
            if board[i][j] > 0:
                # diagonals
                try:
                    if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3]:
                        return board[i][j]
                except:
                    pass
                # horizontal
                try:
                    if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3]:
                        return board[i][j]
                except:
                    pass
                # vertical
                try:
                    if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j]:
                        return board[i][j]
                except:
                    pass

    for i in range(ROWS):
        for j in range(COLUMNS):
            if board[i][j] == 0:
                return 0

    return -1

def play(board):
    first_player_move = True

    while game_over(board) == 0:

        if first_player_move:
            print('Player 1\'s turn')
            piece = 1
        else:
            print('Player 2\'s turn')
            piece = 2
            # first_player_move = True

        try:
            column = int(input('Enter column to mark: ')) - 1
        except ValueError:
            print_board(board, error_code=1)
            continue
        
        if 0 <= column <= COLUMNS-1:
            filled = False
            # if valid check for occupied position
            for row in range(ROWS):
                if board[row][column] != 0:
                    
                    if row == 0: # if column is filled
                        filled = True
                        break

                    board[row-1][column] = piece
                    first_player_move = False if first_player_move else True
                    break
            
            else: # if empty add to bottom
                board[ROWS-1][column] = piece
                first_player_move = False if first_player_move else True

            if filled:
                print_board(board, error_code=2)
            else:
                print_board(board)

        else:
            print_board(board, error_code=1)
            continue

        res = game_over(board)
        if res > 0:
            print(f'Player {res} has won the game.')
            break
        elif res == -1:
            print('it\s a tie.')
            break

if __name__ == '__main__':
    print_board(board)
    play(board)