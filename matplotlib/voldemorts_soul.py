import matplotlib.pyplot as plt

slices = [2**x for x in range(8, 0, -1)]
horcruxes = ['Riddle\'s Diary',
             'Gaunt\'s Ring',
             'Hufflepuff\'s Cup',
             'Slytherin\'s Locket',
             'Ravenclaw\'s Diadem',
             'Harry Potter',
             'Nagini',
             'His Body']
explode = (0, 0, 0, 0, 0, 0.1, 0.2, 0.3)
colors = ['#a64264', '#f9a602', '#eee117', '#0d6217', '#000a90', '#b8161c', '#202b40', '#98d9a8']

plt.pie(slices,
        startangle=45,
        explode=explode,
        colors=colors,
        autopct='%1.1f%%',
        shadow=True)

plt.legend(horcruxes, loc='lower left')
plt.axis('equal')
#plt.tight_layout()
plt.title('% of Voldemort\'s soul\nin different stuff')
plt.show()
