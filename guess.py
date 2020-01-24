import random

start = 0
end = 1492
n = random.randint(start, end)
tries = 1

print('Guessing Game')
print(f'The computer has guessed an integer between {start} and {end}.')
guess = int(input('Guess the number: '))

while guess != n:
    tries += 1
    if n > guess:
        print('The number is larger than you think.')
    elif n < guess:
        print('The number is smaller than you think.')
    guess = int(input('Guess again: '))
    
print(f'Yes the  number is {n}.')
print(f'You have guessed it correctly in {tries} tries.')