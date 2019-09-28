print('Enter a for calculating amount, p for principal, i for interest, r for rate and t for time\n')
choice = (input('Enter your choice: ')).lower()

if choice == 'a' :
    p = float(input('Principal: '))
    r = float(input('Rate per annum: '))
    t = float(input('Time in years: '))

    a = round(p*(1+(r/100))**t, 2)
    print('Amount:', a)

elif choice == 'p':
    a = float(input('Amount: '))
    r = float(input('Rate per annum: '))
    t = float(input('Time in years: '))

    p = round(a / (1+(r/100))**t, 2)
    print('Principal:', p)

