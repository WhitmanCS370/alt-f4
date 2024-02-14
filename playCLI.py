import sys
import simpleaudio
import os

argvlen = len(sys.argv)
sounds = []

def play_sound(filename):
    wave_obj = simpleaudio.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def multi_sound(filenames):
    for fn in filenames:
        wave_obj = simpleaudio.WaveObject.from_wave_file(fn)
        play_obj = wave_obj.play()
    play_obj.wait_done()

def play_sound_sequence():
    for sound in sys.argv[2:]:
        print(f'Playing {sound}')
        file = sound
        play_sound(file)

def find_folder(folder):
    return(os.getcwd()+"/"+folder)


if argvlen<=1 or sys.argv[1]=='--help' or sys.argv[1]=='-h':

    # This prints out a sample of how you might use this command
    print("usage:",sys.argv[0], '[command] [arg(s)]')
    print('--help, -h        : lists help menu, what each function is and how to use it.')
    print('--play, -p        : plays sound(s) that are passed as argument(s) in form \'directory/filename.wav\'.')
    print('                  : when multiple sounds are passed as arguments, the sounds play all at once.')
    print('--sequence, -s    : plays provided sounds sequentially')
    print('                  : sounds are passed as argument(s) in form \'directory/filename.wav\'.')
    print('--rename, -r      : changes name of file (specified by first argument) to name specified in second argument.')
    print('--list_sounds, -ls: lists all of the sounds/files in the default sounds directory')
    print('                  : to list from non-default directories, the directory name should be passed as argument.')

    sys.exit(0);

if sys.argv[1] == '-p' or sys.argv[1] == '--play':
    if sys.argv[2]:
        for arg in sys.argv[2:]:
            sounds.append(arg)
        print(f'Playing sounds')
        multi_sound(sounds)


if sys.argv[1] == '-s' or sys.argv[1] == '--sequence':
    # if we don't have at least the function flag (-s or --sequence) and a sound, we can't play anything.
    if len(sys.argv) < 3:
        print('No file provided...')
    # we have sound(s) to play (sounds are sys.argv[2] and greater), so the sound is played and its name is printed when it does.
    elif len(sys.argv) >= 3:
        # loops through remaining sounds and plays them.
        for sound in sys.argv[2:]:
            print(f'Playing {sound}')
            play_sound(sound)
     

if sys.argv[1] == '-r' or sys.argv[1] == '--rename':
    if sys.argv[2]:
        os.rename(sys.argv[2], sys.argv[3])
    else:
        print('no file provided...')


if sys.argv[1] == '-ls' or sys.argv[1] == '--list_sounds':
    if argvlen>=3:
        category = find_folder(sys.argv[2])
        for file in os.listdir(category):
           print(file)
    else:
        for file in os.listdir(os.getcwd()+"/sounds"):
           print(file)
           