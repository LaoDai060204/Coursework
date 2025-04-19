import tkinter as tk
import font_manager as fonts
from view_tracks import open_view_tracks
from create_track_list import open_create_track_list
from update_tracks import open_update_tracks
from add_track import open_add_track
from delete_track import open_delete_track

class Jukebox:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("700x150")
        self.window.title("JukeBox")
        self.window.configure(bg="gray")
        fonts.configure()
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.window, text="Music Player", bg="gray", font=("Helvetica", 16))\
            .grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        buttons = [
            ("View Tracks", open_view_tracks, 0),
            ("Create Track List", open_create_track_list, 1),
            ("Update Tracks", open_update_tracks, 2),
            ("Add Track", open_add_track, 3),
            ("Delete Track", open_delete_track, 4)
        ]
        
        for text, command, col in buttons:
            tk.Button(self.window, text=text, width=15, command=lambda cmd=command: cmd(self.window))\
                .grid(row=1, column=col, padx=5, pady=10)

        self.status_lbl = tk.Label(self.window, text="", bg="gray", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=5)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = Jukebox()
    app.run()