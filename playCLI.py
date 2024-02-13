import sys
import simpleaudio
import os

argvlen = len(sys.argv)

def play_sound(filename):
    wave_obj = simpleaudio.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()

if sys.argv[1] == '-p' or sys.argv[1] == '--play':
    if sys.argv[2]:
        print(f'Playing {sys.argv[2]}')
        file = sys.argv[2]
        play_sound(file)
    else:
        print('no file provided...')

if sys.argv[1] == '-r' or sys.argv[1] == '--rename':
    if sys.argv[2]:
        os.rename(sys.argv[2], sys.argv[3])
    else:
        print('no file provided...')


if argvlen<=1 or sys.argv[1]=='--help' or sys.argv[1]=='-h':

    # This prints out a sample of how you might use this command
    print("usage:",sys.argv[0], '[command] [arg(s)]')
    print('--help, -h  : lists help menu, what each function is and how to use it.')
    print('--play, -p  : plays sound(s) that are passed as argument(s).')
    print('--rename, -r: changes name of file (specified by first argument) to name specified in second argument.')

    sys.exit(0);

def find_folder(folder):
    return(os.getcwd()+"/"+folder)

if sys.argv[1] == '-ls' or sys.argv[1] == '--list_sounds':
    if argvlen>=3:
        category = find_folder(sys.argv[2])
        for file in os.listdir(category):
           print(file)
    else:
        for file in os.listdir(os.getcwd()+"/sounds"):
           print(file)
        

