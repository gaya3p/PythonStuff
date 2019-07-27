import random
a = 1
b = 100 # must be > a
tries = 1

print('Guessing Game')
print(f'Think of an integer between {a} & {b}.')
n = int(input('Enter the number : '))

guess = random.randint(1, 100)

lower = [1]
greater = [100]

while guess != n:
    print(guess)
    if guess > n:
        greater.append(guess)
        guess = random.randint(max(lower), min(greater))
    elif guess < n:
        lower.append(guess)
        guess = random.randint(max(lower), min(greater))
    tries += 1
    #guess = random.randint(1, 100)

print(f'The computer has guessed the correct number in {tries} tries.')