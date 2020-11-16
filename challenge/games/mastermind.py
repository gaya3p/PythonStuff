import random

print('='*10, 'MASTERMIND', '='*10)
print('Try to guess the key made up of 4 unique digits in the range 1-6.\n')

def generate_key():
    digits = [1, 2, 3, 4, 5, 6]
    key = random.sample(digits, 4)
    return ''.join(map(str, key))

key = generate_key()
guess = input('Enter a guess: ')
tries = 12

while guess != key and tries > 0:
    if len(guess) == 4 and guess.isnumeric():
        rights = wrongs = 0
        tries -= 1
        
        for real_digit, guessed_digit in zip(key, guess):
            if real_digit == guessed_digit:
                rights += 1
        
        for digit in guess:
            if key.find(digit) > -1:
                wrongs += 1
        
        wrongs -= rights
        
        print(f'{tries}You are wrong.\nHint: -{wrongs} +{rights}\n')
        guess = input('Try again: ')
    else:
        guess = input('Enter a valid guess: ')
        
if guess == key:
    print(f'Yes, you win with {tries} points!')
else:
    print('You lose!\nThey key was', key)