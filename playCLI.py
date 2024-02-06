import sys
import simpleaudio

def play_sound(filename):
    wave_obj = simpleaudio.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def multi_sound(filenames):
    for fn in filenames:
        wave_obj = simpleaudio.WaveObject.from_wave_file(fn)
        play_obj = wave_obj.play()
    play_obj.wait_done()

sounds = []
if sys.argv[1] == '-p' or sys.argv[1] == '--play':
    if sys.argv[2]:
        for arg in sys.argv[2:]:
            sounds.append(arg)
        print(f'Playing sounds')
        multi_sound(sounds)
    else:
        print('no file provided...')
