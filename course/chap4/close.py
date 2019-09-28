a = float(input('Enter I number: '))
b = float(input('Enter II number: '))
a, b = min(a,b), max(a,b)

if a+0.001 >= b:
    print('Close')
else:
    print('Not close')
