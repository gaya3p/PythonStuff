days = {
    'january': 31, 
    'february': 28,
    'march': 31,
    'april': 30,
    'may':31,
    'june': 30,
    'july':31, 
    'august': 31,
    'september': 30,
    'october': 31,
    'november': 30,
    'december': 31,
}

vals = list(days.values())

for i in range(len(set(vals))):
    #min_val = min(vals)

    for m, d in days.items():
        min_val = min(vals)
        if d == min_val:
            print(m)
            vals.remove(min_val)
    

'''month = input('Enter a month: ')
print(days.get(month, 'Invalid month.'))

for m, d in days.items():
    if d == 31:
        print(m)
        
months = sorted(list(days.keys()))
print(months)'''