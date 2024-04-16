from pydub import AudioSegment
from pydub.playback import play
import os
import pathlib as path

class EffectManager():

    def __init__(self, controller):
        self.controller = controller
        # if input-merge in list, do it first
        # for the rest, do it there
        #self.parseInput()
        pass

    def parse_merge(self, args):
        input = args.split(" ")

        sounds = []
        out = None

        for item in input:
            if "-out" in item:
                outCommand = item.split("=")
                out = outCommand[1]
            else:
                sounds.append(item)
        return sounds, out

    def merge(self, args):
        # thinking that any "out" sound name should have an -out flag, like -out=<filePathAndName>
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
        pass