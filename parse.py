import validation

# TODO: make like play, where parse is a parent and there's subdivisions based on what
#       needs to be returned.

def parse(type, input):
    flags = []
    sounds = []
    other = []

    input = input.split(" ")
    for item in input:
        if "-" in item:
            flags.append(item.replace("-",""))
        elif validation.path_validator(f"{item}.wav"):
            sounds.append(item)
        else:
            other.append(item)

    if type == "play":
        print("parse play- flag, sounds, delay")
    elif type == "merge":
        print("parse merge- check for out")
    elif type == "reverse":
        print("parse reverse- check for out")
    elif type == "remove_folder":
        print("parse remove_folder- folder")
    elif type == "trim_sounds":
        print("parse trim_sounds-")

    return flags, sounds


def parse_flag(flags, toFind):
    """Find a specific flag within input.
    If the flag with additional information (either -delay or -out) is found,
    then the additional info is returned. Otherwise, it returns nothing.
    """
    for item in flags:
        if toFind in item:
            return item.split("=")[1]
    return
        
def parse_folder(args):
    """Find folder in input.
    From the elements in the input that weren't sounds or flags, search to find
    if there are any valid folders.
    """
    for item in args:
        if validation.directory_validator(item):
            return item


    # def parse_merge(self, args):
    #     input = args.split(" ")

    #     sounds = []
    #     out = None

    #     for item in input:
    #         if "-out" in item:
    #             outCommand = item.split("=")
    #             out = outCommand[1]
    #         elif not item =='':
    #             sounds.append(item)
    #     return sounds, out

    # def parse_reverse(self, args):
    #     input = args.split(" ")
    #     out = None

    #     if (len(input) == 2) and ("-out" in input[1]):
    #         outCommand = input[1].split("=")
    #         out = outCommand[1]
    #         sound = input[0]
    #         return sound, out
    #     else:
    #         sound = input[0]
    #         return sound, out