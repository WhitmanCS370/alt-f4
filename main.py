import cmd
import simpleaudio

class main(cmd.Cmd):

    def __init__(self):
        super().__init__()
        self.intro = "ooga chaka ooga ooga ooga chaka"
        self.prompt = "input command: "


    def do_play(self, args, nArgs = None):
        # have flags, if --multi, use multisound
        #             if --seq, use sequential

        # if argvlen >= index+1 and delay == None:
        #     for sound in sys.argv[index:]:                # loops through remaining sounds and plays them (works with 1 sound).
        #         print(f'Playing {sound}')
        #         play_sound(sound)
        # elif argvlen >= index+2 and delay:                  # we need one more arg (because delay takes up a arg), but play sounds.
        #     print(f"Adding {str(delay)}s of delay between sounds.")
        #     delay_sound(sys.argv[index+1:], delay)          # functions more like -p, loop in the function rather than in call.
        sounds = args.split(" ")

        for sound in sounds:
            wave_obj = simpleaudio.WaveObject.from_wave_file(f"{sound}.wav")
            play_obj = wave_obj.play()
            play_obj.wait_done()
            
    def do_party(self, args):
        print("woot woot")

    def do_exit(self, args):
        print("goodbye")
        return True

if __name__ == "__main__":
    CLI_interface = main()
    CLI_interface.cmdloop()


    # if (self.validate_single_arg(args)):
        #     self.audio.play(args)
        # else:
        #     self.provide_arg_msg()