h = int(input('Enter hour  b/w 1-12: '))
a = int(input('How many hours ahead: '))

b = h + a
b = b%12

print(f'Time would be {b} o\'clock')
