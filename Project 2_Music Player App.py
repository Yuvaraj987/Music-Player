import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player App")
        self.root.geometry("400x400")
        
        self.folder_path = ""
        self.music_files = []
        self.current_index = 0
        
        pygame.mixer.init()
        
        self.select_button = tk.Button(root, text="Select Folder", command=self.load_music)
        self.select_button.pack(pady=10)
        
        self.play_button = tk.Button(root, text="Play", command=self.play_music)
        self.play_button.pack(pady=5)
        
        self.pause_button = tk.Button(root, text="Pause", command=self.pause_music)
        self.pause_button.pack(pady=5)
        
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=5)

        self.playlist_box = tk.Listbox(root, width=50, height=10)
        self.playlist_box.pack(pady=10)
    
    def load_music(self):
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            self.music_files = [
                os.path.join(self.folder_path, f) for f in os.listdir(self.folder_path)
                if f.endswith(".mp3") or f.endswith(".wav")
            ]
            self.current_index = 0

            self.playlist_box.delete(0, tk.END)
            for file in self.music_files:
                self.playlist_box.insert(tk.END, os.path.basename(file))
    
    def play_music(self):
        if self.music_files:
            pygame.mixer.music.load(self.music_files[self.current_index])
            pygame.mixer.music.play()
    
    def pause_music(self):
        pygame.mixer.music.pause()
    
    def stop_music(self):
        pygame.mixer.music.stop()
        
if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()