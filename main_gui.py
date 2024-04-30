#!/usr/bin/env python

import os

import tkinter as tk

from playsound import AudioPlayer
from filemanager import FileManager
from effectsmanager import EffectManager

class AudioArchiveApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Audio Archive Manager')

        # Initialize components
        self.player = AudioPlayer(self)
        self.files = FileManager(self)
        self.effects = EffectManager(self)

        # Setup GUI
        self.create_widgets()

    def create_widgets(self):
        pass

    def play_sound(self):
        pass

    def add_sound(self):
        pass

    def rename_sound(self):
        pass

    def merge_sounds(self):
        pass

    def list_sounds(self):
        pass

    def quit(self):
        pass

if __name__ == "__main__":
    app = AudioArchiveApp()
    app.mainloop()