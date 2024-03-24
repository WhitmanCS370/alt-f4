import sys

MENUINTRO = {
    print("usage:",sys.argv[0], '[command] [arg(s)]'),
    print('commands:           description + usage:')
}

HELPMENU = {
    "--help, -h": "lists help menu, what each function is and how to use it.",
    "--play, -p": "plays sound(s) that are passed as argument(s) in form \'directory/filename.wav\'. When multiple sounds are passed as arguments, the sounds play all at once.",
    "--sequence, -s": "plays provided sounds sequentially. Sounds are passed as argument(s) in form \'directory/filename.wav\'. To play sounds with a set amount of delay between starts, pass a number as the first argument.",
    "--rename, -r": "changes name of file (specified by first argument) to name specified in second argument.",
    "--list_sounds, -ls": "lists all of the sounds/files in the default sounds directory. To list from non-default directories, the directory name should be passed as argument."
}