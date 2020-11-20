from tabulate import tabulate
a = [x for x in range(12)]
n = [x for x in range(1, 13)]

print(tabulate())
print('{:4} {:25.25} {:25.25} {:25.25} {:7}'.format(
            i+1, author, title, series, size
        ))