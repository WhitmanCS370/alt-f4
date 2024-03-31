import sys
import simpleaudio
import os
import time

import helpmenu as hm
import inputparser as ip
import playsound as ps

argvlen = len(sys.argv)
sounds = []
extensions = ['.wav']   # can add more file types here as we add support for them, only impacts visible files.


def delay_sound(filenames, delay):
    """Play sounds sequentially, with a delay between each sound.

    Arguments:
    filenames -- a list of audio files to be played.
    delay -- a float value that determines the length of the delay (in seconds).     
    """
    for fn in filenames:
        wave_obj = simpleaudio.WaveObject.from_wave_file(fn)
        print(f'Playing {fn}')
        play_obj = wave_obj.play()
        time.sleep(delay)
    play_obj.wait_done()

def play_sound(filename):
    """Play a single sound in its entirity.

    Argument:
    filename -- the name of the audio file to play.
    """
    wave_obj = simpleaudio.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def multi_sound(filenames):
    """Play multiple sounds concurrently.

    Argument:
    filenames -- a list of audio files to play concurrently.
    """
    for fn in filenames:
        wave_obj = simpleaudio.WaveObject.from_wave_file(fn)
        play_obj = wave_obj.play()
    play_obj.wait_done()
    
# find_folder, called by --list_sounds.
    # for non-default directories, this takes the intended folder as an argument and returns
    #   the path to that folder.
def find_folder(folder):
    return(os.getcwd()+"/"+folder)

def func_usage():
    # should look through the help menu for the relevant item and print it.
    # called when the user isn't doing a call right.

    #sys.argv[1], check if the first thing contains this?
    for command, desc in hm.HELPMENU.items():
        if sys.argv[1] in str(command):
            print(f"{command}: {desc}")
    pass

def display_help():
    #if argvlen<=1 or sys.argv[1]=='--help' or sys.argv[1]=='-h':
    # the help menu, formatted exactly how it displays on the command line.
    print("usage:",sys.argv[0], "[command] [arg(s)]")

    for command, desc in hm.HELPMENU.items():
        print(f"{command:<18}: {desc}")

    sys.exit(0);

# def play_sound_func():
#     # also need to have a default/work without an internal flag... need to see if 
#     # sys.argv[2] is a valid sound if it isn't one of our accepted flags.
#     if sys.argv[2] == "-m" or sys.argv[2] == "--multi":
#         play_multisound_func(3)
        
#     elif sys.argv[2] == "-s" or sys.argv[2] == "--sequence":
#         if argvlen < 4:
#             print('No file provided...')

#         # tests (and delay calculations)
#         try:
#             delay = float(sys.argv[3])                 # if argument casts to float without issue, save as the delay. 
#         except:
#             delay = None                               # if there's an error, then it's probably a string (should be a sound).
            
#         # we have sound(s) to play, so the sound(s) is played (one after the other) and its name is printed when it does.
#         if argvlen >= 4 and delay == None:
#             for sound in sys.argv[3:]:                # loops through remaining sounds and plays them (works with 1 sound).
#                 print(f'Playing {sound}')
#                 play_sound(sound)
#         elif argvlen >= 5 and delay:                  # we need one more arg (because delay takes up a arg), but play sounds.
#             print(f"Adding {str(delay)}s of delay between sounds.")
#             delay_sound(sys.argv[4:], delay)          # functions more like -p, loop in the function rather than in call.

# def play_multisound_func(index):
#     """ Play multiple sounds at once.
#     Arguments:
#     the index the sounds start at (or a list of sounds?)
#     """
#     # tests
#     try:
#         float(sys.argv[index])              # if the first argument is a number...
#         sys.argv.remove(sys.argv[index])    # get rid of it as it will cause issues in the code.
#     except ValueError:
#         pass

#     # code to play the sounds
#     if sys.argv[index]:                                # if there is a sound to play... (sys.argv[2] not null)
#         for arg in sys.argv[index:]:                   # then append all of the sounds we have together...
#             sounds.append(arg)
#         print(f'Playing sounds')
#         multi_sound(sounds)                        # and play them by calling multi_sound with the appended sounds.

# def play_seqsound_func(index):
#     """ Play multiple sounds one after the other.
#     Arguments:
#     the index the sounds start at (or a list of sounds?)
#     """
#     if argvlen < index + 1:
#         print('No file provided...')

#     # tests (and delay calculations)
#     try:
#         delay = float(sys.argv[index])                 # if argument casts to float without issue, save as the delay. 
#     except:
#         delay = None                               # if there's an error, then it's probably a string (should be a sound).
            
#     # we have sound(s) to play, so the sound(s) is played (one after the other) and its name is printed when it does.
#     if argvlen >= index+1 and delay == None:
#         for sound in sys.argv[index:]:                # loops through remaining sounds and plays them (works with 1 sound).
#             print(f'Playing {sound}')
#             play_sound(sound)
#     elif argvlen >= index+2 and delay:                  # we need one more arg (because delay takes up a arg), but play sounds.
#         print(f"Adding {str(delay)}s of delay between sounds.")
#         delay_sound(sys.argv[index+1:], delay)          # functions more like -p, loop in the function rather than in call.

def rename_func():
    #if sys.argv[1] == '-r' or sys.argv[1] == '--rename':
    if argvlen < 3 or argvlen < 4:        # if not enough args are provided, we can't rename
        print('no file provided...')           
    else:
        os.rename(sys.argv[2], sys.argv[3])           # otherwise, change name of given file


def display_sounds():
    #if sys.argv[1] == '-ls' or sys.argv[1] == '--list_sounds':
    if argvlen>=3:                                      # if we're specifying which directory to open...
        category = find_folder(sys.argv[2])             # find the folder that the user specified...
        for file in os.listdir(category):
            if file.endswith(tuple(extensions)):        # make sure it's a file type we support
                print(file)                             # and print out everything (of acceptable file types) in that folder
    else:
        for file in os.listdir(os.getcwd()+"/sounds"):  # otherwise, we can just print content of default "sounds" folder
           print(file)


commands = {
    "--help": display_help,
    "-h": display_help,
    "--list_sounds": display_sounds,
    "-ls": display_sounds,
    "--play": ps.play_sound_func,
    "-p": ps.play_sound_func,
    "--rename": rename_func,
    "-r": rename_func
}

if __name__ == "__main__":
    if argvlen<=1:
        display_help()

    ip.parse(sys.argv)

    try:
        input = sys.argv[1]
        commands[input]()
    except (IndexError, KeyError):
        print("Invalid command. Use -h or --help for help.")
        sys.exit(1)



# transform flags: reverse, trim, filter, multi (requires multiple inputs)