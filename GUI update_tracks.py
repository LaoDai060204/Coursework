import tkinter as tk
import font_manager as fonts

class UpdateTrackWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.geometry("400x250")
        self.window.title("Update Track Rating")
        fonts.configure()
        
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.window, text="Enter Track Number:").grid(row=0, column=0, padx=10, pady=10)
        self.entry_track = tk.Entry(self.window, width=5)
        self.entry_track.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(self.window, text="Enter New Rating:").grid(row=1, column=0, padx=10, pady=10)
        self.entry_rating = tk.Entry(self.window, width=5)
        self.entry_rating.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Button(self.window, text="Update Track").grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        
        self.status_lbl = tk.Label(self.window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

def open_update_tracks(parent):
    UpdateTrackWindow(parent)

if __name__ == "__main__":
    root = tk.Tk()
    open_update_tracks(root)
    root.mainloop()