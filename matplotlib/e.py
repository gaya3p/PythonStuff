import matplotlib.pyplot as plt

x = [x/100 for x in range(50, 350, 10)]
y = [x/100 for x in range(250, 550, 10)]

def distance(x1, y1, x2 , y2):
    d2 = (x1-x2)**2 + (y1-y2)**2
    return d2**0.5

plt.scatter(3, 2)
plt.scatter(5, 2)

plt.scatter(x, y)

plt.show()