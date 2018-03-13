from xxkcd import xkcd, WhatIf
try:
    def printKcd(x):
        print(x.transcript)


    x = int(input('Your XKCD pass please...  ' ))

    x = xkcd(x)

    printKcd(x)

except:
    print('\nThere is no such XKCD article.')
    
'''
 print(x.title)
Python
>>> print(x.alt)
I wrote 20 short programs in Python yesterday.  It was wonderful.  Perl, I'm leaving you.
>>> what_if = WhatIf(1)
>>> print(what_if.title)
Relativistic Baseball
>>> print(what_if.question)
What would happen if you tried to hit a baseball pitched at 90% the speed of light?
>>> print(what_if.attribute)
- Ellen McManis
from xxkcd import xkcd, WhatIf
# Get random comic
xkcd.random()

# Get number of latest comic
xkcd.latest()

# Get random What If? article
WhatIf.random()
'''
# Get number of latest What If? article
WhatIf.latest()

