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


class CLI():

    def __init__(self, controller):
        self.controller = controller
        pass

    def delay_sound(self, filenames, delay):
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

    def play_sound(self, filename):
        """Play a single sound in its entirity.

        Argument:
        filename -- the name of the audio file to play.
        """
        wave_obj = simpleaudio.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()

    def multi_sound(self, filenames):
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
    def find_folder(self, folder):
        return(os.getcwd()+"/"+folder)

    def func_usage(self):
        # should look through the help menu for the relevant item and print it.
        # called when the user isn't doing a call right.

        #sys.argv[1], check if the first thing contains this?
        for command, desc in hm.HELPMENU.items():
            if sys.argv[1] in str(command):
                print(f"{command}: {desc}")
        pass

    def display_help(self):
        #if argvlen<=1 or sys.argv[1]=='--help' or sys.argv[1]=='-h':
        # the help menu, formatted exactly how it displays on the command line.
        print("usage:",sys.argv[0], "[command] [arg(s)]")

        for command, desc in hm.HELPMENU.items():
            print(f"{command:<18}: {desc}")

        sys.exit(0);

    def rename_func():
        #if sys.argv[1] == '-r' or sys.argv[1] == '--rename':
        if argvlen < 3 or argvlen < 4:        # if not enough args are provided, we can't rename
            print('no file provided...')           
        else:
            os.rename(sys.argv[2], sys.argv[3])           # otherwise, change name of given file


    def display_sounds():
        #if sys.argv[1] == '-ls' or sys.argv[1] == '--list_sounds':
        if argvlen>=3:                                      # if we're specifying which directory to open...
            category = CLI.find_folder(sys.argv[2])             # find the folder that the user specified...
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
        CLI.display_help()

    ip.parse(sys.argv)

    try:
        input = sys.argv[1]
        CLI.commands[input]()
    except (IndexError, KeyError):
        print("Invalid command. Use -h or --help for help.")
        sys.exit(1)



    # transform flags: reverse, trim, filter, multi (requires multiple inputs)