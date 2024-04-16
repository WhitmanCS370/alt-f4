import pathlib as path
import os
# argument checking is done at lower level because returning false here sends control
# back to the function that called it and will throw an error message that's more 
# useful to the user.

validFlags = ["-multi", "-delay", "-mute", "-seq", "-rand"]

def arg_splitter(args):
    """Split arguments.
    Splits arguments on spaces and removes unnecessary additions.
    """
    split = []
    input = args.split(" ")
    for item in input:
        if not item == '':
            split.append(item)
    return split

def path_validator(arg):
    """Find if a file exists.
    Returns true if it exists, false if it doesn't.
    """
    testPath = path.Path(arg).resolve()
    if not os.path.exists(testPath):
        return False
    return True

def directory_validator(arg):
    """Find if a directory/folder exists.
    Returns true if it exists, false if it doesn't.
    """
    directory = path.Path(os.getcwd()).as_posix()+"/"+arg
    if not os.path.isdir(directory):
        return False
    return True

def flag_check(arg):
    """Check play command tags are valid.
    Submethod of validate_play to compare inputted tags to tags we accept.
    """
    for flag in validFlags:
        if flag in arg:
            return True
    return False

def validate_play(args = None):
    """Validates the play command.
    Checks to see that the user passed arguments.
    """
    input = arg_splitter(args)

    if not args:
        return False
    for item in input:
        if "-" in item:
            if not flag_check(item):
                print(f"Error: invalid flag '{item}' used.\n")
                return False
        else:
            if not path_validator(f"{item}.wav") and not directory_validator(item):
                print(f"Error: audio file '{item}' cannot be found.\n")
                return False
    return True
    
def validate_rename(args):
    """Validates the rename command.
    Checks to see that the user passed arguments.
    """
    input = arg_splitter(args)

    if len(input) == 2:
        if not path_validator(input[0]):
            print(f"Error: Cannot recognize '{input[0]}', the sound file to rename.\n")
            return False
        if path_validator(input[1]):
            print(f"Error: Cannot rename a file when a file with the same name exists. \n")
            return False
        return True
    print("Error: Incorrect number of arguments passed. \n")
    return False
    
def validate_list_sounds(args):
    """Validates the list_sounds command.
    Checks to see that the user passed arguments.
    """
    input = arg_splitter(args)
    if len(input) == 1:
        if directory_validator(input[0]):
            return True
        print(f"Error: '{input[0]}' not recognized as a valid directory.")
    return False

def validate_add_sound(args):
    """Validates the add_sound command.
    Checks to see that the user passed arguments.
    """
    # TODO: implement, move validation stuff in the function to here.
    input = arg_splitter(args)
    if len(input) == 2:
        if not directory_validator(input[0]):
            print(f"Error: '{input[0]}' not recognized as a valid directory.")
            return False
        if not path_validator(input[1]) or directory_validator(input[1]):
            print(f"Error: Source file '{input[1]}' not recognized.")
            return False
        if os.path.exists(os.path.join(input[0], os.path.basename(input[1]))):
            print(f"Error: There already exists a file '{input[1]}' in folder '{input[0]}'. Please try again with another name.")
            return False
        return True
    return False

def validate_remove_sound(args):
    """Validates the remove_sound command.
    Checks to see that the user passed arguments.
    """
    # TODO: implement
    input = arg_splitter(args)
    if len(input) == 1:
        if not path_validator(input[0]):
            print(f"Error: Cannot recognize '{input[0]}', the sound file to remove.\n")
            return False
        return True
    print("Error: Incorrect number of arguments. \n")
    return False

def validate_merge(args):
    """Validates the merge command.
    Checks to see that the user passed arguments.
    """
    # TODO: implement
    input = arg_splitter(args)
    if not args:
        return False
    
    for item in input:
        if "-" in item and len(input) > 1:
            if not "-out" in item:
                return False
            outName = item.split("=")[1]
            if outName:
                if path_validator(f"{outName}.wav"):
                    print("Error: Cannot save a file when a file with the same name exists. \n")
                    return False
    return True