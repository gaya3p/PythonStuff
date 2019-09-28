unit = input('Enter unit: ')
temp = float(input('Enter the temperature: '))

if unit == 'k':
    c = temp - 273.15
    f = (c*1.8) + 32
    print('Given temperature:', temp, 'K.')
    print('=', c, '⁰C')
    print('=', f, '⁰F')

elif unit == 'c':
    k = temp + 273.15
    f = (temp*1.8) + 32
    print('Given temperature:', temp, '⁰C.')
    print('=', k, 'K')
    print('=', f, '⁰F')
    
elif unit == 'f':
    c = round((temp-32)/1.8, 2)
    k = c + 273.15
    print('Given temperature:', temp, '⁰F.')
    print('=', c, '⁰C')
    print('=', k, 'K')
