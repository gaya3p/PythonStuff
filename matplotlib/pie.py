import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

slices = [30, 50, 14]
l = ['a', 's', 'd']
colors = ['b', 'r', 'g', 'y']
ex = [0, 0.1, 0.2]

plt.pie(slices, labels=l, explode=ex,shadow=True,
        startangle=90, autopct='%1.1f%%',
        wedgeprops={'edgecolor': 'black'})