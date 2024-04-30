#!/usr/bin/env python

import os

import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

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
        filename = filedialog.askopenfilename(title='Select a sound file', filetypes=[('WAV files', '*.wav')])
        if filename:
            relative_path = os.path.relpath(filename, start=os.getcwd())
            relative_path = relative_path.split('.')[0]
            relative_path = [relative_path]
            self.player.seq_play(relative_path)

    def add_sound(self):
        source = filedialog.askopenfilename(title='Select a sound file to add', filetypes=[('WAV files', '*.wav')])
        if source:
            folder = filedialog.askdirectory(title='Select target folder')
            if folder:
                relative_path = os.path.relpath(folder, start=os.getcwd())
                self.files.add_sound(f"{relative_path} {source}")

    def rename_sound(self):
        original = filedialog.askopenfilename(title='Select a sound file to rename', filetypes=[('WAV files', '*.wav')])
        if original:
            original_path = os.path.relpath(original, start=os.getcwd())
            path_dir = os.path.dirname(original_path)
            new_name = simpledialog.askstring("Rename", "Enter the new name for the sound file:")
            if new_name:
                self.files.rename(f"{original_path} {os.path.join(path_dir,new_name)}")

    def merge_sounds(self):
        pass

    def list_sounds(self):
        folder = filedialog.askdirectory(title='Select folder to list sounds from')
        if folder:
            relative_path = os.path.relpath(folder, start=os.getcwd())
            sounds = self.files.list_sounds(relative_path)
            if sounds:
                messagebox.showinfo("Sounds in folder", '\n'.join(sounds))
            else:
                messagebox.showinfo("Sounds in folder", "No audio files found in the selected folder.")

    def quit(self):
        self.destroy()

if __name__ == "__main__":
    app = AudioArchiveApp()
    app.mainloop()