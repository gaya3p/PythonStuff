import random

print('Guessing Game')
print('The computer has guessed an integer between 1 and 100.')

n = random.randint(1,100)
guess = int(input('Guess the number: '))
tries = 1

while guess != n:
    tries += 1
    if n > guess:
        print('The number is larger than you think.')
    elif n < guess:
        print('The number is smaller than you think.')
    guess = int(input('Guess again: '))
    
print(f'Yes the  number is {n}.')
print(f'You have guessed it correctly in {tries} tries.')