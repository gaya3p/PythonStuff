# Monte Carlo stimulation
from random import random
import math

inside = 0
a = 0
n = 100000

for i in range(n):
    x2 = random()**2
    y2 = random()**2

    if math.sqrt(x2 + y2) < 1:
        inside += 1

pi = (inside/n)*4
print(pi)
