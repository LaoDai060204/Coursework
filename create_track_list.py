import tkinter as tk
import tkinter.scrolledtext as tkst
import track_library as lib
import font_manager as fonts
import csv

class CreateTrackListWindow:
    def __init__(self, parent):
        lib.load_library() 
        self.window = tk.Toplevel(parent)
        self.window.geometry("700x500")
        self.window.title("Create Track List")
        fonts.configure()
        
        self.playlist = []
        self.current_sort_by = "Number"
        self.sort_var = tk.StringVar(value="Number")
        
        self.setup_ui()
        self.update_playlist_display()

    def setup_ui(self):
        tk.Label(self.window, text="Playlist Name:").grid(row=0, column=0, padx=10, pady=10)
        self.entry_playlist_name = tk.Entry(self.window, width=20)
        self.entry_playlist_name.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.window, text="Enter Track Number or Song Name:").grid(row=1, column=0, padx=10, pady=10)
        self.entry_track = tk.Entry(self.window, width=5)
        self.entry_track.grid(row=1, column=1, padx=10, pady=10)
        self.entry_song_name = tk.Entry(self.window, width=20)
        self.entry_song_name.grid(row=1, column=2, padx=10, pady=10)
        tk.Button(self.window, text="Add Track", command=self.add_track).grid(row=1, column=3, padx=10, pady=10)

        tk.Button(self.window, text="Play Playlist", command=self.play_playlist).grid(row=2, column=0, padx=10, pady=10)
        tk.Button(self.window, text="Reset Playlist", command=self.reset_playlist).grid(row=2, column=1, padx=10, pady=10)
        tk.Button(self.window, text="Save Playlist", command=self.save_playlist).grid(row=2, column=2, padx=10, pady=10)
        tk.Button(self.window, text="Load Playlist", command=self.load_playlist).grid(row=2, column=3, padx=10, pady=10)

        tk.Label(self.window, text="Search Track:").grid(row=3, column=0, padx=10, pady=10)
        self.entry_search = tk.Entry(self.window, width=15)
        self.entry_search.grid(row=3, column=1, padx=10, pady=10)
        tk.Button(self.window, text="Search", command=self.search_track).grid(row=3, column=2, padx=10, pady=10)

        tk.Label(self.window, text="Sort by:").grid(row=4, column=0, padx=10, pady=10)
        tk.OptionMenu(self.window, self.sort_var, *["Number", "Name", "Artist", "Rating"]).grid(row=4, column=1, padx=10, pady=10)
        tk.Button(self.window, text="Sort", command=self.apply_sort).grid(row=4, column=2, padx=10, pady=10)

        self.text_area = tkst.ScrolledText(self.window, width=60, height=15, wrap="none")
        self.text_area.grid(row=5, column=0, columnspan=4, padx=10, pady=10)
        self.status_lbl = tk.Label(self.window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

    def update_playlist_display(self, sort_by=None):
        self.text_area.delete("1.0", tk.END)
        if not self.playlist:
            self.text_area.insert(tk.END, "Playlist is empty.")
            return

        sort_key = sort_by if sort_by else self.current_sort_by
        reverse = False
        key_func = None
        
        if sort_key == "Number":
            key_func = lambda x: int(x)
        elif sort_key == "Name":
            key_func = lambda x: lib.get_name(x).lower()
        elif sort_key == "Artist":
            key_func = lambda x: lib.get_artist(x).lower()
        elif sort_key == "Rating":
            key_func = lambda x: lib.get_rating(x)
            reverse = True
        
        sorted_playlist = sorted(self.playlist, key=key_func, reverse=reverse)
        display = "Current Playlist:\n"
        for num in sorted_playlist:
            display += f"{num}: {lib.get_name(num)}\n"
        self.text_area.insert(tk.END, display)

    def add_track(self):
        track_number = self.entry_track.get().strip()
        song_name = self.entry_song_name.get().strip()
        if track_number:
            if not track_number.isdigit():
                self.status_lbl.config(text="❌ Error: Invalid track number")
                return
            formatted_number = f"{int(track_number):02d}"  # Định dạng 2 chữ số
            if formatted_number in self.playlist:
                self.status_lbl.config(text=f"⚠️ Track {formatted_number} already in playlist")
                return
            if not lib.get_name(formatted_number):
                self.status_lbl.config(text=f"❌ Error: Track {formatted_number} not found")
                return
            self.playlist.append(formatted_number)
            self.update_playlist_display()
            self.status_lbl.config(text=f"✅ Track {formatted_number} added")
        elif song_name:
            for num, item in lib.library.items():
                if item.name.lower() == song_name.lower():
                    if num in self.playlist:
                        self.status_lbl.config(text=f"⚠️ Track {num} already in playlist")
                        return
                    self.playlist.append(num)
                    self.update_playlist_display()
                    self.status_lbl.config(text=f"✅ Track {num} added")
                    return
            self.status_lbl.config(text="❌ Error: Song name not found")
        else:
            self.status_lbl.config(text="❌ Error: Please enter a track number or song name")

    def play_playlist(self):
        if not self.playlist:
            self.status_lbl.config(text="⚠️ Playlist is empty")
            return
        for num in self.playlist:
            lib.increment_play_count(num)
        lib.save_library()
        self.status_lbl.config(text="▶️ Playlist played (play counts updated)")

    def reset_playlist(self):
        self.playlist = []
        self.update_playlist_display()
        self.status_lbl.config(text="🗑️ Playlist reset")

    def search_track(self):
        query = self.entry_search.get().strip().lower()
        if not query:
            self.status_lbl.config(text="⚠️ Please enter a search term")
            return
        
        results = []
        all_tracks = lib.list_all().splitlines()
        for line in all_tracks:
            if query in line.lower():
                results.append(line)
        
        self.text_area.delete("1.0", tk.END)
        if results:
            self.text_area.insert(tk.END, "Search Results:\n" + "\n".join(results))
            self.status_lbl.config(text=f"🔍 Found {len(results)} results")
        else:
            self.text_area.insert(tk.END, "No matching tracks found")
            self.status_lbl.config(text="⚠️ No results found")

    def save_playlist(self):
        playlist_name = self.entry_playlist_name.get().strip()
        if not playlist_name:
            self.status_lbl.config(text="❌ Error: Playlist name cannot be empty")
            return
        filename = f"{playlist_name}.csv"
        try:
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["TrackNumber"])
                for num in self.playlist:
                    writer.writerow([num])
            self.status_lbl.config(text=f"💾 Playlist saved to {filename}")
        except Exception as e:
            self.status_lbl.config(text=f"❌ Error saving: {str(e)}")

    def load_playlist(self):
        playlist_name = self.entry_playlist_name.get().strip()
        if not playlist_name:
            self.status_lbl.config(text="❌ Error: Playlist name cannot be empty")
            return
        filename = f"{playlist_name}.csv"
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                next(reader)
                self.playlist = [row[0] for row in reader if row]
            self.update_playlist_display()
            self.status_lbl.config(text=f"📂 Playlist loaded from {filename}")
        except FileNotFoundError:
            self.status_lbl.config(text=f"⚠️ Playlist '{playlist_name}' not found")
        except Exception as e:
            self.status_lbl.config(text=f"❌ Error loading: {str(e)}")

    def apply_sort(self):
        self.current_sort_by = self.sort_var.get()
        self.update_playlist_display()

def open_create_track_list(parent):
    CreateTrackListWindow(parent)

if __name__ == "__main__":
    root = tk.Tk()
    open_create_track_list(root)
    root.mainloop()