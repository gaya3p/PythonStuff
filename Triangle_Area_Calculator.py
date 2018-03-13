print("Hey! Gettin' your homework done? Well then...")
while True: # Love infinities..........
    try:

    #Taking the inputs
        a = float(input('Enter first side: '))
        
        b = float(input('Enter second side: '))
        
        c = float(input('Enter third side: '))
        

    #Checking if the triangle is valid by using the "Triangle Inequality Theorem" 
        if (a+b) > c and (b+c) > a and (c+a) > b :
            
            
    #Finding the area using Heron's formula...        
            s = (a + b + c) / 2
            area = ((s*(s-a)*(s-b)*(s-c)) ** 0.5)
            PrintableArea = str("%.2f" % area)   
            print('The area of the triangle is' , PrintableArea,  'square units.\n\n')

    #If it violates the "Triangle Inequality Theorem"...
        else:
            print("I swear by my protractor, this triangle is not possible.\n\n")

    except:
        print('\n\nYour input is not valid. :(\nPlease enter three different sides in three different lines.\n\n')
