import matplotlib.pyplot as plt

population_ages = [22, 55, 62, 21, 89, 67, 45, 90, 15, 10, 2, 95, 99, 5, 89, 56, 78, 23, 86, 45, 58, 69, 47, 54, 16, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 29, 27, 28, 35, 36, 37]
#ids= [x for x in range(len(population_ages))]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
n = len(population_ages)
median = sorted(population_ages)[int(n/2)]

plt.hist(population_ages, bins, histtype='bar', rwidth=1, edgecolor='black')

plt.axvline(median, color='red', label='Median', linewidth=2)

plt.style.use('fivethirtyeight')
#plt.tight_layout()
plt.xlabel('ages')
plt.ylabel('frequency')
plt.title('HIstogram')
plt.legend()
plt.show()