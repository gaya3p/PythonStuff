key = input('Enter the answer: ')
guess = input('Enter a guess: ')

tries = 12
rights = 0
wrongs = 0

while guess != key or tries == 0:
    rights = wrongs = 0
    tries -= 1
    
    for real_digit, guessed_digit in zip(key, guess):
        if real_digit == guessed_digit:
            rights += 1
    
    for digit in guess:
        if key.find(digit) > -1:
            wrongs += 1
    
    wrongs -= rights
    
    print(f'You are wrong.\nHint: -{wrongs} +{rights}')
    guess = input('Try again: ')

if guess == key:
    print(f'Yes, you win with {tries} points!')
else:
    print('You lose!')