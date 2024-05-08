import cmd, os

import validation
from datetime import datetime
from playsound import AudioPlayer
from filemanager import FileManager
from metadatamanager import MetadataManager
from effectsmanager import EffectManager


class main(cmd.Cmd):

    commandDict = {"play":validation.validate_play,
                   "rename":validation.validate_rename,
                   "list_sounds":validation.validate_list_sounds,
                   "add_sound":validation.validate_add_sound,
                   "remove_sound":validation.validate_remove_sound,
                   "merge":validation.validate_merge,
                   "new_folder":validation.validate_new_folder,
                   "remove_folder":validation.validate_remove_folder,
                   "list_folders":validation.validate_list_folders,
                   "trim_sound":validation.validate_trim_sound,
                   "reverse":validation.validate_reverse,
                   "find_length":validation.validate_find_length,
                   "filter":validation.validate_filter,
                   "add_tags":validation.validate_add_tags,}

    def __init__(self):
        super().__init__()
        self.intro = "Command line interface for audio archive."
        self.prompt = "\ninput command: "
        self.player = AudioPlayer(self)
        self.files = FileManager(self)
        self.metadata = MetadataManager("metadata.db")
        self.effects = EffectManager(self)
        # init sound editing file.

    def validate(self, inputType, args):
        """Validate commands passed by the user.
        Using the 'validation' module, it checks if the type of command
        exists and if the passed arguments work with the command.

        Arguments:
        inputType-- the type of command the user is trying to run.
        args-- all other parts of the user's input.
        """
        if inputType in self.commandDict.keys():
            validator = self.commandDict[inputType](args)
            return validator
        else:
            print(f"{inputType} is not a recognized command! Type 'help' to view commands.")
            return False

    def parse(self, input):
        """Parse through play commands.
        There are different ways to play sounds, and input can be
        complicated. 

        Arguments:
        input-- the arguments the user passed in their command call.

        Returns:
        flags-- a list of flags that were paseed (what type of play to do)
        sounds-- a list of sounds to play
        delay-- how much delay between sounds (delay play exclusive)
        """
        flags = []
        sounds = []
        delay = None
        folder = None

        input = input.split(" ")
        for item in input:
            if "-" in item:
                if "-delay" in item:
                    delayCommand = item.split("=")
                    delay = delayCommand[1]
                else:
                    flags.append(item.replace("-",""))
            elif validation.is_valid_path(f"{item}.wav"):
                sounds.append(item)
            elif validation.directory_validator(item):
                folder = item

        return flags, sounds, delay, folder

    def do_play(self, args):
        """Play sound(s), either all at once or sequentially (with or without delay).
        Implementation handled in AudioPlayer.
        usage) play [-multi|-seq|-rand|-delay={delaytime}] <file_name(s)>
        """
    
        if(self.validate("play", args)):
            self.player.play(args)
        else:
            self.do_help("play")

    def do_rename(self, args):
        """Rename an audio file.
        Implementation handled in FileManager.
        usage) rename <original_file> <new_name>        
        """
        if(self.validate("rename", args)):
            self.files.rename(args)
        else:
            self.do_help("rename")

    def do_add_sound(self, args):
        """Add sound to audio archive.
        Implementation handled in FileManager.
        usage) add_sound <folder_to_add_to> <path_to_original_file>
        """
        if(self.validate("add_sound", args)):
            self.files.add_sound(args)
        else:
            self.do_help("add_sound")

    def do_remove_sound(self, args):
        """Remove sound from audio archive.
        Implementation handled in FileManager.
        usage) remove_sound <path_to_file>
        """
        if(self.validate("remove_sound", args)):
            self.files.remove_sound(args)
        else:
            self.do_help("remove_sound")

    def do_new_folder(self, args):
        """Make new folder.
        usage) new_folder <folder_name>
        """
        if(self.validate("new_folder", args)):
            self.files.new_folder(args)
        else:
            self.do_help("new_folder")

    def do_list_sounds(self, args):
        """List sounds in specified folder.
        Implementation handled in FileManager.
        usage) list_sounds <folder>
        """
        if(self.validate("list_sounds", args)):
            self.files.list_sounds(args) 
        else:
            self.do_help("list_sounds")

    def do_list_folders(self, args):
        """List folders in specified folder.
        usage) list_folders [folder_name]
        """
        if(self.validate("list_folders",args)):
            self.files.list_folders(args)
        else:
            self.do_help("list_folders")

    def do_remove_folder(self, args):
        """Remove specified folder
        usage) remove_folder [-empty|-nonempty] <folder_to_remove>
        """
        if(self.validate("remove_folder",args)):
            self.files.remove_folder(args)
        else:
            self.do_help("remove_folder")
                
    def do_merge(self, args):
        """Merge sounds together (sequentially) into a single longer audio.
        Implementation handled in EffectManager.
        usage) merge <file_name(s)> [-out=<path_to_new_file>]
        """
        if(self.validate("merge", args)):
            self.effects.merge(args)
        else:
            self.do_help("merge")
        return
    
    def do_trim_sound(self, args):
        """Change the size of a sound file.
        Implementation handled in EffectManager.
        usage: trim_sound <file_name> <start_time(sec)> <end_time(sec)> [-out=<path_to_new_file>]"""
        if(self.validate("trim_sound", args)):
            self.effects.trim_sound(args)
        else:
            self.do_help("trim_sound")
        return
    
    def do_reverse(self, args):
        """Reverse the playback direction of a sound.
        Implementation handled in EffectManager.
        usage: reverse <file_name> [-out=<path_to_new_file>]"""
        if(self.validate("reverse", args)):
            self.effects.reverse(args)
        else:
            self.do_help("reverse")
        return
    
    def do_find_length(self, args):
        """Finds the length of a sound in seconds. Helper function to trim_sound.
        Implementation handled in EffectManager.
        usage: find_length <file_name>
        """
        if(self.validate("find_length", args)):
            self.files.find_length(args)
        else:
            self.do_help("find_length")
        return

    def do_filter(self, args):
        """Puts a high or low filter on a sound.
        Implementation handled in EffectManager.
        usage: filter <file_name> <high or low> [-out=<path_to_new_file>]
        """
        if(self.validate("filter", args)):
            self.effects.filter(args)
        else:
            self.do_help("filter")
    
    def do_add_tags(self, args):
        """Add tags to a sound file.
        Implementation handled in MetadataManager.
        usage: add_tags <file_name> <tag1> <tag2> ... <tagN>
        """
        if(self.validate("add_tags", args)):
            self.metadata.add_tags(args)
        else:
            self.do_help("add_tags")

    def do_exit(self, args):
        """ End the command line interface loop/program.
        usage) exit
        """
        return True
    
if __name__ == "__main__":
    CLI_interface = main()
    CLI_interface.cmdloop()