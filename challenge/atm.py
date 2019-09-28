notes = {
    50: 1,
    20: 5,
    10: 3,
}

dens = list(notes.keys())

def totalAmt():
    tot = 0
    for note in notes:
        tot += note * notes[note]
    return tot

withdraw = int(input('Enter amount to withdraw: '))

while withdraw <= totalAmt() >= 10:
    notes_used = {
        50: 0,
        20: 0,
        10: 0,
    }
    
    for den in dens:
        while withdraw >= den and notes[den] > 0:          
            notes_used[den] += 1
            notes[den] -= 1
            withdraw -= den
            
    if withdraw == 0:
        for den in dens:
            if notes_used[den] != 0:
                print(f'{den}-{notes_used[den]}', end=' ')
    else:
        print('Not enough cash')
        break
    
    print()
    
    if totalAmt() >= 10:
        withdraw = int(input('Enter amount to withdraw: '))
else:
    print('Not enough cash left.')