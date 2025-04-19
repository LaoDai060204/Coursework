import tkinter as tk
import tkinter.messagebox as messagebox
import track_library as lib
import font_manager as fonts

class AddTrackWindow:
    def __init__(self, parent):
        lib.load_library()  
        self.window = tk.Toplevel(parent)
        self.window.geometry("400x300")
        self.window.title("Add Track")
        fonts.configure()
        
        self.setup_ui()

    def setup_ui(self):
        fields = [
            ("Track Number:", 0),
            ("Track Name:", 1),
            ("Artist:", 2),
            ("Rating:", 3),
            ("Play Count:", 4)
        ]
        
        self.entries = {}
        for idx, (label, row) in enumerate(fields):
            tk.Label(self.window, text=label).grid(row=row, column=0, padx=10, pady=10)
            entry = tk.Entry(self.window, width=20 if idx > 0 else 5)
            entry.grid(row=row, column=1, padx=10, pady=10)
            self.entries[label] = entry
        
        tk.Button(self.window, text="Add Track", command=self.add_track).grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def add_track(self):
        number = self.entries["Track Number:"].get().strip()
        name = self.entries["Track Name:"].get().strip()
        artist = self.entries["Artist:"].get().strip()
        rating = self.entries["Rating:"].get().strip()
        play_count = self.entries["Play Count:"].get().strip()

        if not number.isdigit() or int(number) <= 0:
            messagebox.showerror("Error", "Track number must be a positive integer")
            return
        formatted_number = f"{int(number):02d}"
        if lib.get_name(formatted_number) is not None:
            messagebox.showerror("Error", f"Track {formatted_number} already exists")
            return
        if not name or not artist:
            messagebox.showerror("Error", "Name and artist are required")
            return
        if not rating.isdigit() or not (0 <= int(rating) <= 5):
            messagebox.showerror("Error", "Rating must be an integer between 0 and 5")
            return
        if not play_count.isdigit() or int(play_count) < 0:
            messagebox.showerror("Error", "Play count must be a non-negative integer")
            return
        
        lib.library[formatted_number] = lib.LibraryItem(name, artist, int(rating), int(play_count))
        lib.save_library()
        messagebox.showinfo("Success", f"Track {formatted_number} added")
        self.window.destroy()

def open_add_track(parent):
    AddTrackWindow(parent)

if __name__ == "__main__":
    root = tk.Tk()
    open_add_track(root)
    root.mainloop()