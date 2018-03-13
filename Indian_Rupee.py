try:

    money = round(float(input('Amount: ')), 2)

    # % returns the remainder...
    # // returns the quotient

    # DEN MAENS DENOMINATION

    if money >= 2000:
        den2k = 0
        if money < 4000:
            den2k += 1
        else:
            den2k = den2k + (money // 2000)#Returns the quotient
        
        money = money % 2000
        print("2000  x ", int(den2k), ' = ', (2000*int(den2k)))
        
    if money >= 500 and money < 2000:
        denCC = 0
        if money < 1000:
            denCC += 1
        else:
            denCC +=  (money//500)
            
        money = money - (denCC*500)
        print("500   x ", int(denCC), ' = ', (500*int(denCC)))
      

    if money >= 100 and money < 500:
        denD = 0
        if money < 200:
            denD += 1
        else:
            denD += (money//100)
        print("100  x ", int(denD), ' = ', (100*int(denD)))
        money = money - (denD*100)
        

    if money >= 50 and money < 100:
        denC = 0
        if money < 100:
            denC += 1
        else:
            denC += (money // 50)
        print("50   x ", int(denC), ' = ', (50*int(denC)))
        money = money - (denC*50)
        
        
    if money >= 20 and money < 50:
        denL = 0
        if money < 40:
            denL += 1
        else:
            denL += (money // 20)
        print("20  x ", int(denL), ' = ', (20*int(denL)))
        money = money - (denL*20)

        
    if money >= 10 and money < 20:
        denXX = 0
        if money < 20:
            denXX += 1
        else:
            denXX = denXX + (money // 10)
        print("10  x ", int(denXX), ' = ', (10*int(denXX)))
        money = money - (denXX*10)

     
    if money >= 5 and money < 10:
        denX = 0
        if money < 10:
            denX += 1
        else:
            denX = denX + (money // 5)
        print("5   x ", int(denX), ' = ', (5*int(denX)))
        money = money - (denX*5)

    if money >= 2 and money < 5:
        denV = 0
        if money < 4:
            denV += 1
        else:
            denV = denV + (money // 2)
        print("2  x ", int(denV), ' = ', (2*int(denV)))
        money = money - (denV*2)
        
    if money >= 1 and money < 2:
        denII = 0
        if money < 2:
            denII += 1
        else:
            denII = denII + (money // 1)
        print("1  x ", int(denII), ' = ', int(denII))
        print(denII)
        money = money - (denII*1)

    '''    
    if money < 1:
        denI = 0
        denI += money // 1
        print("Rest ~", denI)
    '''

except ValueError:
    print('You have to enter a valid \'Number\'.')

except:
    print('Oops! I (Python) think the program crashed. If you\'re seeing this,  please contact me(Not Python!).')

