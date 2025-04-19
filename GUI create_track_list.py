import tkinter as tk
import tkinter.scrolledtext as tkst
import font_manager as fonts

class CreateTrackListWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.geometry("700x500")
        self.window.title("Create Track List")
        fonts.configure()
        
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.window, text="Playlist Name:").grid(row=0, column=0, padx=10, pady=10)
        self.entry_playlist_name = tk.Entry(self.window, width=20)
        self.entry_playlist_name.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.window, text="Enter Track Number:").grid(row=1, column=0, padx=10, pady=10)
        self.entry_track = tk.Entry(self.window, width=5)
        self.entry_track.grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self.window, text="Add Track").grid(row=1, column=2, padx=10, pady=10)

        tk.Button(self.window, text="Play Playlist").grid(row=2, column=0, padx=10, pady=10)
        tk.Button(self.window, text="Reset Playlist").grid(row=2, column=1, padx=10, pady=10)

        self.text_area = tkst.ScrolledText(self.window, width=60, height=15, wrap="none")
        self.text_area.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
        
        self.status_lbl = tk.Label(self.window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

def open_create_track_list(parent):
    CreateTrackListWindow(parent)

if __name__ == "__main__":
    root = tk.Tk()
    open_create_track_list(root)
    root.mainloop()