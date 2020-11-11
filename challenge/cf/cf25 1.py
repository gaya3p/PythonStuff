from itertools import permutations
c, f = list(map(int, input().split()))

fs = {}
##    (1, 2): 10,
##    (1, 3): 24,
##    (2, 3): 2,
##    (2, 4): 15,
##    (3, 4): 7
##    }
for i in range(f):
    x, y, p = list(map(int, input().split()))
    fs[(x, y)] = p


l = [i for i in range(1, c+1)]
perms = list(permutations(l))

min_c = 0
costs = []

for path in perms:
    cost = 0
    f = True

    for i in range(c-1):
        t = (path[i], path[i+1])
        t2 = (path[i+1], path[i])
        
        if t in fs:
            cost += fs[t]

        elif t2 in fs:
            cost += fs[t2]

        else:
            f = False
            break
            
    else:
        if f:
            costs.append(cost)
        
# minimum cost
print(min(costs))
        

