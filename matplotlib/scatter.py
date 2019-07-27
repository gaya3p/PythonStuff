import matplotlib.pyplot as plt

x = [8.4,8.4,7.9,8.3,8.1,8.5,8.3,8.4, 9, 0, 6, 5, 9, 9, 3, 6, 7, 8, 9]
y = [x for x in range(len(x))]

plt.scatter(x, y, label="scats", color='k', marker='x', s=100)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot')
plt.legend()
plt.show()