import os

def print_board(board, error_code=0):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('='*7, 'Tic Tac Toe', '='*7)

    if error_code == 1:
        print('The position is already occupied.\n')
    if error_code == 2:
        print('Invalid selection.\nEnter a value between 1-9.\n')
    
    print('-'*13)
    for i in range(0, 9, 3):
        print('|', end='')
        for j in range(3):
            item = board[j+i]
            if item == 0:
                piece = '   '
            else:
                piece = ' o ' if item == 1 else ' x '
            print(piece, end='|')
        print()
    print('-'*13)

def game_over(board):
    '''
    0 -> not over
    1 -> player 1 wins
    2 -> player 2 wins
    -1 -> tie
    '''

    # horizontals
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2]:
            return board[i]
    # verticals
    for i in range(3):
        if board[i] == board[i+3] == board[i+6]:
            return board[i]
    # diagonals
    if board[0] == board[4] == board[8]:
        return board[0]
    elif board[2] == board[4] == board[6]:
        return board[2]
    # check if all filled or not
    for i in board:
        if i == 0:
            return 0
    # all filled and its a tie
    return -1
    
def play(board):
    first_player_move = True

    while game_over(board) == 0:
        if first_player_move:
            print('Player 1\'s turn')
        else:
            print('Player 2\'s turn')

        try:
            pos = int(input('Enter position of your mark: '))
        except ValueError:
            pos = -1

        if 0 <= pos <= 9:
            if board[pos-1] == 0:
                board[pos-1] = 1 if first_player_move else 2
                first_player_move = False if first_player_move else True
                print_board(board)
            else:
                print_board(board, 1) 
        else:
            print_board(board, 2)

        res = game_over(board)
        if res > 0:
            print(f'Player {res} has won the game!')
            break
        elif res == -1:
            print('It\'s a tie.')
            break

    print('Game over')

def main():
    board = [0 for _ in range(9)]
    print_board(board)
    play(board)

if __name__ == '__main__':
    first_time = True
    main()
    while (input('Want to play again? (Y/N) ')).lower() == 'y':
        main()