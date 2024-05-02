import os
from main import main

def get_relative_path(path):
    """ Translates a absolute filepath into a relative one """
    return os.path.relpath(path, start=os.getcwd())

def get_parent_path(path):
    return os.path.dirname(path)

class CLIAdapter(main):
    def __init__(self):
        """
        Acts as a bridge between the GUI and the CLI. Translates user interaction from the GUI into parseable user input to be ran on the CLI
        """
        super().__init__()

    def run(self, action, **kwargs):
        """ Construct and execute a command as CLI input based on action and parameters """
        if action == 'play':
            file_path = get_relative_path(kwargs.get('file_path'))
            file_path = file_path.split('.')[0] # refers to issue #52
            command = f"play {file_path}"

        elif action == 'add_sound':
            dest = get_relative_path(kwargs.get('destination_path'))
            command = f"add_sound {dest} {kwargs.get('src')}"

        elif action == 'rename':
            dir_path = get_parent_path(kwargs.get('original')) # get parent directory
            src = get_relative_path(kwargs.get('original'))
            dest = os.path.join(dir_path, kwargs.get('new_name')) # create new merged parent directory and name
            command = f"rename {src} {dest}"

        elif action == 'list':
            # Uses the file manager because we need to fetch list_sounds return value, which is not provided through onecwd
            path = get_relative_path(kwargs.get('folder'))
            sounds = self.files.list_sounds(path)
            return sounds

        # Execute the constructed command
        self.onecmd(command)
