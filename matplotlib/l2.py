from matplotlib import pyplot as plt

ages = [2, 8, 16, 21, 26, 39, 50, 55, 65, 75, 80]
py_salaries =  [3, 15, 18, 29, 32, 45, 52, 59, 49, 46, 30]
dev_salaries = [2, 10, 26, 32, 45, 25, 20, 40, 45, 45, 50]

plt.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

plt.plot(ages, py_salaries, label='Python')

overall_median = 57287

plt.fill_between(ages, py_salaries, dev_salaries,
                 where=(py_salaries > dev_salaries),
                 interpolate=True, alpha=0.25, label='Above Avg')

plt.fill_between(ages, py_salaries, dev_salaries,
                 where=(py_salaries <= dev_salaries),
                 interpolate=True, color='red', alpha=0.25, label='Below Avg')

plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()
