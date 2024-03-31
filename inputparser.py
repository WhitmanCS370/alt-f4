import sys

def parse(arglist):
    """Make a list of tuples for each command"""
    transforms = []
    plays = []
    output = []
    flags = []
    other = []
    for item in arglist:
        print(item)
        if "--" in item:
            print(1)
            flags.append(item)
        if "--transform" in item:
            print(2)
            transforms.append(item)
        if "--play" in item:
            print(3)
            plays.append(item)
        if "--output" in item:
            print(4)
            output.append(item)
        else:
            print(5)
            other.append(item)
    
    print("flags: ", end=''),
    
    for x in range(len(transforms)):
        print(str(x) + " " + str(transforms[x]) + ", ", end='')
    print(" ")

