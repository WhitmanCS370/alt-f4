import sys

def parse(arglist):
    """Make a list for each command"""
    transforms = []
    plays = []
    output = []
    flags = []
    other = []
    for item in arglist[1:]:
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

    comSplit("play", plays)
    
def comSplit(commandType, commands):
    """Convert input commands into usable ones (tuple)."""
    # format = --commandType=variable or --commandType=var1_var2_var3...
    parsedcommands = []

    for item in commands:
        comdetails = item.split("=")[1]
        parsedcommands.append(comParse(comdetails))

    print("parsed commands:", end=" ")
    print(parsedcommands)

def comParse(comstring):
    """Convert string command into method name and variables"""
    comlist = comstring.split("_")
    returnlist = []

    for item in comlist:
        returnlist.append(item)

    return returnlist 