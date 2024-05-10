import os
from main import main

def get_relative_path(path):
    """ Translates a absolute filepath into a relative one """
    return os.path.relpath(path, start=os.getcwd())

def get_parent_path(path):
    """ Returns the parent directory path """
    return os.path.dirname(path)

class CLIAdapter(main):
    def __init__(self):
        """
        Acts as a bridge between the GUI and the CLI. Translates user interaction from the GUI into parseable user input to be ran on the CLI
        """
        super().__init__()

    def run(self, action, **kwargs):
        """ 
        Construct and execute a command as CLI input based on action and parameters 
        
        WARNING: The methods inside of Cmd do not pass along data inside of the actions they dispatch.
        Below is a list of actions that must reference private methods inside of main directly
        Subject to change and a better solution later
        - list sounds

        file_path.split('.')[0] examples relate to issue #52
        """
        if action == 'play':
            print()
            mode = kwargs.get('mode')
            if mode == 'seq' or mode == 'multi':
                files = []
                for file in kwargs.get('files'):
                    file = get_relative_path(file).split('.')[0]
                    files.append(file)
                files = ' '.join(files)
                command = f"play {'-multi' if mode == 'multi' else ''} {files}"

            elif mode == 'rand':
                folder = get_relative_path(kwargs.get('folder'))
                command = f"play -rand {folder}"

            elif mode == 'delay':
                files = []
                for file in kwargs.get('files'):
                    file = get_relative_path(file).split('.')[0]
                    files.append(file)
                files = ' '.join(files)
                delay = kwargs.get('delay')
                command = f"play -delay={delay} {files}"

        elif action == 'add_sound':
            dest = get_relative_path(kwargs.get('destination_path'))
            command = f"add_sound {dest} {kwargs.get('src')}"

        elif action == 'rename':
            dir_path = get_parent_path(kwargs.get('original')) # get parent directory
            src = get_relative_path(kwargs.get('original'))
            dest = os.path.join(dir_path, kwargs.get('new_name')) # create new merged parent directory and name
            command = f"rename {src} {dest}"

        elif action == 'list':
            path = get_relative_path(kwargs.get('folder'))
            sounds = self.files.list_sounds(path)
            return sounds
        
        elif action == 'merge':
            files = []
            for file in kwargs.get('files'):
                file = get_relative_path(file).split('.')[0]
                files.append(file)
            files = ' '.join(files)
            command = f"merge {files}"

        elif action == 'trim':
            file_path = get_relative_path(kwargs.get('file_path')).split('.')[0]
            start_time = kwargs.get('start_time')
            end_time = kwargs.get('end_time')
            command = f"trim_sound {file_path} {start_time} {end_time}"

        elif action == 'reverse':
            file_path = get_relative_path(kwargs.get('file_path')).split('.')[0]
            command = f"reverse {file_path}"

        # Execute the constructed command
        self.onecmd(command)
