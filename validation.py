def validate_play(args):
    """Validates the play 
    """
    # TODO: check if first thing is a sound or flag (maybe)
    if not args:
        return False
    return True
    
def validate_rename(args):
    # TODO: think if there's other things we need to validate
    input = args.split(" ")
    if len(input) == 2:
        return True
    return False
    
def validate_list_sounds(args):
    # TODO: think if there's other things we need to validate
    input = args.split(" ")
    if len(input)==1 and input[0]=="":
        return False
    return True

def validate_add_sound(args):
    # TODO: implement, move validation stuff in the function to here.
    return True

def validate_remove_sound(args):
    # TODO: implement
    return True