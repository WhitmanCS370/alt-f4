import cmd
import simpleaudio
import time
import os
import validation
import pathlib as path

class main(cmd.Cmd):

    commandDict = {"play":validation.validate_play, "rename":validation.validate_rename, "list_sounds":validation.validate_list_sounds}

    def __init__(self):
        super().__init__()
        self.intro = "Command line interface for audio archive."
        self.prompt = "input command: "
        # init audio editor
        # init file manager (for file editing)
        # init play module
        # init out module

    def validate(self, inputType, args):
        ret = True
        if inputType in self.commandDict.keys():
            ret = self.commandDict[inputType](args)
            return ret
        else:
            return False
        
    # def validate_play(self, args):
    #     # TODO: check if first thing is a sound or flag (maybe)
    #     input = args.split(" ")
    #     if len(input) == 1 and input[0]=="":
    #         return False
    #     print(len(input))
    #     return True
    
    # def validate_rename(self, args):
    #     # TODO: think if there's other things we need to validate
    #     input = args.split(" ")
    #     if len(input) == 2:
    #         return True
    #     return False
    
    # def validate_list_sounds(self, args):
    #     # TODO: think if there's other things we need to validate
    #     input = args.split(" ")
    #     if len(input) > 1:
    #         return False
    #     return True

    # def auto_help(self, command):
    #     print("invalid argument...")
    #     print(f"type 'help {command}', or'help' to see all commands.")

    def _parse_play(self, input):
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
            else:
                sounds.append(item)

        return flags, sounds, delay

    def _multi_play(self, sounds):
        for sound in sounds:
            wave_obj = simpleaudio.WaveObject.from_wave_file(f"{sound}.wav")
            play_obj = wave_obj.play()
        play_obj.wait_done()
        return
    
    def _seq_play(self, sounds):
        for sound in sounds:
            wave_obj = simpleaudio.WaveObject.from_wave_file(f"{sound}.wav")
            play_obj = wave_obj.play()
            play_obj.wait_done()
        return
    
    def _delay_play(self, sounds, delay):
        for sound in sounds:
            wave_obj = simpleaudio.WaveObject.from_wave_file(f"{sound}.wav")
            print(f'Playing {sound}')
            play_obj = wave_obj.play()

            if not sound == sounds[-1]:                 # add delay as long as it's not the last sound.
                time.sleep(float(delay))
        play_obj.wait_done()

    def do_play(self, args):
        """Play sound(s), either all at once or sequentially (with or without delay).
        usage) play [multi|seq|delay={delaytime}] <file_name(s)>
        """
        # have flags, if --multi, use multisound
        #             if --seq, use sequential
        # if delay is added, use --seq
        #             delay is of form --delay=float

        # TODO: add error catching for if --delay=(something other than float)
    
        if(self.validate("play", args)):
            input = args.split(" ")
            flags, sounds, delay = self._parse_play(input)
            
            if delay:
                print(f"play with {delay}s of delay")
                self._delay_play(sounds, delay)
            elif "multi" in flags:
                self._multi_play(sounds)  
            elif flags == [] or "seq" in flags:
                self._seq_play(sounds)
        else:
            self.do_help("play")

    def do_rename(self, args):
        """Rename an audio file.
        usage) rename <original_file> <new_name>        
        """
        if(self.validate("rename", args)):
            input = args.split(" ")
            os.rename(input[0], input[1]) 
            pass
        else:
            self.do_help("rename")

    def do_add_sound(self, args):
        """Add sound to audio archive.
        usage) add_sound <folder_to_add_to> <path_to_original_file>
        """
        pass

    def do_remove_sound(self, args):
        """Remove sound from audio archive.
        usage) remove_sound <path_to_file>
        """
        pass

    def do_list_sounds(self, args = "sounds"):
        """List sounds in specified folder.
        usage) list_sounds <folder>
        """

        if(self.validate("list_sounds", args)):
            input = args.split(" ")
            folderPath = path.Path(os.getcwd()).as_posix()+"/"+input[0]
            print(folderPath)

            for file in os.listdir(folderPath):
                if file.endswith(".wav"):      
                    print(file)   
        else:
            self.do_help("list_sounds")
                
            
    def do_party(self, args):
        """
        party time!!! prints out 'woot woot'
        usage) party
        """
        print("woot woot")

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