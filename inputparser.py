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
    
    print("flags: ", end=''),
    
    for x in range(len(flags)):
        print(str(x) + " " + flags[x] + " ", end='')
    print(" ")