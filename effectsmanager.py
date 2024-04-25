from pydub import AudioSegment
from pydub.playback import play
import os
import pathlib as path

class EffectManager():

    def __init__(self, controller):
        self.controller = controller
        pass


    ### Helper functions

    def parse_merge(self, args):
        """Parse through merge to find out value.
        Helper function called by merge.
        Loops through all arguments and splits them into sounds and out.
        """
        input = args.split(" ")

        sounds = []
        out = None

        for item in input:
            if "-out" in item:
                outCommand = item.split("=")
                out = outCommand[1]
            elif not item =='':
                sounds.append(item)
        return sounds, out
    
    def parse_reverse(self, args):
        """Parse through reverse arguments.
        Helper function called by reverse.
        Identifies and returns out when passed, returns audio file.
        """
        input = args.split(" ")
        out = None

        if len(input) == 2:
            outCommand = input[1].split("=")
            out = outCommand[1]
            sound = input[0]
            return sound, out
        else:
            sound = input[0]
            return sound, out
        
    def parse_trim_sound(self, args):
        """Parse through trim_sound arguments.
        Helper function called by trim_sound.
        Returns the sound to trim, the start and end times that bound
        the clip to return, and the optional out that says where to save
        the trimmed sound to.
        """
        input = args.split(" ")
        out = None
        sound = input[0]
        start_time = input[1]
        end_time = input[2]

        if len(input) == 4:
            outCommand = input[3].split("=")
            out = outCommand[1]

        return sound, start_time, end_time, out
        

    ### Functionality implementation

    def merge(self, args):
        """
        """
        input = self.parse_merge(args)
        for i, item in enumerate(input[0]):
            if i == 0:
                merged = AudioSegment.from_file(f"{item}.wav", format="wav")
            else:
                itemAudio = AudioSegment.from_file(f"{item}.wav", format="wav")
                merged = merged + itemAudio

        merged.export(out_f = "merged.wav", format = "wav") 
        self.controller.do_play("merged")

        if input[1]:
            self.controller.do_rename(f"merged.wav {input[1]}.wav")
        else:
            os.remove(path.Path("merged.wav").resolve())

    def reverse(self, args):
        """
        """
        input = self.parse_reverse(args)
        sound = AudioSegment.from_wav(f"{input[0]}.wav")
        reversed_sound = sound.reverse()
        reversed_sound.export("reversed.wav", format="wav")
        self.controller.do_play("reversed")
        if input[1] != None:
            self.controller.do_rename(f"reversed.wav {input[1]}.wav")
        else:
            os.remove(path.Path("reversed.wav").resolve())

    def trim_sound(self, args):
        """ Trim a sound to a new length.
        Uses start and end times specified by the user to crop the sound to
        a new, shorter length. The new sound is played and then either saved
        to a set new file name or automatically deleted.
        """
        input = self.parse_trim_sound(args)
        sound_mp3 = AudioSegment.from_wav(f"{input[0]}.wav")
        trimmed_sound = sound_mp3[float(input[1])*1000:float(input[2])*1000]
        trimmed_sound.export(out_f = "trimmed.wav", format = "wav") 
        self.controller.do_play("trimmed")

        if input[3] != None:
            self.controller.do_rename(f"trimmed.wav {input[3]}.wav")
        else:
            os.remove(path.Path("trimmed.wav").resolve())
       