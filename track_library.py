from library_item import LibraryItem
import json

library = {}
library["01"] = LibraryItem("Another Brick in the Wall", "Pink Floyd", 4)
library["02"] = LibraryItem("Stayin' Alive", "Bee Gees", 5)
library["03"] = LibraryItem("Highway to Hell", "AC/DC", 2)
library["04"] = LibraryItem("Shape of You", "Ed Sheeran", 1)
library["05"] = LibraryItem("Someone Like You", "Adele", 3)

def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output

def get_name(key):
    return library[key].name if key in library else None

def get_artist(key):
    return library[key].artist if key in library else None

def get_rating(key):
    return library[key].rating if key in library else -1

def set_rating(key, rating):
    if key in library:
        library[key].rating = rating

def get_play_count(key):
    return library[key].play_count if key in library else -1

def increment_play_count(key):
    if key in library:
        library[key].play_count += 1

def save_library(filename="library.json"):
    with open(filename, "w") as file:
        json.dump({key: item.__dict__ for key, item in library.items()}, file)

def load_library(filename="library.json"):
    global library
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            library = {key: LibraryItem(**values) for key, values in data.items()}
    except FileNotFoundError:
        pass