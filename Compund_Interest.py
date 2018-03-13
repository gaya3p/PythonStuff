import string
import random

string1 = "ABCDEF"
string2 = "FABCDE"

letters = list(string1)
extra = list("MNOP")
alphabet = letters  # + extra

counts = {"ONE": 0, "TWO": 0}


def measure():

    my_string = "0" * len(string1)
    over = None

    while over is None:
        my_string = my_string[1:] + random.choice(alphabet)
        if my_string == string1:
            over = "ONE"
        elif my_string == string2:
            over = "TWO"
    return over


for round in range(200000):
    counts[measure()] += 1

print(counts)
