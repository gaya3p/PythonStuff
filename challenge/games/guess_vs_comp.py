import random
a = 1
b = 1000 # must be > a
tries = 1

print('Guessing Game')
print(f'Think of an integer between {a} & {b}.')
n = int(input('Enter the number : '))
print('\nGuesses:')

guess = random.randint(a, b)

lower = [a]
greater = [b]

while guess != n:
    print(guess)
    if guess > n:
        greater.append(guess)
    elif guess < n:
        lower.append(guess)
    guess = random.randint(max(lower)+1, min(greater)-1)
    tries += 1
    #guess = random.randint(a, b)

print(f'\nThe computer has guessed the correct number in {tries} tries.')