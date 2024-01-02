import os
import pygame
from tkinter import Tk, Button, Label, filedialog

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player By KRN")
        self.root.geometry("400x200")
        pygame.init()
        self.current_track = ""
        self.playing = False
        self.track_label = Label(root, text="No track selected", font=("Helvetica", 12))
        self.track_label.pack(pady=10)
        self.play_button = Button(root, text="Play", command=self.play_pause)
        self.play_button.pack(pady=10)
        self.select_button = Button(root, text="Select Track", command=self.select_track)
        self.select_button.pack(pady=10)
    def select_track(self):
        track_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
        if track_path:
            self.current_track = track_path
            self.track_label.config(text=os.path.basename(track_path))
            pygame.mixer.music.load(track_path)
    def play_pause(self):
        if self.current_track:
            if not self.playing:
                pygame.mixer.music.play()
                self.playing = True
                self.play_button.config(text="Pause")
            else:
                pygame.mixer.music.pause()
                self.playing = False
                self.play_button.config(text="Play")
if __name__ == "__main__":
    root = Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
