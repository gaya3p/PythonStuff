#solution 3
n, m = [4, 3]#list(map(int, input().split()))
l = [2, 2, 2]#list(map(int, input().split()))

def sumUpto(no):
    c = 0
    for i in range(1, no+1):
        c += i
    return c

def maxcost(ls,no):
    ls = list(ls)
    cost = 0
    while no > 0:
        for i in range(len(ls)):
            if ls[i] < no:
                cost += sumUpto(no)
                no -= ls[i]
                ls[i] = 0
##                print(ls[i], no)
                if no == 0:
                    return cost
                continue

            if ls[i] == no:
                cost += sumUpto(ls[i])
                no -= ls[i]
                return cost
            
            else:
                cost += sumUpto(ls[i]) - sumUpto(ls[i] - no)
                return cost
             
    return cost

def mincost(ls, no):
    ls = list(ls)
    cost = 0
    while no > 0:
        for i in range(len(ls)):
            cost += ls[i]
            ls[i] -= 1
            no -= 1
            if no == 0:
                return cost
##        print(ls)
    return cost
       

print(mincost(l, n), end=' ')
print(maxcost(l, n))
