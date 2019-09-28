x = {
    'a':'x',
    'b':'y',
    'c':'z',     
}

xbar = {}

for key, val in x.items():
    xbar[val] = key

print(xbar)
