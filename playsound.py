import simpleaudio
import time


def parse_play(input):
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

def multi_play(sounds):
    for sound in sounds:
        wave_obj = simpleaudio.WaveObject.from_wave_file(f"{sound}.wav")
        play_obj = wave_obj.play()
    play_obj.wait_done()
    return
    
def seq_play(sounds):
    for sound in sounds:
        wave_obj = simpleaudio.WaveObject.from_wave_file(f"{sound}.wav")
        print(f'Playing {sound}')
        play_obj = wave_obj.play()
        play_obj.wait_done()
    return
    
def delay_play(sounds, delay):
    for i, sound in enumerate(sounds):
        if i > 0:                 # add delay as long as it's not the last sound.
            time.sleep(float(delay))
        wave_obj = simpleaudio.WaveObject.from_wave_file(f"{sound}.wav")
        print(f'Playing {sound}')
        play_obj = wave_obj.play()
    play_obj.wait_done()
