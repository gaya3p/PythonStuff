import matplotlib.pyplot as plt
import numpy as np

xIndex = np.arange(6)
w = 0.4

x = [chr(x) for x in range(65, 71)]
y = [4, 9, 1, 7, 3, 5]
y2 = [9, 5, 6, 7, 1, 7]

''' HORIZONTAL
plt.barh(xIndex - w/2, y, label="bar 1", height=w, color='b')
plt.barh(xIndex + w/2, y2, label="bar 2", height=w, color='c')

plt.yticks(xIndex, x)'''

plt.bar(xIndex - w/2, y, label="bar 1", width=w, color='b')
plt.bar(xIndex + w/2, y2, label="bar 2", width=w, color='c')

plt.xticks(xIndex, x)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Bars')
plt.legend()
plt.show()