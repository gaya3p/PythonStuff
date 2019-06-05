string = input('Enter a string: ')
print('It\'s a palindrome.') if string == string[::-1] else print('It\'s not a palindrome.')