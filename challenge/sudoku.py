sudoku = [[5,0,0,0,1,0,0,0,0],
        [2,7,4,0,0,0,6,0,0],
        [0,8,0,9,0,4,0,0,0],
        [8,1,0,4,6,0,3,0,2],
        [0,0,2,0,0,0,1,0,0],
        [7,0,6,0,9,1,0,5,0],
        [0,0,0,5,0,3,0,1,0],
        [0,0,5,0,0,0,9,2,7],
        [1,0,0,0,2,0,0,0,3]]

def printGrid(grid):
    for i in range(9):
        if i%3 == 0:
            print('', '-'*37)
            
        for j in range(9):
            n = grid[i][j] if grid[i][j] != 0 else ' '
            if j%3 == 0:
                print(' | ', end='')
                        
            print(f' {n} ', end='')
            if j == 8:
               print(' |', end='') 
        
        print()
        if i == 8:
            print('', '-'*37)

def possible(grid, y, x, n):
    if n in grid[y]:
        return False
    for row in grid:
        if n == row[x]:
            return False
    
    q = ((y//3)*3)
    p = ((x//3)*3)
    
    for i in range(q, q+3):
        for j in range(p, p+3):
            if grid[i][j] == n:
                return False
    
    return True

def isSolved(grid):
    for row in grid:
        if 0 in row:
            return False
    return True

def solve(grid):
    for y in range(9):
        for x in range(9):
            n = grid[y][x]
            if n == 0:
                ps_vals = []
                for i in range(1, 10):
                    if possible(grid, y, x, i):
                        ps_vals.append(i)
                
                if len(ps_vals) == 1:
                    grid[y][x] = ps_vals[0]

                    
printGrid(sudoku)
c = 0
while not(isSolved(sudoku)):
    solve(sudoku)
    c += 1
    if c > 1000:
        print('This sudoku cannot be solved.')
        break
else:
    print()
    printGrid(sudoku)
    print(f'\nCount: {c}')