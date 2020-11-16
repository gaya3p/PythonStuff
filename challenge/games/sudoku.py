from time import time
sudoku = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0,0]] 

def print_grid(grid):
    for i in range(9):
        if i%3 == 0:
            print('', '-'*37)
            
        for j in range(9):
            n = grid[i][j] if grid[i][j] != 0 else ' '
            if j%3 == 0:
                print(end=' | ')
                        
            print(f' {n} ', end='')
            if j == 8:
                print(end=' | ')
        
        print()
        if i == 8:
            print('', '-'*37)

def is_valid(grid, y, x, n):
    if n in grid[y]:
        return False

    for row in grid:
        if n == row[x]:
            return False
    
    q, p = ((y//3)*3), ((x//3)*3)
    for i in range(q, q+3):
        for j in range(p, p+3):
            if grid[i][j] == n:
                return False
    
    return True

def find_empty_position(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return False

def solve(grid):
    position = find_empty_position(grid)

    if not position:
        return True

    y, x = position

    for number in range(1, 10):
        if is_valid(grid, y, x, number):
            grid[y][x] = number
            if solve(grid):
                return True
            
            grid[y][x] = 0

    return False

if __name__ == '__main__':
    print_grid(sudoku)
    start_time = time()
    solve(sudoku)
    print(f'--- solved in {time() - start_time} seconds ---' % ())
    print_grid(sudoku)