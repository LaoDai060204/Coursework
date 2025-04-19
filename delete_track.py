import tkinter as tk
import tkinter.messagebox as messagebox
import track_library as lib
import font_manager as fonts
import os

class DeleteTrackWindow:
    def __init__(self, parent):
        lib.load_library()
        self.window = tk.Toplevel(parent)
        self.window.geometry("400x250")
        self.window.title("Delete Track or Playlist")
        fonts.configure()
        
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.window, text="Delete Track or Playlist", font=("Helvetica", 12)).grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        tk.Label(self.window, text="Track Number:").grid(row=1, column=0, padx=10, pady=10)
        self.entry_track_number = tk.Entry(self.window, width=5)
        self.entry_track_number.grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self.window, text="Delete Track", command=self.delete_track).grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        
        tk.Label(self.window, text="Playlist Name:").grid(row=3, column=0, padx=10, pady=10)
        self.entry_playlist_name = tk.Entry(self.window, width=20)
        self.entry_playlist_name.grid(row=3, column=1, padx=10, pady=10)
        tk.Button(self.window, text="Delete Playlist", command=self.delete_playlist).grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        
        self.status_lbl = tk.Label(self.window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def delete_track(self):
        track_number = self.entry_track_number.get().strip()
        if not track_number.isdigit():
            messagebox.showerror("Error", "Track number must be numeric")
            return
        
        formatted_number = f"{int(track_number):02d}"
        if lib.get_name(formatted_number) is None:
            messagebox.showerror("Error", f"Track {formatted_number} not found")
            return
        
        confirm = messagebox.askyesno("Confirm", f"Delete track {formatted_number}?")
        if confirm:
            del lib.library[formatted_number]
            lib.save_library()
            self.status_lbl.config(text=f"✅ Track {formatted_number} deleted")
            self.entry_track_number.delete(0, tk.END)

    def delete_playlist(self):
        playlist_name = self.entry_playlist_name.get().strip()
        if not playlist_name:
            messagebox.showerror("Error", "Playlist name cannot be empty")
            return
        
        filename = f"{playlist_name}.csv"
        if not os.path.exists(filename):
            messagebox.showerror("Error", f"Playlist '{playlist_name}' not found")
            return
        
        confirm = messagebox.askyesno("Confirm", f"Delete playlist '{playlist_name}'?")
        if confirm:
            try:
                os.remove(filename)
                self.status_lbl.config(text=f"🗑️ Playlist '{playlist_name}' deleted")
                self.entry_playlist_name.delete(0, tk.END)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete playlist: {str(e)}")

def open_delete_track(parent):
    DeleteTrackWindow(parent)

if __name__ == "__main__":
    root = tk.Tk()
    open_delete_track(root)
    root.mainloop()