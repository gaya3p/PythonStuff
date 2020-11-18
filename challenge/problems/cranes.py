'''
You are playing a video game in which several stacks of boxes are lined up on the floor, 
with a crane on top to rearrange the boxes.

The crane supports the following commands:
• Move one position left (does nothing if already at the leftmost position)
• Move one position right (does nothing if already at the rightmost position)
• Pick up a box from the current stack (does nothing if the crane already has a box)
• Drop a box on the current stack (does nothing if the crane doesn't already have a box)

Further, there is a limit H on the number of boxes on each stack. If a 'drop' command would result in a stack having more than H boxes, the crane ignores this drop command. If the current stack has no boxes, a 'pick up' command is ignored.
You are given the initial number of boxes in each stack and the sequence of operations performed by the crane. You have to compute the final number of boxes in each stack.

        *
*       *
*   *   * 
* * * * * _ *
    Stacks

For example, suppose the initial configuration of the game is as shown in the figure above, with 7 stacks and H=4. Then, after the following sequence of instructions,
1. Pick up box
2. Move right
3. Move right
4. Move right
5. Move right
6. Drop box
7. Move left
8. Pick up box
9. Move left
10. Drop box

the number of boxes in each stack from left to right would be 2,1,3,1,4,0,1.

The commands are encoded as follows:
1 : Move left
2 : Move right
3 : Pick up box
4 : Drop box
0 : Quit

Sample input 1
7 4 -> number of stacks, max height
3 1 2 1 4 0 1 -> initial state
3 2 2 2 2 4 1 3 1 4 0 -> commands

Sample output 1
2 1 3 1 4 0 1

Sample input 2
3 5
2 5 2
3 2 4 2 2 2 1 4 1 1 1 1 0

Sample output 2
1 5 2 
'''

n, h = list(map(int, input().split()))
stacks = list(map(int, input().split()))
commands = list(map(int, input().split()))

pos = 0
curr = 0
for c in commands:
    if c == 0:
        break
    elif c == 1:
        pos = pos - 1 if pos > 0 else 0
    elif c == 2:
        pos = pos + 1 if pos < n-1 else n-1
    elif c == 3:
        if curr == 0 and stacks[pos] > 0:
            curr = 1
            stacks[pos] -= 1
    elif c == 4:
        if curr == 1 and stacks[pos] < h:
            curr = 0
            stacks[pos] += 1
    else:
        continue

print(' '.join(map(str, stacks)))
