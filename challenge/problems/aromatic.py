keys = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

s = '3X2I4X'
n = 0

for i, char in enumerate(s):
    if char == s[-1]:
        n += int(s[i -1]) * keys[char]
    else:
        if char.isalpha():
            k = int(s[i -1]) * keys[char]
            if keys[char] < keys[s[i + 2]]:
                n -= k
            else:
                n += k

print(n)
