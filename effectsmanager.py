from pydub import AudioSegment
from pydub.playback import play
import os
import pathlib as path

class EffectManager():

    def __init__(self, controller):
        self.controller = controller
        pass

    def parse_merge(self, args):
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

    def parse_reverse(self, args):
        input = args.split(" ")
        out = None

        if (len(input) == 2) and ("-out" in input[1]):
            outCommand = input[1].split("=")
            out = outCommand[1]
            sound = input[0]
            return sound, out
        else:
            sound = input[0]
            return sound, out

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
        

    def parse_trim_sound(self, args):
        input = args.split(" ")
        out = None
        
        if (len(input) == 4) and ("-out" in input[3]):
            outCommand = input[3].split("=")
            out = outCommand[1]
            sound = input[0]
            start_time = input[1]
            end_time = input[2]
            return sound, start_time, end_time, out
        else:
            sound = input[0]
            start_time = input[1]
            end_time = input[2]
            return sound, start_time, end_time
    
    def sec_to_millisecond(self, seconds):
        """Convert seconds to milliseconds.
        """
        return seconds * 1000

    def trim_sound(self, args):
        """ trim a sound to a new length"""
        input = self.parse_trim_sound(args)
        sound_mp3 = AudioSegment.from_wav(f"{input[0]}.wav")
        trimmed_sound = sound_mp3[float(input[1])*1000:float(input[2])*1000]
        trimmed_sound.export(out_f = "trimmed.wav", format = "wav") 
        self.controller.do_play("trimmed")

        if len(input) == 4:
            self.controller.do_rename(f"trimmed.wav {input[3]}.wav")
        else:
            os.remove(path.Path("trimmed.wav").resolve())

    def parse_find_length(self, args):
        """
        """
        input = args.split(" ")
        sound = input[0]
        return sound
    
    def find_length(self, args):
        """Find the length of a sound file"""
        input = self.parse_find_length(args)
        sound = AudioSegment.from_wav(f"{input}.wav")
        length = len(sound)
        length_seconds = length / 1000
        print(length_seconds)
       