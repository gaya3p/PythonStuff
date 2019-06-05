import matplotlib.pyplot as plt

x = [2, 4, 6, 8, 10]
y = [4,  9, 1, 7, 3]

x2 = [1,5,9,7,3, 15]
y2 = [9, 5, 6, 7, 1, 7]

plt.bar(x, y, label="bar 1", color='b')
plt.bar(x2, y2, label="bar 2", color='c')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Bars')
plt.legend()
plt.show()