# alt-f4
Sams' Team

#### Group Members
- Jack Allard: rename sounds, single sound playback.
- Jacob Burrill: list available sounds (of default 'sounds' directory and specified directories.
- Coden Stark: help menu update (lists the available commands), commented the code, shortened the sequential sounds play function, added delay sound to sequential play (and first arg checks)
- Sam Boerner: simultaneous sounds playback.

# How to use
To use our program, open the command line, navigate to the directory in which the playCLI.py file is located, and run `python playCLI.py`. This displays a help menu that lists all current functionality and how to use each. To play sound, run `python playCLI.py -p [sound-directory/sound-file.wav]`. If multiple sound files are used as arguments when calling `-p`, then the sounds play concurrently. To play sounds sequentially, run `python playCLI.py -s [optional delay] [sound-directory/sound-file.wav]...`. Our project currently has two built-in sound directories, the default 'sounds' directory and the 'minecraft_sounds' directory (the sounds in each can be seen by calling `python playCLI.py -ls [directory-name]`). To rename a sound, run `python playCLI.py -r [original-file] [new-name]`.

# Epoch 1

#### Challenges
Most of our challenges stemmed from trying to use GitHub. Our group experienced our fair share of merge conflicts and weird branch issues, but we were able to handle/manage them while working together in lab. Using issues helped to prevent most conflicts, but merging back to the staging branch caused some issues whenever things became out of date. 

Outside of issues with trying to write code in the first place, our biggest hurdle while programming was deciding how to deal with the different variations of the play command. A user should be able to play a single sound, play multiple sounds concurrently, and play multiple sounds sequentially. As we divided the work to tackle different functionality all at once, playing concurrently and sequentially were done using the same tag. When we were ready to put everything together, we needed to decide how the app should work (which function should be default and which should use a new flag).

#### Future modifications/changes
The most obvious modification would be allowing our app to function with sound files of different file types. Our program works well for .wav files, but only for .wav files. If we want an app that can act as an audio archive, then it needs to accept a wider range of audio file types in order to capture/use a wider range of sounds from the user's life. We have a place to add file extensions when we can use them, but the functions we use to play sound only work with .wav files.
Adding sound editing is an upcoming issue, and might demand some changes in base functionality. We'll probably need to add functionality that allows for sound saving. The play functions might also need to take more arguments (like what sound modifications and on which sounds), but how we decide to implement sound edits plays a big role in the change we'll need to make.

#### Testing
Most of our testing was done by mimicing users. We called different functions using the command line arguments specified in the help menu and checked to make sure they had the intended effect. For renaming, we visually confirmed in our files that the original document no longer existed but a file of the new name had the same audio associated with it. Playing sounds was easier to check as there was audio associated with success (although it was occasionally hard to tell if all the sounds were playing when we called them to play concurrently). We tested edge cases and got out-of-bounds errors (that we fixed) due to the ordering of checks in some of our functions. Before getting too far into the next epoch, we need to write concrete test cases to ensure that we don't lose any of our current functionality when moving forward.

More recent additions to testing include checking the type of the first argument in the `-play` and `-sequence` commands. While it would be worthwile to check if the arguments are normally within the available sounds, checking for numbers makes it easier to implement the delay functionality.


## Check-in 2-2
So far, we have implemented a simple CLI that is able to play an audio file which is passed in as an argument through the command line.

### Use cases/User stories
https://docs.google.com/document/d/1Bvmg0npipdcdK8qbS1LAFQIgXJsy3d2tt_Xbh7vTE2g/edit
