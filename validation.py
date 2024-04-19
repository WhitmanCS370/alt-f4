import pathlib as path
import os
# argument checking is done at lower level because returning false here sends control
# back to the function that called it and will throw an error message that's more 
# useful to the user.

validPlayFlags = ["-multi", "-delay", "-mute", "-seq", "-rand"]
validRemoveFolderFlags = ["-empty", "-nonempty"]

def arg_splitter(args):
    """Split arguments.
    Splits arguments on spaces and removes unnecessary empty items.
    """
    split = []
    input = args.split(" ")
    for item in input:
        if not item == '':
            split.append(item)
    return split

def path_validator(arg):
    """Find if a file exists.
    Returns true if the argument is a file, false if it isn't.
    """
    testPath = path.Path(arg).resolve()
    if not os.path.exists(testPath):
        return False
    return True

def directory_validator(arg):
    """Find if a directory/folder exists.
    Returns true if the argument is a directory, false if it isn't.
    """
    directory = path.Path(os.getcwd()).as_posix()+"/"+arg
    if not os.path.isdir(directory):
        return False
    return True

def flag_check(arg, validFlags):
    """Check play command tags are valid.
    Submethod of validate_play and validate_remove_folder to compare inputted 
    tags to tags we accept.
    Returns false if the argument isn't within the list of valid flags.
    """
    for flag in validFlags:
        if flag in arg:
            return True
    return False

def validate_play(args = None):
    """Validates the play command.
    Checks to see that the user passed arguments. It checks that the flags are valid
    and in the list of acceptable flags. It also checks that all of the audio files
    to play are valid audio files that can be found (and not directories).
    """
    input = arg_splitter(args)

    if not args:
        return False
    for item in input:
        if "-" in item:
            if not flag_check(item, validPlayFlags):
                print(f"Error: invalid flag '{item}' used.\n")
                return False
        else:
            if not path_validator(f"{item}.wav") and not directory_validator(item):
                print(f"Error: audio file '{item}' cannot be found.\n")
                return False
    return True
    
def validate_rename(args):
    """Validates the rename command.
    Checks to see that the user passed 2 arguments. It checks that the first argument
    is a valid, existing audio file and that the second argument is not a valid audio 
    file in order to avoid overlapping names.
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
    Checks to see that the user passed a single argument and that the argument
    is a valid directory.
    """
    input = arg_splitter(args)
    if len(input) == 1:
        if directory_validator(input[0]):
            return True
        print(f"Error: '{input[0]}' not recognized as a valid directory.\n")
    return False

def validate_add_sound(args):
    """Validates the add_sound command.
    Checks to see that the user passed two arguments. It makes sure that the directory
    (the first argument) is valid and exists. It also makes sure that the second argument
    is a valid file and not a directory. The function also returns false if the file to be
    added already exists in the target directory.
    """
    # TODO: implement, move validation stuff in the function to here.
    input = arg_splitter(args)
    if len(input) == 2:
        if not directory_validator(input[0]):
            print(f"Error: '{input[0]}' not recognized as a valid directory.\n")
            return False
        if not path_validator(input[1]) or directory_validator(input[1]):
            print(f"Error: Source file '{input[1]}' not recognized.\n")
            return False
        if os.path.exists(os.path.join(input[0], os.path.basename(input[1]))):
            print(f"Error: There already exists a file '{input[1]}' in folder '{input[0]}'. Please try again with another name.\n")
            return False
        return True
    return False

def validate_remove_sound(args):
    """Validates the remove_sound command.
    Checks to see that the user passed a single argument and that the file to remove
    exists.
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
    Checks to see that the user passed arguments. If the user uses the -out
    flag, it checks that the out file doesn't already exist (and that there are
    no other flags).
    """
    # TODO: check that sounds are valid
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

def validate_new_folder(args):
    """Validates the new_folder command.
    Checks that the input is a single argument and that it
    isn't already a directory.
    """
    input = arg_splitter(args)
    if len(input) == 1:
        if directory_validator(input[0]):
            print(f"Error: Folder '{input[0]}' already exists. \n")
            return False
        return True
    return False

def validate_remove_folder(args):
    """Validates the remove_folder command.
    Checks that there's either 1 or 2 arguments. The folder has to exist
    and there can be only one. If there's a flag, there can be only one
    and it has to be in the list of valid flags.
    """
    input = arg_splitter(args)
    flag = False
    folder = False 

    if not args:
        return False
    
    for item in input:
        if "-" in item and len(input) == 2:
            if not flag_check(item, validRemoveFolderFlags):
                print(f"Error: Invalid flag '{item}' used.\n")
                return False
            if flag:
                print("Error: remove_folder only works with one flag at a time. \n")
                return False
            flag = True
        elif len(input) <= 2:
            if folder:
                print("Error: remove_folder only works with one folder at a time. \n")
                return False
            if not directory_validator(item):
                print(f"Error: Folder '{item}' doesn't exist. \n")
                return False
            else:
                folder = True
        else:
            print("Error: Incorrect number of arguments passed. \n")
            return False
    return True

def validate_list_folders(args):
    """Validates the list_folders command.
    """
    # TODO: make this validation better, must be other cases to return false.
    input = arg_splitter(args)
    if len(input) > 1:
        return False
    return True

def validate_trim_sound(args):
    """Validates the trim_sound command.
    """
    input = arg_splitter(args)
    if not args:
        return False
    if len(input) > 4 or len(input) < 2:
        print("Please enter a sound, a start time (in seconds), an end time (in seconds), and optionally a name to save new file")
        return False
    for item in input:
        if item < 0:
            print("Please enter positive start and end times.")
            return False
    if input[1] < input[2]:
        print("Please enter a start time less than the end time.")
        return False
    return True

def validate_reverse(args):
    """Validates the reverse command.
    """
    input = arg_splitter(args)
    if not args:
        return False
    if len(input) > 2:
        print("Please enter a sound and optionally a new sound file name")
        return False
    return True