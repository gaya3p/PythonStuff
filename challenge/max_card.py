'''
Alice and Bob are very good friends. They keep on playing some strange games. Today Alice came up with a new game, in which each player gets N cards at the start. Each card has it's value printed on it.
The game proceeds as each player chooses a random card and shows it's value. The player having card with higher value wins. 

As Alice came up with this game, he wants to ensure his win. So he starts to increase value of some cards using an algorithm. 
To increase the value of a card by 1, the running time of algorithm is K seconds.
Find the minimum running time of algorithm, ensuring the win of Alice.

Input:
First line of input contains an integer N denoting the number of TestCases.
First line of Each testcase contains two Integers N and K.
Next two lines of each TestCase contains N integers, each denoting value of cards of Alice and Bob respectively.
    
Output:
Print a single line for each TestCase, running time of algorithm to ensure the win for Alice.   

'''

N = int(input())

for _ in range(N):
    _, time = list(map(int, input().split()))
    alice = list(map(int, input().split()))
    bob = list(map(int, input().split()))
    t = 0
    m = max(bob)
    for a in alice:
        if a <= m:
            t += m - a + 1
    print(time*t)