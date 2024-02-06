import sys
import simpleaudio

def play_sound(filename):
    wave_obj = simpleaudio.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()

if sys.argv[1] == '-p' or sys.argv[1] == '--play':
    if sys.argv[2]:
        print(f'Playing {sys.argv[2]}')
        file = sys.argv[2]
        play_sound(file)
        
if sys.argv[1] == '-ls' or sys.argv[1] == '--list_sounds':
           
    else:
        print('no file provided...')
