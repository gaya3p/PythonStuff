a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

# Checking if the triangle is valid by using the "Triangle Inequality Theorem" 
if (a+b) > c and (b+c) > a and (c+a) > b :   
    # Finding the area using Heron's formula...        
    s = (a + b + c) / 2
    area = ((s*(s-a)*(s-b)*(s-c)) ** 0.5)
    area = str("%.2f" % area)   
    print('The area of the triangle is' , area,  'square units.')

# If it violates the "Triangle Inequality Theorem"...
else:
    print("This triangle is not possible.")