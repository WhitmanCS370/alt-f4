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
        
    def play_save_temp_audio(self, func, audio, outFile):
        """ File management for edited sounds.
        Helper function.
        The edited sound is exported and played. If the user specified an -out,
        then the temp sound is renamed into a permanent file. If no -out is
        specified, then the sound isn't saved and the temp file is deleted.
        """
        audio.export(out_f = f"{func}.wav", format = "wav") 
        self.controller.do_play(f"{func}")
        if outFile:
            self.controller.do_rename(f"{func}.wav {outFile}.wav")
        else:
            os.remove(path.Path(f"{func}.wav").resolve())


    ### Functionality implementation

    def merge(self, args):
        """ Merge audio files together sequentially.
        Merges 1+ audio files (of type .wav) together sequentially and plays
        the combined sound back to the user. If the function is called with an
        -out flag, then the merged sound can be played without having to re-merge
        the sounds.
        """
        input = self.parse_merge(args)
        for i, item in enumerate(input[0]):
            if i == 0:
                merged = AudioSegment.from_file(f"{item}.wav", format="wav")
            else:
                itemAudio = AudioSegment.from_file(f"{item}.wav", format="wav")
                merged = merged + itemAudio

        self.play_save_temp_audio("merge", merged, input[1])

    def reverse(self, args):
        """ Reverse a sound.
        Reverses the audio file passed by the user and plays the sound. If the
        user specified an -out destination, then the reversed audio file is saved
        there.
        """
        input = self.parse_reverse(args)
        sound = AudioSegment.from_wav(f"{input[0]}.wav")
        reversed_sound = sound.reverse()

        self.play_save_temp_audio("reversed", reversed_sound, input[1])

    def trim_sound(self, args):
        """ Trim a sound to a new length.
        Uses start and end times specified by the user to crop the sound to
        a new, shorter length. The new sound is played and then either saved
        to a set new file name or automatically deleted.
        """
        input = self.parse_trim_sound(args)
        sound_mp3 = AudioSegment.from_wav(f"{input[0]}.wav")
        trimmed_sound = sound_mp3[float(input[1])*1000:float(input[2])*1000]

        self.play_save_temp_audio("trimmed", trimmed_sound, input[3])
       