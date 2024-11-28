import sys
sys.path.append("models\\")
__name__ = "models"
__all__ = ["Track","Duration", "Playlist", "MusicLibrary", "ArrayList"]
from .track import Track, Duration
from .Playlist import Playlist, MusicLibrary
from .Queue import ArrayList, Queue