from tkinter import *
from tkinter import messagebox
import lyricsgenius

# Genius API key (replace with your own key from Genius Developer API)
GENIUS_API_KEY = "Rk6tOuUkddTVKfWNLkIruWg4NWZMOxBdgmFo150tAzMaBAMTkCEtx1M8FN53VGXY"

# Initialize Genius API client
genius = lyricsgenius.Genius(GENIUS_API_KEY)

# Function to fetch lyrics
def fetch_lyrics():
    artist = artist_entry.get().strip()  # Get artist name
    song = song_entry.get().strip()  # Get song title
    
    if not artist or not song:
        messagebox.showerror("Input Error", "Both fields are required!")
        return
    
    try:
        song_data = genius.search_song(song, artist)  # Search for the song on Genius
        if song_data:
            lyrics_text.delete(1.0, END)  # Clear previous lyrics
            lyrics_text.insert(END, song_data.lyrics)  # Display lyrics
        else:
            messagebox.showinfo("Not Found", "Lyrics not found for this song.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create main window
root = Tk()
root.title("Lyrics Extractor")
root.geometry("600x600")
root.configure(bg="#333")  

# Title Label
Label(
    root,
    text="Lyrics Extractor",
    font="Helvetica 20 bold",
    bg="#333",
    fg="white"
).pack(pady=10)

# Input Section
Label(root, text="Artist:", font="Arial 12", bg="#333",fg="White").pack(pady=5)
artist_entry = Entry(root, font="Arial 12", width=40)
artist_entry.pack(pady=5)

Label(root, text="Song Title:", font="Arial 12", bg="#333",fg="White").pack(pady=5)
song_entry = Entry(root, font="Arial 12", width=40)
song_entry.pack(pady=5)

# Fetch Button
Button(
    root,
    text="Fetch Lyrics",
    font="Arial 12 bold",
    bg="#ff3399",
    fg="white",
    command=fetch_lyrics
).pack(pady=10)

# Lyrics Display Box
lyrics_text = Text(root, font="Arial 12", wrap=WORD, height=20, width=60, bg="white")
lyrics_text.pack(pady=10)

# Start the GUI event loop
root.mainloop()
