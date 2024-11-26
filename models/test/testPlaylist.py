import sys
import unittest
sys.path.append(".")
from models import Playlist, Track, Duration

class TestPlaylist(unittest.TestCase):
    def setUp(self):
        self.playlist = Playlist("My Favorite Songs")
        self.track1 = Track("Blinding Lights", "The Weeknd", "After Hours", Duration(minute=3, sec=20))
        self.track2 = Track("Watermelon Sugar", "Harry Styles", "Fine Line", Duration(minute=2, sec=6))
        self.playlist.insert(self.track1)
        self.playlist.insert(self.track2)

    def test_playlist_title(self):
        self.assertEqual(self.playlist.getTitle(), "My Favorite Songs")

    def test_playlist_duration(self):
        total_duration = self.playlist.getDuration()
        self.assertEqual(total_duration.getMinute(), 5)  # 3 + 2 minutes
        self.assertEqual(total_duration.getSecond(), 26)  # 20 + 6 seconds

    def test_playlist_string_representation(self):
        print(str(self.playlist))
        self.assertIn("My Favorite Songs", str(self.playlist))

if __name__ == '__main__':
    unittest.main()