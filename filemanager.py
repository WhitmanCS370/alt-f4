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
        folderPath = path.Path(os.getcwd()).as_posix()+"/"+input[0]
        print(folderPath)

        for file in os.listdir(folderPath):
            if file.endswith(".wav"):      
                print(file)  

    def add_sound(self, args):
        # TODO: move the validation included in the implementation to a validator
        input = args.split(" ")
        targetDirectory = path.Path(os.getcwd()).as_posix()+"/"+input[0]
        sourcePath = path.Path(input[1]).resolve()

        if not os.path.isdir(targetDirectory): 
            print("Target directory not recognized.")
        elif os.path.exists(os.path.join(targetDirectory, os.path.basename(input[1]))):
            print("There alread exists a file in that location with that name. Please try again with another name.")
        elif not os.path.exists(sourcePath):
            print("Cannot recognize source sound file.")
        else:
            shutil.copy(sourcePath, targetDirectory)

    def remove_sound(self, args):
        input = args.split(" ")
        filePath = path.Path(input[0]).resolve()
        if not os.path.exists(filePath):
                print("Cannot recognize source file.")
        else:
            os.remove(filePath)