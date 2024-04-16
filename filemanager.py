import os
import pathlib as path
import shutil

class FileManager():

    def __init__(self, controller):
        self.controller = controller

    def rename(self, args):
        input = args.split(" ")
        os.rename(input[0], input[1])
    
    def list_sounds(self, args):
        input = args.split(" ")
        targetDirectory = path.Path(os.getcwd()).as_posix()+"/"+input[0]

        for file in os.listdir(targetDirectory):
            if file.endswith(".wav"):      
                print(file)  

    def add_sound(self, args):
        input = args.split(" ")
        targetDirectory = path.Path(os.getcwd()).as_posix()+"/"+input[0]
        sourcePath = path.Path(input[1]).resolve()
        shutil.copy(sourcePath, targetDirectory)

    def remove_sound(self, args):
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

        """
        # TODO: currently prints all folders, should only print folders with audio file.
        for item in os.listdir(os.getcwd()):
            if os.path.isdir(item):
                print(f"{item}")


    def remove_folder(self, args):
        """Remove existing folder.
        
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