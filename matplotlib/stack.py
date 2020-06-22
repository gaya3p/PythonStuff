import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

labels = [1, 2, 3]

plt.stackplot(minutes, player1, player3, player2
              , labels=labels)

plt.legend()