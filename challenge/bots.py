'''ep 8
bot = [1]
def findBot(bot):
  if bot[:-1] == 1:
    bot
'''
  
'''Think like a coder ep 7
grid = [7, 12, 5, 10, 3, 5, 8, 11, 9, 11, 10]

l = len(grid)
energy = 0
temp = 0
n = max(grid)

def pillars(i):
  left = grid[:i+1]
  right = grid[i:]

  a, b = max(left), max(right)

  e = min(a, b) - grid[i] 
  return e

for i in range(1, l-1):
  temp = pillars(i)
  print(i, ':', temp)
  
  energy += temp

print(energy)'''

'''Think like a coder Ep 5'''
'''painting = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],]

n = len(painting)

for i in range(n):
  painting[i][i] = 1

for i, j in zip(range(n), range(n-1, -1, -1)):
  painting[i][j] = 1
  print(i, j)

for row in painting:
  print(row)'''

'''Think Like a coder Ep 3'''
'''from random import  shuffle
x = 15
i = 0

class Bot:
  def __init__(self, furnace, serial):
    self.serial = serial
    self.furnace = furnace

bots = [Bot(0, x)]

rands = [i for i in range(1, 11)]
shuffle(rands)

for i in range(10):
  a = rands[i]
  bots.append(Bot(x, a))
  x = a

for bot in bots:
  print(bot.furnace, bot.serial)

bot = bots[0]

while bot.furnace != 0:
  for x in bots:
    if x.serial == bot.furnace:
      bot = x

print(bot.serial)'''
