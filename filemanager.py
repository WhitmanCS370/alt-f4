import os
import pathlib as path
import shutil
from pydub import AudioSegment

class FileManager():

    def __init__(self, controller):
        self.controller = controller

    def rename(self, args):
        """Rename a sound file.
        Changes the name of a sound file, given a valid sound file and an
        unused name.
        """
        input = args.split(" ")
        os.rename(input[0], input[1])
    
    def list_sounds(self, args):
        """Display a list of sounds in a folder.
        Prints all sounds from within a specified folder. Only files that end
        in '.wav' are printed, since it should only display sounds that are
        playable.
        """
        input = args.split(" ")
        targetDirectory = path.Path(os.getcwd()).as_posix()+"/"+input[0]

        for file in os.listdir(targetDirectory):
            if file.endswith(".wav"):      
                print(file)  

    def add_sound(self, args):
        """Add sound to a folder.
        Copies a sound file from a specified source path (can be internal or
        external of the working directory) to a folder.
        """
        input = args.split(" ")
        targetDirectory = path.Path(os.getcwd()).as_posix()+"/"+input[0]
        sourcePath = path.Path(input[1]).resolve()
        shutil.copy(sourcePath, targetDirectory)

    def remove_sound(self, args):
        """Remove sound.
        Deletes the file from the provided path.
        """
        input = args.split(" ")
        filePath = path.Path(input[0]).resolve()
        os.remove(filePath)

    def new_folder(self, args):
        """Make new folder.
        Uses os library to make a new folder/directory with a provided name.
        """
        input = args.split(" ")
        os.mkdir(input[0])

    def list_folders(self, args):
        """List folders in current working directory.
        Prints the name of all folders.
        """
        # TODO: currently prints all folders, should only print folders with audio file.
        currentFolder = os.listdir(os.getcwd())
        if args:
            currentFolder = os.listdir(path.Path(os.getcwd()).as_posix()+"/"+args)
        for item in currentFolder:
            if os.path.isdir(item) or os.path.isdir(args + '/' + item):
                print(f"{item}")

    def remove_folder(self, args):
        """Remove existing folder.
        If a folder is empty, it can be removed without a flag. If a non-empty
        folder is passed without a flag, then it errors (warning the user that
        the folder isn't empty). The -empty flag allows the user to remove empty
        folders and the -nonempty flag allows the user to remove non-empty
        folders.
        """
        # TODO: can handle differently. if user deletes nonempty folder, can make a trash folder
        # that keeps all sounds from deleted folders and auto-deletes on exit.
        flags, sounds, delay, folder = self.controller.parse(args)
        
        if sounds or delay:
            print("Error: remove_folder doesn't work with sounds or delay.")
            return
        elif "nonempty" in flags:
            shutil.rmtree(folder)
            print(f"{folder} removed.")
        elif "empty" in flags or (flags == []):
            os.rmdir(folder)
            print(f"{folder} removed.")

    def parse_find_length(self, args):
        """
        """
        input = args.split(" ")
        sound = input[0]
        return sound
    
    def find_length(self, args):
        """Find the length of a sound file"""
        input = self.parse_find_length(args)
        sound = AudioSegment.from_wav(f"{input}.wav")
        length = len(sound)
        length_seconds = length / 1000
        print(f"{length_seconds} seconds")