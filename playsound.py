import simpleaudio
import time
import random
import os


class AudioPlayer():

    def __init__(self, controller):
        self.controller = controller

    def play(self,args):
        """Delegate play sound commmand.
        Uses the 'parse' helper method to divide the inputted command.
        Chooses which function to handle the audio playing based on the flags used and
        the inputs passed to the function.
        Handles playing with delay, playing multiple sounds at a time, playing sounds
        sequentially, playing without sound, and playing a random sound from a folder.
        """
        flags, sounds, delay, folder = self.controller.parse(args)

        if delay:
            self.delay_play(sounds, delay)
        elif "multi" in flags:
            self.multi_play(sounds) 
        elif "mute" in flags:
            return
        elif "rand" in flags:
            self.random_play(folder)
        else:
            self.seq_play(sounds)

    def multi_play(self, sounds):
        """Play multiple sounds, starting at the same time.
        Called by play() when the -multi flag is used. Starts playing all sounds at the same
        time before waiting for sounds to finish.
        """
        print("Playing all sounds.")
        for sound in sounds:
            wave_obj = simpleaudio.WaveObject.from_wave_file(f"{sound}.wav")
            play_obj = wave_obj.play()
        play_obj.wait_done()
        return
        
    def seq_play(self, sounds):
        """Play multiple sounds sequentially, default.
        Called by play() when -seq flag is used, or when no flag is used. Plays each sound in
        order that they're passed and waits for the sound to complete before playing the
        next.
        """
        for sound in sounds:
            wave_obj = simpleaudio.WaveObject.from_wave_file(f"{sound}.wav")
            print(f'Playing {sound}')
            play_obj = wave_obj.play()
            play_obj.wait_done()
        return
        
    def delay_play(self, sounds, delay):
        """Play multiple sounds with delay between starts.
        Called by play() when -delay=<float> flag is used, with the float being the length
        of the delay. Functionally similar to multiplay but with added delay between sounds
        in the loop that start playing the sounds.
        """
        print(f"Playing with {delay} seconds of delay.")
        for i, sound in enumerate(sounds):
            # add delay before as long as it's not the first sound
            if i > 0:    
                time.sleep(float(delay))
            wave_obj = simpleaudio.WaveObject.from_wave_file(f"{sound}.wav")
            print(f'Playing {sound}')
            play_obj = wave_obj.play()
        play_obj.wait_done()

    def random_play(self, folder):
        """Play a random sound from a given folder.
        Called by play() when the -rand flag is used. Plays a single sound from the
        folder.

        possible extensions: allow users to pick the number of sounds to randomly
        play. let users play all sounds in a folder in (random) order.
        """
        sound = random.choice(os.listdir(folder))
        while not sound.endswith(".wav"):
            sound = random.choice(os.listdir(folder))
        print(f"playing {sound} from {folder}.")
        playSound = f"{folder}/{sound}"
        wave_obj = simpleaudio.WaveObject.from_wave_file(f"{playSound}")
        play_obj = wave_obj.play()
        play_obj.wait_done()
        
