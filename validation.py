# argument checking is done at lower level because returning false here sends control
# back to the function that called it and will throw an error message that's more 
# useful to the user.

def validate_play(args = None):
    """Validates the play command.
    Checks to see that the user passed arguments.
    """
    # TODO: check if first thing is a sound or flag (maybe)
    if not args:
        return False
    return True
    
def validate_rename(args):
    """Validates the rename command.
    Checks to see that the user passed arguments.
    """
    # TODO: think if there's other things we need to validate
    input = args.split(" ")
    if len(input) == 2:
        return True
    return False
    
def validate_list_sounds(args):
    """Validates the list_sounds command.
    Checks to see that the user passed arguments.
    """
    # TODO: think if there's other things we need to validate
    if not args:
        return False
    return True

def validate_add_sound(args):
    """Validates the add_sound command.
    Checks to see that the user passed arguments.
    """
    # TODO: implement, move validation stuff in the function to here.
    if not args:
        return False
    return True

def validate_remove_sound(args=None):
    """Validates the remove_sound command.
    Checks to see that the user passed arguments.
    """
    # TODO: implement
    if not args:
        return False
    return True

def validate_delay(args):
    """Validates the delay subcommand of play command.
    Checks to see that the user passed arguments.
    """
    # TODO: implement
    if not args:
        return False
    return True