x = int(input('Enter 1st number: '))
y = int(input('Enter 2nd number: '))

a = max(x, y)
b = min(x, y)

while a % b != 0:
    a, b = b, (a % b)

hcf = b
lcm = int((x*y) / hcf)

print(f'HCF of {x} and {y} : {hcf}')
print(f'LCM of {x} and {y} : {lcm}')