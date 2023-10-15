import tkinter as tk
from tkinter import filedialog
import pygame



class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("300x150")

        self.current_song = None
        self.paused = False

        self.create_widgets()

    def create_widgets(self):
        # Song label
        self.song_label = tk.Label(self.root, text="No song playing")
        self.song_label.pack(pady=10)

        # Buttons frame
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack()

        # Play button
        self.play_button = tk.Button(self.buttons_frame, text="Play", command=self.play_music)
        self.play_button.grid(row=0, column=0, padx=5)

        # Pause button
        self.pause_button = tk.Button(self.buttons_frame, text="Pause", command=self.pause_music, state=tk.DISABLED)
        self.pause_button.grid(row=0, column=1, padx=5)

        # Stop button
        self.stop_button = tk.Button(self.buttons_frame, text="Stop", command=self.stop_music, state=tk.DISABLED)
        self.stop_button.grid(row=0, column=2, padx=5)

        # Load button
        self.load_button = tk.Button(self.root, text="Load Song", command=self.load_song)
        self.load_button.pack(pady=10)

    def load_song(self):
        song_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if song_path:
            pygame.mixer.music.load(song_path)
            self.current_song = song_path
            self.song_label.config(text="Now playing: " + song_path.split("/")[-1])
            self.play_button.config(state=tk.NORMAL)

    def play_music(self):
        if not self.paused:
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.unpause()
        self.play_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.NORMAL)
        self.paused = False

    def pause_music(self):
        pygame.mixer.music.pause()
        self.pause_button.config(state=tk.DISABLED)
        self.play_button.config(state=tk.NORMAL)
        self.paused = True

    def stop_music(self):
        pygame.mixer.music.stop()
        self.stop_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.DISABLED)
        self.play_button.config(state=tk.NORMAL)
        self.song_label.config(text="No song playing")
        self.current_song = None
        self.paused = False

# Initialize pygame mixer
pygame.mixer.init()

# Create the Tkinter root window
root = tk.Tk()

# Create an instance of the MusicPlayer class
music_player = MusicPlayer(root)

# Run the Tkinter event loop
root.mainloop()
