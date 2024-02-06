import sys
import simpleaudio
import os

def play_sound(filename):
    wave_obj = simpleaudio.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()

if sys.argv[1] == '-p' or sys.argv[1] == '--play':
    if sys.argv[2]:
        print(f'Playing {sys.argv[2]}')
        file = sys.argv[2]
        play_sound(file)
        
    else:
        print('no file provided...')

if sys.argv[1] == '-r' or sys.argv[1] == '--rename':
    if sys.argv[2]:
        os.rename(sys.argv[2], sys.argv[3])
    else:
        print('no file provided...')
