import sys
import simpleaudio
import os

def play_sound(filename):
    wave_obj = simpleaudio.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def play_sound_sequence(filenames):
    for sound in sys.argv[2:]:
        print(f'Playing {sound}')
        file = sound
        play_sound(file)

if sys.argv[1] == '-p' or sys.argv[1] == '--play':
    playing_sequence = False

    if len(sys.argv) < 3:
        print('No file provided...')
    elif len(sys.argv) == 3:
        print(f'Playing {sys.argv[2]}')
        file = sys.argv[2]
        play_sound(file)
    # if there are more than 2 arguments, then we are playing a sequence
    elif len(sys.argv) > 3:
        play_sound_sequence(sys.argv[2:])


if sys.argv[1] == '-r' or sys.argv[1] == '--rename':
    if sys.argv[2]:
        os.rename(sys.argv[2], sys.argv[3])
    else:
        print('no file provided...')
