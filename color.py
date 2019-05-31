from time import strftime, sleep

print(strftime("\nTime zone: %Z (%z)\n"))
showTimeZone = input("Show time zone each refresh? (Y/N)\n")
if showTimeZone.upper() == "Y":
    string = "%x      %X       %Z (%z)"
else:
    string = "         %x      %X"

showLineBreaks = input("Only show one line at a time? Kinda like screensaver\
                       (Don't use this with high refresh rates!) (Y/N)\n")
if showLineBreaks.upper() == "Y":
    showLineBreaks=True
    br = 20
else:
    showLineBreaks=False
    br = 0

col = input("Text color (input black, red, yellow, green, cyan, blue, magenta or white): ").lower()
coldict = {"black":0,"red":1,"green":2,"yellow":3,"blue":4,"magenta":5,"cyan":6,"white":7}

if col in coldict:
    col = coldict[col]
else:
    col = 7
    
ansiesccol = "\33[3"+str(col)+"m"

x = float(input("Refresh time (secs): "))

print("\33[?25l")
print(ansiesccol)

while True:
    if showLineBreaks:
        print("\33[2J")
   
    print(strftime(string)+"\n"*br)
    sleep(x)
