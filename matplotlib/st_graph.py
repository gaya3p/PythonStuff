import matplotlib.pyplot as plt

x = []
y = []
y2 = []

g = 9.81
u = 0
u2 = 50

for t in range(60):
    s = (u*t) + (0.5*g*t**2)
    s2 = (u2*t) + (0.5*g*t**2)
    
    x.append(t)
    y.append(s)
    y2.append(s2)

plt.plot(x, y, label='u = 0')
plt.plot(x, y2, label='u = 5')

plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')

plt.title('Free fall\nDisplacement Time Graph')
plt.legend()

plt.show()