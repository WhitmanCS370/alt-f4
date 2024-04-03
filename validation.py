def validate_play(self, args):
    # TODO: check if first thing is a sound or flag (maybe)
    input = args.split(" ")
    if len(input) == 1 and input[0]=="":
        return False
    print(len(input))
    return True
    
def validate_rename(self, args):
    # TODO: think if there's other things we need to validate
    input = args.split(" ")
    if len(input) == 2:
        return True
    return False
    
def validate_list_sounds(self, args):
    # TODO: think if there's other things we need to validate
    input = args.split(" ")
    if len(input) > 1:
        return False
    return True