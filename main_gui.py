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
        upper_frame = tk.Frame(self, bg="red")
        edit_frame = tk.Frame(self, bg="blue")
        lower_frame = tk.Frame(self, bg="green")

        upper_frame.pack(side='top', anchor='n')
        edit_frame.pack()
        lower_frame.pack()

        # Buttons
        play_button = tk.Button(self, text='Play Sound', command=self.play_sound)
        play_button.pack(pady=10)

        add_sound_button = tk.Button(self, text='Add Sound', command=self.add_sound)
        add_sound_button.pack(pady=10)

        rename_button = tk.Button(self, text='Rename Sound', command=self.rename_sound)
        rename_button.pack(pady=10)

        list_sounds_button = tk.Button(self, text='List Sounds', command=self.list_sounds)
        list_sounds_button.pack(pady=10)

        edit_label = tk.Label(edit_frame, text="Edit Sounds")
        trim_button = tk.Button(edit_frame, text="Trim Sound", command=self.trim_sound)
        reverse_button = tk.Button(edit_frame, text="Reverse Sound", command=self.reverse_sound)
        merge_button = tk.Button(edit_frame, text='Merge Sounds', command=self.merge_sounds)

        edit_label.grid(row=0, column=1)
        trim_button.grid(row=1, column=0)
        reverse_button.grid(row=1, column=1)
        merge_button.grid(row=1, column=2)



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
                self.files.add_sound(f"{folder} {source}")

    def rename_sound(self):
        original = filedialog.askopenfilename(title='Select a sound file to rename', filetypes=[('WAV files', '*.wav')])
        if original:
            new_name = simpledialog.askstring("Rename", "Enter the new name for the sound file:")
            if new_name:
                self.files.rename(f"{original} {new_name}")

    def merge_sounds(self):
        pass

    def trim_sound(self):
        pass

    def reverse_sound(self):
        pass

    def list_sounds(self):
        folder = filedialog.askdirectory(title='Select folder to list sounds from')
        if folder:
            folder = os.path.basename(folder)
            sounds = self.files.list_sounds(folder)
            if sounds:
                messagebox.showinfo("Sounds in folder", '\n'.join(sounds))
            else:
                messagebox.showinfo("Sounds in folder", "No audio files found in the selected folder.")

    def quit(self):
        self.destroy()

if __name__ == "__main__":
    app = AudioArchiveApp()
    app.mainloop()