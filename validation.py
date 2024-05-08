import pathlib as path
import os
# argument checking is done at lower level because returning false here sends control
# back to the function that called it and will throw an error message that's more 
# useful to the user.

validPlayFlags = ["-multi", "-delay", "-mute", "-seq", "-rand"]
validRemoveFolderFlags = ["-empty", "-nonempty"]


### Helper functions

def _arg_splitter(args):
    """Split arguments.
    Helper function.
    Splits arguments on spaces and removes unnecessary empty items.
    """
    split = []
    input = args.split(" ")
    for item in input:
        if not item == '':
            split.append(item)
    return split

def is_valid_path(arg):
    """Find if a file exists.
    Helper function.
    Returns true if the argument is a file, false if it isn't.
    """
    if ".wav.wav" in arg:
        print("When accessing sounds do not append .wav.")
        return False
    testPath = path.Path(arg).resolve()
    if not os.path.exists(testPath):
        return False
    return True

def has_audio_files(arg):
    """Return if a folder has an audio file.
    Helper function.
    Returns false if the folder is empty or if it doesn't have any .wav files.
    Returns true if the folder has at least one .wav file.
    """
    directory = path.Path(os.getcwd()).as_posix()+"/"+arg

    if len(os.listdir(directory)) == 0:
        return False
    for file in os.listdir(directory):
        if file.endswith(".wav"):      
            return True  
        print(file)
    #return False

def is_valid_out(arg):
    """Validate -out flags.
    Helper function for effect functions.
    Returns false if the flag is not -out, or if the file name already
    exists.
    Returns true otherwise.
    """
    if not "-out=" in arg:
        print(f"Error: '{arg}' not recognized for this function. Please use '-out=<path_to_new_file>. \n")
        return False
    outName = arg.split("=")[1]
    if outName:
        if is_valid_path(f"{outName}.wav"):
            print("Error: Cannot save a file when a file with the same name exists. \n")
            return False
        if not is_valid_new_sound(arg):
            print("Error: Path to out file not recognized. \n")
            return False
    return True

def is_valid_directory(arg):
    """Find if a directory/folder exists.
    Helper function.
    Returns true if the argument is a directory, false if it isn't.
    """
    directory = path.Path(os.getcwd()).as_posix()+"/"+arg
    if not os.path.isdir(directory):
        return False
    return True

def is_valid_flag(arg, validFlags):
    """Check play command tags are valid.
    Submethod of validate_play and validate_remove_folder to compare inputted 
    tags to tags we accept.
    Returns false if the argument isn't within the list of valid flags.
    """
    for flag in validFlags:
        if flag in arg:
            return True
    return False

def is_valid_new_sound(arg):
    """Check that the path to a non-existant audio file is valid.
    Helper function.
    When making a new sound, part of the path is the folder in which the sound is to
    be saved. This needs to be a folder that already exists, so if the folder doesn't
    exist (yet), this function returns false.
    """
    # split at the / and makes sure the stuff before the end is a valid directory.
    outPath = arg.split("=")[-1]
    if not "/" in outPath:
        return True
    else:
        outDirectory = outPath.rsplit("/", 1)[-2]
        return is_valid_directory(outDirectory)



### Function validation.

def validate_play(args = None):
    """Validate the play command.
    Checks to see that the user passed arguments. It checks that the flags are valid
    and in the list of acceptable flags. It also checks that all of the audio files
    to play are valid audio files that can be found (and not directories).
    """
    input = _arg_splitter(args)

    if not args:
        return False
    for item in input:
        if "-" in item:
            if not is_valid_flag(item, validPlayFlags):
                print(f"Error: invalid flag '{item}' used.\n")
                return False
        else:
            if is_valid_directory(item) and not has_audio_files(item):
                print(f"Error: folder '{item}' doesn't contain any audio files. \n")
                return False
            if not is_valid_path(f"{item}.wav") and not is_valid_directory(item):
                print(f"Error: audio file '{item}' cannot be found.\n")
                return False
    return True
    
def validate_rename(args):
    """Validate the rename command.
    Checks to see that the user passed 2 arguments. It checks that the first argument
    is a valid, existing audio file and that the second argument is not a valid audio 
    file in order to avoid overlapping names.
    """
    input = _arg_splitter(args)

    if len(input) == 2:
        if not is_valid_path(input[0]):
            print(f"Error: Cannot recognize '{input[0]}', the sound file to rename.\n")
            return False
        if is_valid_path(input[1]):
            print(f"Error: Cannot rename a file when a file with the same name exists. \n")
            return False
        return True
    print("Error: Incorrect number of arguments passed. \n")
    return False
    
def validate_list_sounds(args):
    """Validate the list_sounds command.
    Checks to see that the user passed a single argument and that the argument
    is a valid directory.
    """
    input = _arg_splitter(args)
    if len(input) == 1:
        if is_valid_directory(input[0]):
            return True
        print(f"Error: '{input[0]}' not recognized as a valid directory.\n")
    return False

def validate_add_sound(args):
    """Validate the add_sound command.
    Checks to see that the user passed two arguments. It makes sure that the directory
    (the first argument) is valid and exists. It also makes sure that the second argument
    is a valid file and not a directory. The function also returns false if the file to be
    added already exists in the target directory.
    """
    input = _arg_splitter(args)
    if len(input) == 2:
        if not is_valid_directory(input[0]):
            print(f"Error: '{input[0]}' not recognized as a valid directory.\n")
            return False
        if not is_valid_path(input[1]) or is_valid_directory(input[1]):
            print(f"Error: Source file '{input[1]}' not recognized.\n")
            return False
        if os.path.exists(os.path.join(input[0], os.path.basename(input[1]))):
            print(f"Error: There already exists a file '{input[1]}' in folder '{input[0]}'. Please try again with another name.\n")
            return False
        return True
    return False

def validate_remove_sound(args):
    """Validate the remove_sound command.
    Checks to see that the user passed a single argument and that the file to remove
    exists.
    """
    input = _arg_splitter(args)
    if not args:
        return False
    if len(input) == 1:
        if not is_valid_path(input[0]):
            print(f"Error: Cannot recognize '{input[0]}', the sound file to remove.\n")
            return False
        return True
    print("Error: Incorrect number of arguments. \n")
    return False

def validate_merge(args):
    """Validate the merge command.
    Checks to see that the user passed arguments. If the user uses the -out
    flag, it checks that the out file doesn't already exist (and that there are
    no other flags).
    """
    input = _arg_splitter(args)
    if not args:
        return False
    
    for item in input:
        if "-" in item and len(input) > 1:
            if not is_valid_out(item):
                # if the item is a flag but isn't a valid -out, then we don't want it.
                return False
        elif not is_valid_path(f"{item}.wav"):
            print(f"Error: '{item}' is not a valid audio file. \n")
            return False
    return True

def validate_new_folder(args):
    """Validate the new_folder command.
    Checks that the input is a single argument and that it
    isn't already a directory.
    """
    input = _arg_splitter(args)
    if len(input) == 1:
        if is_valid_directory(input[0]):
            print(f"Error: Folder '{input[0]}' already exists. \n")
            return False
        return True
    return False

def validate_remove_folder(args):
    """Validate the remove_folder command.
    Checks that there's either 1 or 2 arguments. The folder has to exist
    and there can be only one. If there's a flag, there can be only one
    and it has to be in the list of valid flags.
    """
    input = _arg_splitter(args)

    if not args:
        return False
    
    # if there's one input, it must be an empty folder.
    if len(input) == 1:
        if not is_valid_directory(input[0]):
            print(f"Error: Folder '{input[0]}' doesn't exist. \n")
            return False
        elif len(os.listdir(input[0])) > 0:
            print(f"Error: {input[0]} isn't empty. Type 'remove_folder -nonempty {input[0]}' to remove.")
            return False
        return True

    # if there's two input, the first must be a flag and the second must be a folder.
    # if the '-empty' flag is used, then the folder to remove must be empty.
    elif len(input) == 2:
        if ("-" in input[0]) and not is_valid_flag(input[0], validRemoveFolderFlags):
            print(f"Error: Invalid flag '{input[0]}' used.\n")
            return False
        elif not is_valid_directory(input[1]):
            print(f"Error: Folder '{input[1]}' doesn't exist. \n")
            return False
        elif input[0] == "-empty" and (len(os.listdir(input[1])) > 0):
            print(f"Error: {input[1]} isn't empty. Type 'remove_folder -nonempty {input[1]}' to remove.")
            return False
        return True
    print("Error: Too many arguments passed. \n")
    return False

def validate_list_folders(args):
    """Validate the list_folders command.
    Checks that no arguments are passed, or that the only argument is a 
    valid directory.

    possible extension: only let user see folders that contain .wav files
    """
    input = _arg_splitter(args)
    if not args:
        return True

    if len(input) == 1 and is_valid_directory(input[0]):
        return True
    print("Error: list_folders takes a maximum of 1 argument. \n")
    return False

def validate_trim_sound(args):
    """Validate the trim_sound command.
    Checks that the user inputted either 3 or 4 arguments. The audio file to trim
    must be valid/exist. If the user includes an -out flag, then it must be valid. 
    The start and end times cannot be negative, nor can the end time come before 
    the start time.
    """
    input = _arg_splitter(args)
    if not args:
        return False
    if len(input) < 3 or len(input) > 4:
        print(f"Error: Incorrect number of arguments ({len(input)}) passed. \n")
        return False
    if not is_valid_path(f"{input[0]}.wav"):
        print(f"Error: '{input[0]}' is not a valid audio file. \n")
        return False
    if len(input) == 4:
        if "-" in input[3]:
            if not is_valid_out(input[3]):
                return False
        else:
            print(f"Error: unknown '{input[3]}' passed instead of an -out flag. \n")
            return False
    for item in input:
        if isinstance(item, float) and float(item) < 0:
            print("Error: invalid start and/or end times. \n")
            return False
    if float(input[1]) > float(input[2]):
        print("Error: the trim start time must come before the end time. \n")
        return False
    return True

def validate_reverse(args):
    """Validates the reverse command.
    Checks to see that the user passed the correct number of arguments 
    (either 1 or 2). If there's an -out flag, it checks if it's properly 
    formatted. It checks that the audio file to be reversed is valid.
    """
    input = _arg_splitter(args)

    if not args or len(input) > 2:
        print("Error: Incorrect number of arguments. \n")
        return False
    if len(input) == 2 and "-" in input[1]:
        if not is_valid_out(input[1]):
            return False
    if not is_valid_path(f"{input[0]}.wav"):
        print(f"Error: '{input[0]}' is not a valid audio file. \n")
        return False
    return True


def validate_find_length(args):
    """Validate the find_length command.
    Checks to see that the user only passed one argument and that the
    argument is a valid string.
    """
    input = _arg_splitter(args)
    if not args:
        return False

    if len(input) == 1:
        if not is_valid_path(f"{input[0]}.wav"):
            print(f"Error: '{input[0]}' is not a valid sound. \n")
            return False
        return True
    print("Error: Too many arguments passed. \n")
    return False

def validate_filter(args):
    """Validate the filter command. 
    Checks to see that the user passed the correct number of arguments 
    (either 2 or 3) and that the second argument is either 'high' or 'low'. 
    If there's an -out flag, it checks if it's properly formatted. It checks 
    that the audio file to be filtered is valid.
    """
    input = _arg_splitter(args)
    if not args or len(input)< 2 or len(input) > 3:
        print("Error: Incorrect number of arguments. \n")
        return False
    
    if not is_valid_path(f"{input[0]}.wav"):
        print(f"Error: '{input[0]}' is not a valid audio file. \n")
        return False
    
    if input[1] not in ["high", "low"]:
        print("Error: Please indicate a high or low filter using 'high' or 'low'. \n")
        return False
    
    if len(input) == 3 and "-" in input[2]:
        if not is_valid_out(input[2]):
            return False
    
    return True

def validate_add_tags(args):
    """Validate the add_tags command.
    Checks to see that the user passed the correct number of arguments 
    (at least 2). The first argument must be a valid audio file. The rest 
    of the arguments can be anything.
    """
    input = _arg_splitter(args)
    if not args or len(input) < 2:
        print("Error: Not enough arguments passed. \n")
        return False
    if not is_valid_path(f"{input[0]}.wav"):
        print(f"Error: '{input[0]}' is not a valid audio file. \n")
        return False
    return True

def validate_add_description(args):
    """Validate the add_description command.
    Checks to see that the user passed the correct number of arguments 
    (exactly 2). The first argument must be a valid audio file.
    The second argument must be a description string.
    """
    input = _arg_splitter(args)
    if not args or len(input) < 2:
        print("Error: Not enough arguments passed. \n")
        return False
    if not is_valid_path(f"{input[0]}.wav"):
        print(f"Error: '{input[0]}' is not a valid audio file. \n")
        return False
    return True

def validate_search_tag(args):
    """Validate the search_tag command.
    Checks to see that the user passed the correct number of arguments 
    (exactly 2). 
    """
    input = _arg_splitter(args)
    if not args or len(input) < 2:
        print("Error: Not enough arguments passed. \n")
        return False
    return True

def validate_search_description(args):
    """Validate the search_description command.
    Checks to see that the user passed the correct number of arguments 
    (exactly 2). 
    """
    input = _arg_splitter(args)
    if not args or len(input) < 2:
        print("Error: Not enough arguments passed. \n")
        return False
    return True
    
