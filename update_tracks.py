import tkinter as tk
import tkinter.messagebox as messagebox
import track_library as lib
import font_manager as fonts

class UpdateTrackWindow:
    def __init__(self, parent):
        lib.load_library()
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
        
        tk.Button(self.window, text="Update Track", command=self.update_track).grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        self.status_lbl = tk.Label(self.window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def update_track(self):
        track_number = self.entry_track.get().strip()
        new_rating = self.entry_rating.get().strip()
        
        if not track_number.isdigit():
            messagebox.showerror("Error", "Invalid track number")
            return
        formatted_number = f"{int(track_number):02d}"  # Định dạng 2 chữ số
        if not new_rating.isdigit() or not (0 <= int(new_rating) <= 5):
            messagebox.showerror("Error", "Rating must be between 0-5")
            return
        
        track_name = lib.get_name(formatted_number)
        if track_name is None:
            messagebox.showerror("Error", "Track not found")
            return
        
        lib.set_rating(formatted_number, int(new_rating))
        lib.save_library()
        play_count = lib.get_play_count(formatted_number)
        self.status_lbl.config(text=f"Updated: {track_name}\nRating: {new_rating}\nPlays: {play_count}")

def open_update_tracks(parent):
    UpdateTrackWindow(parent)

if __name__ == "__main__":
    root = tk.Tk()
    open_update_tracks(root)
    root.mainloop()