import matplotlib.pyplot as plt
import numpy as np
#matplotlib.use('Qt4Agg')

a = np.array([2, 8, 16, 21, 26, 39, 50, 55, 65, 75, 80])
b = np.array([3, 15, 18, 29, 32, 45, 52, 59, 49, 46, 30])
c = np.array([2, 10, 26, 32, 45, 25, 20, 40, 45, 45, 50])

plt.plot(a, b, 'go--', linewidth=2, markersize=3, label='c')
plt.plot(a, c, color='#191919', linewidth=3, linestyle=':')

d = 30

plt.fill_between(a, b, c,
                 where=(b >c),
                 interpolate=True, alpha=0.25)

plt.fill_between(a, b, c,
                 where=(b< c),
                 interpolate=True, alpha=0.25)

plt.style.use('fivethirtyeight')
plt.legend(['b', 'c'])
plt.tight_layout()
plt.show()
#fast, seaborn-paper, seaborn-poster, fivethirtyeight, seaborn-white, seaborn
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3])
y1 = np.array([0.8, 0.8, 0.2, 0.2])
y2 = np.array([0, 0, 1, 1])

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

ax1.set_title('interpolation=False')
ax1.plot(x, y1, 'o--')
ax1.plot(x, y2, 'o--')
ax1.fill_between(x, y1, y2, where=(y1 > y2), color='C0', alpha=0.3)
ax1.fill_between(x, y1, y2, where=(y1 < y2), color='C1', alpha=0.3)

ax2.set_title('interpolation=True')
ax2.plot(x, y1, 'o--')
ax2.plot(x, y2, 'o--')
ax2.fill_between(x, y1, y2, where=(y1 > y2), color='g', alpha=0.3,
                 interpolate=True)
ax2.fill_between(x, y1, y2, where=(y1 <= y2), color='r', alpha=0.3,
                 interpolate=True)
fig.tight_layout()

plt.show()'''



