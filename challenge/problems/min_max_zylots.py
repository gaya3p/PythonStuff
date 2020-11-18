'''
Dave and Larry are about to travel abroad by plane. 
The local airport has a special "Choose Your Plane" offer. The offer's conditions are as follows:

1. it is up to a passenger to choose a plane to fly on;
2. if the chosen plane has x (x > 0) empty seats at the given moment, then the ticket for such a plane 
costs x zlotys.

Input
The first line contains two integers n and m — the number of passengers in the queue and the number of planes in the airport.
The next line contains m integers a1, a2, ..., am — ai stands for the number of empty seats in the i-th plane initially.

Output
Print  the maximum and the minimum number of zlotys that the airport administration can earn.

Input 1:
4 3
2 1 1
Output 1:
5 5

Input 1:
4 3
2 2 2
Output 1:
7 6
'''

n, m = [4, 3]#map(int, input().split())
c = [2, 3, 2]#list(map(int, input().split()))

c.sort()
w = []

for i in range(len(c)):
    for j in range(c[i],0,-1):
        w.append(j)

# max cost
w1=sorted(w, reverse=True)

print(sum(w1[:n]), sum(w[:n]))