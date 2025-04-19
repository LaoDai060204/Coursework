import tkinter as tk  # Import the Tkinter library for creating GUI components
import tkinter.scrolledtext as tkst  # Import scrolled text widget for displaying large amounts of text
import track_library as lib  # Import the track library module which handles track data operations
import font_manager as fonts  # Import font manager to configure font settings

class TrackViewer:
    """Class to create a window for viewing track information."""
    
    def __init__(self, parent):
        """Initialize the TrackViewer with a parent window."""
        lib.load_library()  # Load the track library data into memory
        self.window = tk.Toplevel(parent)  # Create a new top-level window attached to the parent
        self.window.geometry("750x350")  # Set the window dimensions to 750 pixels wide by 350 pixels high
        self.window.title("View Tracks")  # Set the title of the window to "View Tracks"
        fonts.configure()  # Apply font configurations from the font_manager module
        
        self.setup_ui()  # Call the method to set up the user interface components
        self.list_all_tracks()  # Call the method to initially display all tracks
    
    def setup_ui(self):
        """Set up the user interface components."""
        # Create a button labeled "List All Tracks" that triggers the list_all_tracks method when clicked
        tk.Button(self.window, text="List All Tracks", command=self.list_all_tracks).grid(row=0, column=0, padx=10, pady=10)
        
        # Create a label with text "Enter Track Number:" to prompt user input
        tk.Label(self.window, text="Enter Track Number:").grid(row=0, column=1, padx=10, pady=10)
        # Create an entry field for the user to input a track number, with a width of 5 characters
        self.entry_track = tk.Entry(self.window, width=5)
        self.entry_track.grid(row=0, column=2, padx=10, pady=10)  # Place the entry field in the grid
        # Create a button labeled "View Details" that triggers the view_track_details method when clicked
        tk.Button(self.window, text="View Details", command=self.view_track_details).grid(row=0, column=3, padx=10, pady=10)
        
        # Create a scrolled text area to display the list of all tracks, with specified width and height
        self.list_area = tkst.ScrolledText(self.window, width=48, height=12, wrap="none")
        self.list_area.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)  # Span across 3 columns, align west
        
        # Create a text area to display details of a selected track, with specified width and height
        self.detail_area = tk.Text(self.window, width=24, height=4, wrap="none")
        self.detail_area.grid(row=1, column=3, sticky="NW", padx=10, pady=10)  # Align northwest in the grid
        
        # Create a label to display status messages, initially empty, with a specific font
        self.status_lbl = tk.Label(self.window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, padx=10, pady=10)  # Span across 4 columns
    
    def list_all_tracks(self):
        """List all tracks in the library in the list_area."""
        self.list_area.delete("1.0", tk.END)  # Delete all existing content in the list_area from start to end
        tracks = lib.list_all()  # Retrieve a string of all tracks from the track library
        self.list_area.insert(tk.END, tracks)  # Insert the tracks string into the list_area at the end
        self.status_lbl.config(text="Listed all tracks")  # Update the status label to indicate tracks are listed
    
    def view_track_details(self):
        """View details of a specific track based on the entered track number."""
        track_number = self.entry_track.get().strip()  # Get the text from the entry field and remove whitespace
        # Format the track number to two digits if it's numeric, otherwise use it as is
        formatted_number = f"{int(track_number):02d}" if track_number.isdigit() else track_number
        name = lib.get_name(formatted_number)  # Attempt to get the track name from the library using the formatted number
        if name is None:  # Check if the track was not found
            self.detail_area.delete("1.0", tk.END)  # Delete all existing content in the detail_area
            self.detail_area.insert(tk.END, "Track not found")  # Insert "Track not found" message into the detail_area
            return  # Exit the method since no track was found
        
        # Retrieve additional track details from the library
        artist = lib.get_artist(formatted_number)  # Get the artist name for the track
        rating = lib.get_rating(formatted_number)  # Get the rating value for the track
        plays = lib.get_play_count(formatted_number)  # Get the play count for the track
        # Format the track details into a multi-line string with name, artist, rating (as stars), and plays
        details = f"{name}\n{artist}\nRating: {'★' * rating}\nPlays: {plays}"
        
        self.detail_area.delete("1.0", tk.END)  # Delete all existing content in the detail_area
        self.detail_area.insert(tk.END, details)  # Insert the formatted track details into the detail_area
        # Update the status label to show which track's details are being displayed
        self.status_lbl.config(text=f"Showing details for Track {formatted_number}")

def open_view_tracks(parent):
    """Function to open the track viewer window."""
    TrackViewer(parent)  # Create a new instance of TrackViewer with the given parent window

if __name__ == "__main__":
    """Main block to run the application for testing purposes."""
    root = tk.Tk()  # Create the main Tkinter root window
    TrackViewer(root)  # Create an instance of TrackViewer attached to the root window
    root.mainloop()  # Start the Tkinter event loop to run the application