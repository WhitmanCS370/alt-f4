# alt-f4
Sams' Team

#### Group Members
- Jack Allard
- Jacob Burrill
- Coden Stark
- Sam Boerner

# How to use
To use our program, open the command line, navigate to the directory in which the main.py file is located, and run `python main.py`. Run `help` to display a help menu that lists all current functionality and how to use each. To play sound, run `play <sound-directory/sound-file>`. To play multiple sounds in various ways, run `play [-multi|-seq|-rand|-delay={delaytime}] <file_name(s)>`. Our project currently has two built-in sound directories, the 'minecraft_sounds' directory and the 'zelda' directory. More folders can be added by running `new_folder <folder_name>` (the sounds in each existing folder each can be seen by calling `list_sounds [directory-name]`). To rename a sound, run `rename <original-file> <new-name>`. Our program also implements an editing functionality with several possible edits: trim_sound, merge, and reverse. To see how to use each, run `help <command>`.  

# Epoch 1

#### Challenges
Most of our challenges stemmed from trying to use GitHub. Our group experienced our fair share of merge conflicts and weird branch issues, but we were able to handle/manage them while working together in lab. Using issues helped to prevent most conflicts, but merging back to the staging branch caused some issues whenever things became out of date. 

Outside of issues with trying to write code in the first place, our biggest hurdle while programming was deciding how to deal with the different variations of the play command. A user should be able to play a single sound, play multiple sounds concurrently, and play multiple sounds sequentially. As we divided the work to tackle different functionality all at once, playing concurrently and sequentially were done using the same tag. When we were ready to put everything together, we needed to decide how the app should work (which function should be default and which should use a new flag).

#### New architecture specifications
https://docs.google.com/document/d/e/2PACX-1vSPnYQpgqhx5gYlePdWDlQ6_wK9AGMG9exWWu7vxbkf8pdi0E2Myf2Pgi-RcGGALU7CGyCEryk2gdDc/pub
Use argparse to parse command line flags and options!

# Epoch 2 

#### Challenges
Perhaps the biggest step we took in Epoch 2 was a complete refactor of the project. This came with all sorts of challenges as most of our original code had to be tweaked in order to function properly with our new structure. A challenge we had with implementing the edit features is the tremendous amount of exceptions that could arise when a user attempts to call a command. In order to counteract these exceptions, we added validation methods that validate the commands entered by the user. These methods check the syntax of entered commands and direct the user to correct the usage if an error is thrown. 

#### Contributions
 - Coden: Commenting, refactoring, implementing all validation, implementing merge + random sound playback. Manual testing for implementing validation.
 - Jacob: Sound editing, including reverse and trim_sound. File information accessing with find_length.
 - Jack and Sam: Project planning

#### Use cases for epoch 2
https://docs.google.com/document/d/1jVy2usLuIfONpKf52ehIbkFX4-a30FGDG3DknKEAECw/edit 

# Epoch 3

#### Future modifications/changes
 1. Further extend and modify the GUI to capture every feature added from epoch 2
 2. Adding more core features to our program such as the ability for the user to make playlists, manipulate waveforms, control sound volume, speed, etc.
 3. TEST TEST TEST - write concrete test cases. This is something we didn't get to in our epochs but we need testing for a functional app.

#### Reflection and Challenges
A big problem that has spilled over from epoch 2 is how coupled CLI loop is with parsing and the actual business of the program. ideally, we would have the GUI and the CLI independent of eachother as seperate modules however multiple methods, such as play in the audioplayer module, call on the parse method of its parent (which is main). this was a strange implementation that while wouldn't be impossible to untangle, the easiest solution would be to create an adapter module that translates user input from the GUI to the CLI. The problem is that while it's easy to send information from the GUI to the CLI when it comes to changing around the filesystem or audio out, we can't really get information back. If I were to edit the dispatch (do_x) methods in main to include return values, they wouldn't have been passed through the onecwd function we call in the CLI adapter, which means having to call some component modules of the CLI directly.

#### Testing
Most of our testing was done by mimicing users. We called different functions using the command line arguments specified in the help menu and checked to make sure they had the intended effect. For renaming, we visually confirmed in our files that the original document no longer existed but a file of the new name had the same audio associated with it. Playing sounds was easier to check as there was audio associated with success (although it was occasionally hard to tell if all the sounds were playing when we called them to play concurrently). We tested edge cases and got out-of-bounds errors (that we fixed) due to the ordering of checks in some of our functions. We still need to write concrete test cases to ensure that we don't lose any of our current functionality when moving forward. 

#### Contributions
- Jack: Metadata feature (ability to add tags and description to sound, storage of timestamps and sound duration in the metadata SQLite database, integrating the metadata in the GUI, allowing the user to view and edit metadata in the GUI,) refactoring, GUI fit and finish, fixed the soundLength method.
- Sam: Designing and creating the GUI for our application, interfacing the GUI on top of the CLI, constructing user queries, designing unit test cases and failing hard!
