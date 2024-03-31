import simpleaudio
import time
import sys

argvlen = len(sys.argv)
sounds = []

def delay_sound(filenames, delay):
    """Play sounds sequentially, with a delay between each sound.

    Arguments:
    filenames -- a list of audio files to be played.
    delay -- a float value that determines the length of the delay (in seconds).     
    """
    for fn in filenames:
        wave_obj = simpleaudio.WaveObject.from_wave_file(fn)
        print(f'Playing {fn}')
        play_obj = wave_obj.play()
        time.sleep(delay)
    play_obj.wait_done()

def play_sound(filename):
    """Play a single sound in its entirity.

    Argument:
    filename -- the name of the audio file to play.
    """
    wave_obj = simpleaudio.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def multi_sound(filenames):
    """Play multiple sounds concurrently.

    Argument:
    filenames -- a list of audio files to play concurrently.
    """
    for fn in filenames:
        wave_obj = simpleaudio.WaveObject.from_wave_file(fn)
        play_obj = wave_obj.play()
    play_obj.wait_done()

def play_sound_func():
    # also need to have a default/work without an internal flag... need to see if 
    # sys.argv[2] is a valid sound if it isn't one of our accepted flags.
    if sys.argv[2] == "-m" or sys.argv[2] == "--multi":
        play_multisound_func(3)
        
    elif sys.argv[2] == "-s" or sys.argv[2] == "--sequence":
        play_seqsound_func(3)

def play_multisound_func(index):
    """ Play multiple sounds at once.
    Arguments:
    the index the sounds start at (or a list of sounds?)
    """
    # tests
    try:
        float(sys.argv[index])              # if the first argument is a number...
        sys.argv.remove(sys.argv[index])    # get rid of it as it will cause issues in the code.
    except ValueError:
        pass

    # code to play the sounds
    if sys.argv[index]:                                # if there is a sound to play... (sys.argv[2] not null)
        for arg in sys.argv[index:]:                   # then append all of the sounds we have together...
            sounds.append(arg)
        print(f'Playing sounds')
        multi_sound(sounds)                        # and play them by calling multi_sound with the appended sounds.

def play_seqsound_func(index):
    """ Play multiple sounds one after the other.
    Arguments:
    the index the sounds start at (or a list of sounds?)
    """
    if argvlen < index + 1:
        print('No file provided...')

    # tests (and delay calculations)
    try:
        delay = float(sys.argv[index])                 # if argument casts to float without issue, save as the delay. 
    except:
        delay = None                               # if there's an error, then it's probably a string (should be a sound).
            
    # we have sound(s) to play, so the sound(s) is played (one after the other) and its name is printed when it does.
    if argvlen >= index+1 and delay == None:
        for sound in sys.argv[index:]:                # loops through remaining sounds and plays them (works with 1 sound).
            print(f'Playing {sound}')
            play_sound(sound)
    elif argvlen >= index+2 and delay:                  # we need one more arg (because delay takes up a arg), but play sounds.
        print(f"Adding {str(delay)}s of delay between sounds.")
        delay_sound(sys.argv[index+1:], delay)          # functions more like -p, loop in the function rather than in call.
