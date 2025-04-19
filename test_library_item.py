import pytest
from library_item import LibraryItem

def test_library_item_init():
    item = LibraryItem("Test Song", "Test Artist", 3, 10)
    assert item.name == "Test Song"
    assert item.artist == "Test Artist"
    assert item.rating == 3
    assert item.play_count == 10

def test_library_item_info():
    item = LibraryItem("Test Song", "Test Artist", 3, 10)
    assert item.info() == "Test Song - Test Artist ★★★"

def test_library_item_stars():
    item = LibraryItem("Test Song", "Test Artist", 5, 10)
    assert item.stars() == "★★★★★"
    item.rating = 0
    assert item.stars() == ""
    item.rating = 2
    assert item.stars() == "★★"

def test_library_item_invalid_rating():
    with pytest.raises(ValueError):
        LibraryItem("Test Song", "Test Artist", -1, 10)
    with pytest.raises(ValueError):
        LibraryItem("Test Song", "Test Artist", 6, 10)