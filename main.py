import cmd

from playsound import AudioPlayer
import validation
from filemanager import FileManager
from metadatamanager import MetadataManager

class main(cmd.Cmd):

    commandDict = {"play":validation.validate_play,
                   "rename":validation.validate_rename,
                   "list_sounds":validation.validate_list_sounds,
                   "add_sound":validation.validate_add_sound,
                   "remove_sound":validation.validate_remove_sound,
                   "delay":validation.validate_delay}

    def __init__(self):
        super().__init__()
        self.intro = "Command line interface for audio archive."
        self.prompt = "\ninput command: "
        self.player = AudioPlayer(self)
        self.files = FileManager(self)
        self.metadata = MetadataManager("metadata.db")
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
            print("That's not a recognized command! Type 'help' to view commands.")
            return False

    def parse_play(self, input):
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

    def do_play(self, args):
        """Play sound(s), either all at once or sequentially (with or without delay).
        Implementation handled in AudioPlayer.
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
        # TODO: implement validate_remove_sound in validation.py and make sure it works as intended
        if(self.validate("remove_sound", args)):
            self.files.remove_sound(args)
        else:
            self.do_help("remove_sound")

    def do_list_sounds(self, args = "sounds"):
        """List sounds in specified folder.
        Implementation handled in FileManager.
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