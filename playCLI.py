import sys
import simpleaudio
import os
import time

argvlen = len(sys.argv)
sounds = []
extensions = ['.wav']   # can add more file types here as we add support for them, only impacts visible files.


# delay_sound, called by --sequence.
    # this code is used when --sequence is called with the first argument being an int
    # the first argument is interpreted as the delay.
    # when looping through the sounds to play them sequentially, delay is added using
    #   time.sleep().
def delay_sound(filenames, delay):
    for fn in filenames:
        wave_obj = simpleaudio.WaveObject.from_wave_file(fn)
        print(f'Playing {fn}')
        play_obj = wave_obj.play()
        time.sleep(delay)
    play_obj.wait_done()

# play_sound, called by --sequence.
    # because we want to play sounds one after the other, we wait for the sound to finish.
    # it's called repeatedly in --sequence to cover each sound in the list of arguments.
def play_sound(filename):
    wave_obj = simpleaudio.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()

# multi_sound, called by --play.
    # adds together all of the .wav sound files and starts them all before waiting for them
    #   all to end.
def multi_sound(filenames):
    for fn in filenames:
        wave_obj = simpleaudio.WaveObject.from_wave_file(fn)
        play_obj = wave_obj.play()
    play_obj.wait_done()
    
# find_folder, called by --list_sounds.
    # for non-default directories, this takes the intended folder as an argument and returns
    #   the path to that folder.
def find_folder(folder):
    return(os.getcwd()+"/"+folder)


if argvlen<=1 or sys.argv[1]=='--help' or sys.argv[1]=='-h':
    # the help menu, formatted exactly how it displays on the command line.
    print("usage:",sys.argv[0], '[command] [arg(s)]')
    print('commands:           description + usage:')
    print('--help, -h        : lists help menu, what each function is and how to use it.')
    print('--play, -p        : plays sound(s) that are passed as argument(s) in form \'directory/filename.wav\'.')
    print('                  : when multiple sounds are passed as arguments, the sounds play all at once.')
    print('--sequence, -s    : plays provided sounds sequentially')
    print('                  : sounds are passed as argument(s) in form \'directory/filename.wav\'.')
    print('                  : to play sounds with a set amount of delay between starts, pass a number as the first argument.')
    print('--rename, -r      : changes name of file (specified by first argument) to name specified in second argument.')
    print('--list_sounds, -ls: lists all of the sounds/files in the default sounds directory')
    print('                  : to list from non-default directories, the directory name should be passed as argument.')

    sys.exit(0);

if sys.argv[1] == '-p' or sys.argv[1] == '--play':
    # tests
    try:
        float(sys.argv[2])              # if the first argument is a number...
        sys.argv.remove(sys.argv[2])    # get rid of it as it will cause issues in the code.
        print("!!! When using -p or --play to play, please don't use any numbers. !!!")
    except ValueError:
        pass

    # code to play the sounds
    if sys.argv[2]:                                # if there is a sound to play... (sys.argv[2] not null)
        for arg in sys.argv[2:]:                   # then append all of the sounds we have together...
            sounds.append(arg)
        print(f'Playing sounds')
        multi_sound(sounds)                        # and play them by calling multi_sound with the appended sounds.


if sys.argv[1] == '-s' or sys.argv[1] == '--sequence':
    # if we don't have at least the function flag (-s or --sequence) and a sound, we can't play anything.
    if argvlen < 3:
        print('No file provided...')

    # tests (and delay calculations)
    try:
        delay = float(sys.argv[2])                 # if argument casts to float without issue, save as the delay. 
    except ValueError:
        delay = None                               # if there's an error, then it's probably a string (should be a sound).
        
    # we have sound(s) to play, so the sound(s) is played (one after the other) and its name is printed when it does.
    if argvlen >= 3 and delay == None:
        for sound in sys.argv[2:]:                # loops through remaining sounds and plays them (works with 1 sound).
            print(f'Playing {sound}')
            play_sound(sound)
    elif argvlen >= 4 and delay:                  # we need one more arg (because delay takes up a arg), but play sounds.
        print(f"Adding {str(delay)}s of delay between sounds.")
        delay_sound(sys.argv[3:], delay)          # functions more like -p, loop in the function rather than in call.
     

if sys.argv[1] == '-r' or sys.argv[1] == '--rename':
    if argvlen < 3 or argvlen < 4:        # if not enough args are provided, we can't rename
        print('no file provided...')           
    else:
        os.rename(sys.argv[2], sys.argv[3])           # otherwise, change name of given file to val of other arg.


if sys.argv[1] == '-ls' or sys.argv[1] == '--list_sounds':
    if argvlen>=3:                                      # if we're specifying which directory to open...
        category = find_folder(sys.argv[2])             # find the folder that the user specified...
        for file in os.listdir(category):
            if file.endswith(tuple(extensions)):        # make sure it's a file type we support
                print(file)                             # and print out everything (of acceptable file types) in that folder
    else:
        for file in os.listdir(os.getcwd()+"/sounds"):  # otherwise, we can just print content of default "sounds" folder
           print(file)
