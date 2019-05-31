str = input('Enter a string: ')
print('It\'s a palindrome.') if str == str[::-1] else print('It\'s not a palindrome.')