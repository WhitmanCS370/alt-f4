import cmd
import simpleaudio
import time
import os
import validation
import pathlib as path
import shutil

from playsound import AudioPlayer
from validation import Validator
from filemanager import FileManager

class main(cmd.Cmd):

    commandDict = {"play":Validator.validate_play,
                   "rename":Validator.validate_rename,
                   "list_sounds":Validator.validate_list_sounds,
                   "add_sound":Validator.validate_add_sound,
                   "remove_sound":Validator.validate_remove_sound,
                   "delay":Validator.validate_delay}

    def __init__(self):
        super().__init__()
        self.intro = "Command line interface for audio archive."
        self.prompt = "input command: "
        self.player = AudioPlayer(self)
        self.validator = Validator(self)
        self.files = FileManager(self)
        # init sound editing file.

    def validate(self, inputType, args):
        ret = True
        if inputType in self.commandDict.keys():
            ret = self.commandDict[inputType](args)
            return ret
        else:
            print("That's not a recognized command! Type 'help' to view commands.")
            return False

    def parse_play(self, input):
        flags = []
        sounds = []
        delay = None

        for item in input:
            if "--" in item:
                if "--delay" in item:
                    delayCommand = item.split("=")
                    delay = delayCommand[1]
                else:
                    flags.append(item.replace("--",""))
            elif not item == '':
                sounds.append(item)

        return flags, sounds, delay

        for i, sound in enumerate(sounds):
            if i > 0:                 # add delay as long as it's not the last sound.
                time.sleep(float(delay))
            wave_obj = simpleaudio.WaveObject.from_wave_file(f"{sound}.wav")
            print(f'Playing {sound}')
            play_obj = wave_obj.play()
        play_obj.wait_done()

    def do_play(self, args):
        """Play sound(s), either all at once or sequentially (with or without delay).
        usage) play [multi|seq|delay={delaytime}] <file_name(s)>
        """
        # TODO: add error catching for if --delay=(something other than float)
        #       should actually add to some validation.
    
        if(self.validate("play", args)):
            self.player.play(args)
        else:
            self.do_help("play")

    def do_rename(self, args):
        """Rename an audio file.
        usage) rename <original_file> <new_name>        
        """
        if(self.validate("rename", args)):
            self.files.rename(args)
        else:
            self.do_help("rename")

    def do_add_sound(self, args):
        """Add sound to audio archive.
        usage) add_sound <folder_to_add_to> <path_to_original_file>
        """
        if(self.validate("add_sound", args)):
            self.files.add_sound(args)
        else:
            self.do_help("add_sound")

    def do_remove_sound(self, args):
        """Remove sound from audio archive.
        usage) remove_sound <path_to_file>
        """
        # TODO: implement validate_remove_sound in validation.py and make sure it works as intended
        if(self.validate("remove_sound", args)):
            self.files.remove_sound(args)
        else:
            self.do_help("remove_sound")

    def do_list_sounds(self, args = "sounds"):
        """List sounds in specified folder.
        usage) list_sounds <folder>
        """

        if(self.validate("list_sounds", args)):
            self.files.list_sounds(args) 
        else:
            self.do_help("list_sounds")
                

    def do_exit(self, args):
        """ End the command line interface loop/program.
        usage) exit
        """
        print("goodbye")
        return True

if __name__ == "__main__":
    CLI_interface = main()
    CLI_interface.cmdloop()


    # if (self.validate_single_arg(args)):
        #     self.audio.play(args)
        # else:
        #     self.provide_arg_msg()