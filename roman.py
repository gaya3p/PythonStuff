romanKeys = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1
}

def toRoman(n):
    roman = ''
    for key in romanKeys:
        while n >= romanKeys[key]:
            roman += key
            n -= romanKeys[key]
    return roman

print(toRoman(3888))
