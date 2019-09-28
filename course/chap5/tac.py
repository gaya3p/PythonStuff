board = [' ' for i in range(9)]
board = ['x', ' ', 'o', 'x', 'o', 'o', 'o', ' ', ' ']

x = 'x'
o = 'o'

wins = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]

def showBoard(first):
    for i in range(1, 10, 3):
        for j in range(3):
            s = f' {i+j} |' if first else f' {board[i+j-1]} |'
            print(s, end='')
        print('\n------------')

def check(m):
    a = []
    for i in range(len(board)):
        if board[i] == m:
            a.append(i)
    print(a)
    
    for combination in wins:
        if tuple(a) == combination:
            return True
    return False

def combs(l, 3):
    
combs([2, 4, 5, 6], 3)
print('Place you mark on the index')
showBoard(False)
print(check('o'))
'''while True:
    a = int(input('Player A: '))
    board[a-1] = x
    check(x)'''
    
