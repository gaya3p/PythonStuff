import matplotlib.pyplot as plt
from random import randint

x = [randint(1, 20) for x in range(20)]
y = [x for x in range(len(x))]
c = [randint(1,10) for i in range(len(x))]
s = [randint(40, 900) for i in range(len(x))]

plt.scatter(x, y, label="scats", c=c, marker='o', s=s)
#plt.scatter(c)

cbar = plt.colorbar()
cbar.set_label('Range')


plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot')
plt.legend()
plt.show()