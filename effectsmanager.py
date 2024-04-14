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

    def parseInput(self, args):
        # loop through, split on = first, then _
        # once we identify the name to call 
        pass

    def merge(self, args):
        # thinking that any "out" sound name should have an -out flag, like -out=<filePathAndName>
        input = args.split(" ")
        for i, item in enumerate(input):
            if i == 0:
                merged = AudioSegment.from_file(f"{item}.wav", format="wav")
            else:
                itemAudio = AudioSegment.from_file(f"{item}.wav", format="wav")
                merged = merged + itemAudio
        # print("Playing merged sounds.")
        # play(merged)
        merged.export(out_f = "sounds/merged.wav", format = "wav") 
        self.controller.do_play("sounds/merged")

        # if no out file specified, remove.
        os.remove(path.Path("sounds/merged.wav").resolve())

    def reverse(self, args):
        pass