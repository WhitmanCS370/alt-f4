#!/usr/bin/env python

import os

import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from datetime import datetime

from playsound import AudioPlayer
from filemanager import FileManager
from effectsmanager import EffectManager
from metadatamanager import MetadataManager

from cliadapter import CLIAdapter

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

        # Initialize the cli adapter
        self.cli = CLIAdapter()
        self.metadata = MetadataManager("metadata.db")


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

        view_metadata_button = tk.Button(self, text='View Metadata', command=self.view_metadata)
        view_metadata_button.pack(pady=10)

        quit_button = tk.Button(self, text='Quit', command=self.quit)
        quit_button.pack(pady=10)

    def play_sound(self):
        filename = filedialog.askopenfilename(title='Select a sound file', initialdir=os.getcwd(), filetypes=[('WAV files', '*.wav')])
        if filename:
            self.cli.run('play', file_path=filename)

    def view_metadata(self):
        filename = filedialog.askopenfilename(title='Select a sound file', initialdir=os.getcwd(), filetypes=[('WAV files', '*.wav')])
        print(f'filename is {filename}')
        if filename:
            metadata = self.metadata.has_metadata(os.path.basename(filename))
            if metadata:
                messagebox.showinfo("Metadata", self.metadata.stringify_metadata(os.path.basename(filename)))
            else:
                # show no metadata found, ask user if they want to add some
                add_metadata = messagebox.askyesno("No metadata found", "No metadata found for this sound file. Would you like to add some?")
                if add_metadata:
                    self.add_metadata(filename)

    def add_metadata(self, filename):
        print(f'filename is {filename}')
        tags = simpledialog.askstring("Add Tags", "Enter tags separated by commas:")
        description = simpledialog.askstring("Add Description", "Enter a description:")
        self.metadata.add("", os.path.basename(filename), self.files.find_length(filename), description, tags)
            

    def add_sound(self):
        source = filedialog.askopenfilename(title='Select a sound file to add', filetypes=[('WAV files', '*.wav')])
        if source:
            destination = filedialog.askdirectory(title='Select target folder', initialdir=os.getcwd())
            if destination:
                self.cli.run('add_sound', destination_path=destination, src=source)

    def rename_sound(self):
        original = filedialog.askopenfilename(title='Select a sound file to rename', initialdir=os.getcwd(), filetypes=[('WAV files', '*.wav')])
        if original:
            new_name = simpledialog.askstring("Rename", "Enter the new name for the sound file:")
            if new_name:
                self.cli.run('rename', original=original, new_name=new_name)

    def merge_sounds(self):
        files = filedialog.askopenfilenames(title='Select sound files to merge', initialdir=os.getcwd(), filetypes=[('WAV files', '*.wav')])
        if files:
            self.cli.run('merge', files=files)

    def trim_sound(self):
        file_path = filedialog.askopenfilename(title='Select a sound file to trim',  initialdir=os.getcwd(), filetypes=[('WAV files', '*.wav')])
        if file_path:
            start_time = simpledialog.askstring("Trim Sound", "Enter start time (seconds):")
            end_time = simpledialog.askstring("Trim Sound", "Enter end time (seconds):")
            if start_time and end_time:
                self.cli.run('trim', file_path=file_path, start_time=start_time, end_time=end_time)

    def reverse_sound(self):
        file_path = filedialog.askopenfilename(title='Select a sound file to reverse',  initialdir=os.getcwd(), filetypes=[('WAV files', '*.wav')])
        if file_path:
            self.cli.run('reverse', file_path=file_path)

    def list_sounds(self):
        folder = filedialog.askdirectory(title='Select folder to list sounds from', initialdir=os.getcwd())
        if folder:
            sounds = self.cli.run('list', folder=folder)
            if sounds:
                messagebox.showinfo("Sounds in folder", '\n'.join(sounds))
            else:
                messagebox.showinfo("Sounds in folder", "No audio files found in the selected folder.")

    def quit(self):
        self.destroy()

if __name__ == "__main__":
    app = AudioArchiveApp()
    app.mainloop()