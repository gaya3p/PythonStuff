'''
Identifiers:
\ used to escape a character
\d any number
\D anything but a number
\s space
\S anything but a space
\w any character
\W anything but a character
. any character except a new line
\. actually a period
\b whitespace around words

Modifiers:
{1,3} we're expecting 1-3
+ Match 1 or more
? Match 0 or 1
* Match 0 or more
$ match the end of a string
^ match the beginning of a string
| matches either or e.g. \d{1-3}|\w{5-6}
[] Match range or "variance" e.g. [A-Za-z] or [1-5a-qA-Z]
{x} expecting "x" amount

White Space Characters:
\n new line
\s space
\t tab
\e escape (rare)
\f form feed (rare)
\r return

Punctuators:
. + * ? [ ] $ ^ ( ) { } \ |
'''

import re

pattern = r'[78]\d{2}.\d{3}.\d{4}'
#matches = re.findall(pattern, s)

#print(matches)

def opea():
    return

with open('hp.txt', 'r') as f:
    contents = f.read()

def countFrequency(name):
    redPattern = re.compile(name)
    reds = redPattern.finditer(contents)
    
    i=0
    
    for red in reds:
        i +=  1
        #a, b = red.start(), red.end()
        #print(contents[a:b], i)
    
    print(f'f of {name}: {i}')

witches_and_wizards = ['Harry',
                       'Hermione',
                       'Ron',
                       'Lupin',
                       'Black',
                       'Snape',
                       r'Professor\s[A-Za-z]*\s',
                       r'Professor\s[A-Za-z]*\.',
                       ]

for person in witches_and_wizards:
    countFrequency(person)
    
while True:
    word = input('\nEnter a word: ')
    if not(word):
        break
    
blank = re.compile(r'[a-zA-Z]*\n')
blanks = blank.finditer(contents)