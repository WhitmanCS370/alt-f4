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
        self.geometry('600x400')

        # Initialize components
        self.player = AudioPlayer(self)
        self.files = FileManager(self)
        self.effects = EffectManager(self)

        # Setup GUI
        self.create_widgets()

    def create_widgets(self):
        # Buttons
        play_button = tk.Button(self, text='Play Sound', command=self.play_sound)
        play_button.pack(pady=10)

        add_sound_button = tk.Button(self, text='Add Sound', command=self.add_sound)
        add_sound_button.pack(pady=10)

        rename_button = tk.Button(self, text='Rename Sound', command=self.rename_sound)
        rename_button.pack(pady=10)

        merge_button = tk.Button(self, text='Merge Sounds', command=self.merge_sounds)
        merge_button.pack(pady=10)

        list_sounds_button = tk.Button(self, text='List Sounds', command=self.list_sounds)
        list_sounds_button.pack(pady=10)

        # Quit button
        quit_button = tk.Button(self, text='Quit', command=self.quit)
        quit_button.pack(pady=10)

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