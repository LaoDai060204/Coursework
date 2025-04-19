import tkinter as tk  # Core Tkinter module for GUI elements
import tkinter.scrolledtext as tkst  # ScrolledText widget for scrollable text display
import track_library as lib  # Custom library handling track data retrieval and storage
import font_manager as fonts  # Module to apply consistent font settings across widgets

class TrackViewer:
    """Window class to display a list of tracks and show individual track details."""
    
    def __init__(self, parent):
        """Set up the track viewer window and load track library data."""
        lib.load_library()  # Initialize the track database into memory
        self.window = tk.Toplevel(parent)  # Create a floating window above the main application
        self.window.geometry("750x350")  # Define window size: width=750px, height=350px
        self.window.title("View Tracks")  # Window title shown in the title bar
        fonts.configure()  # Apply font settings from the font_manager module
        
        self.setup_ui()  # Build and layout UI components within the window
        self.list_all_tracks()  # Populate the track list on startup
    
    def setup_ui(self):
        """Construct buttons, input fields, and text areas for user interaction."""
        # Button to refresh and show every track in the library
        tk.Button(self.window, text="List All Tracks", command=self.list_all_tracks).grid(row=0, column=0, padx=10, pady=10)
        
        # Label prompting the user to enter a track ID
        tk.Label(self.window, text="Enter Track Number:").grid(row=0, column=1, padx=10, pady=10)
        # Entry widget for user to type in the desired track number
        self.entry_track = tk.Entry(self.window, width=5)
        self.entry_track.grid(row=0, column=2, padx=10, pady=10)
        # Button to display details for the track number entered above
        tk.Button(self.window, text="View Details", command=self.view_track_details).grid(row=0, column=3, padx=10, pady=10)
        
        # Scrollable text area listing all tracks available
        self.list_area = tkst.ScrolledText(self.window, width=48, height=12, wrap="none")
        self.list_area.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)
        
        # Text widget showing selected track's information
        self.detail_area = tk.Text(self.window, width=24, height=4, wrap="none")
        self.detail_area.grid(row=1, column=3, sticky="NW", padx=10, pady=10)
        
        # Status label to display messages like "Listed all tracks" or "Track not found"
        self.status_lbl = tk.Label(self.window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, padx=10, pady=10)
    
    def list_all_tracks(self):
        """Fetch all track entries and display them in the scrollable list area."""
        self.list_area.delete("1.0", tk.END)  # Clear previous content
        tracks = lib.list_all()  # Get a combined string of every track in the library
        self.list_area.insert(tk.END, tracks)  # Add the tracks text to the list widget
        self.status_lbl.config(text="Listed all tracks")  # Update status to inform the user
    
    def view_track_details(self):
        """Show detailed information for a single track, identified by its number."""
        track_number = self.entry_track.get().strip()  # Read and trim input from the entry field
        # Normalize numeric IDs to two digits (e.g., '3' becomes '03')
        formatted_number = f"{int(track_number):02d}" if track_number.isdigit() else track_number
        name = lib.get_name(formatted_number)  # Look up track title in the library
        if name is None:
            # If no matching track, clear details area and show an error message
            self.detail_area.delete("1.0", tk.END)
            self.detail_area.insert(tk.END, "Track not found")
            return
        
        # Gather other attributes for the selected track
        artist = lib.get_artist(formatted_number)
        rating = lib.get_rating(formatted_number)
        plays = lib.get_play_count(formatted_number)
        # Build a multi-line string for display: title, artist, star-rating, and play count
        details = f"{name}\n{artist}\nRating: {'★' * rating}\nPlays: {plays}"
        
        self.detail_area.delete("1.0", tk.END)  # Remove old track details
        self.detail_area.insert(tk.END, details)  # Insert the newly formatted details
        self.status_lbl.config(text=f"Showing details for Track {formatted_number}")  # Inform user which track is displayed

def open_view_tracks(parent):
    """Convenience function to instantiate the TrackViewer window."""
    TrackViewer(parent)

if __name__ == "__main__":
    # When run as a script, create the main Tkinter window and launch TrackViewer
    root = tk.Tk()
    TrackViewer(root)
    root.mainloop()
