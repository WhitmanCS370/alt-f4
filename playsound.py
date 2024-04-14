import simpleaudio
import time


class AudioPlayer():

    def __init__(self, controller):
        self.controller = controller

    def play(self,args):
        input = args.split(" ")
        flags, sounds, delay = self.controller.parse_play(input)
        
        if delay:
            self.delay_play(sounds, delay)
        elif "multi" in flags:
            self.multi_play(sounds) 
        elif "mute" in flags:
            return
        elif flags == [] or "seq" in flags:
            self.seq_play(sounds)

    def multi_play(self, sounds):
        print("Playing all sounds.")
        for sound in sounds:
            wave_obj = simpleaudio.WaveObject.from_wave_file(f"{sound}.wav")
            play_obj = wave_obj.play()
        play_obj.wait_done()
        return
        
    def seq_play(self, sounds):
        for sound in sounds:
            wave_obj = simpleaudio.WaveObject.from_wave_file(f"{sound}.wav")
            print(f'Playing {sound}')
            play_obj = wave_obj.play()
            play_obj.wait_done()
        return
        
    def delay_play(self, sounds, delay):
        print(f"Playing with {delay} seconds of delay.")
        for i, sound in enumerate(sounds):
            if i > 0:                 # add delay as long as it's not the last sound.
                time.sleep(float(delay))
            wave_obj = simpleaudio.WaveObject.from_wave_file(f"{sound}.wav")
            print(f'Playing {sound}')
            play_obj = wave_obj.play()
        play_obj.wait_done()
