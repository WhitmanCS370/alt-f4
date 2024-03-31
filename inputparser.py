import sys

def parse(arglist):
    """Make a list of tuples for each command"""
    # userin = []
    flags = []
    other = []
    for item in arglist:
        if "-" in item:
            flags.append(item)
        else:
            other.append(item)
    
    while i < len(arglist):
        currentitem = arglist[i]
        if "-" in currentitem:
            flags.append((currentitem,i))   # add item and where it appears
        else:
            other.append((currentitem,i))   # add item and where it appears
        print(arglist[i])
        i = i + 1
    
    print("flags: ", end=''),
    
    for x in range(len(flags)):
        print(str(x) + " " + flags[x][0] + ", " + flags[x][1] + " ", end='')
    print(" ")

