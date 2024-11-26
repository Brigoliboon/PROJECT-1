import unittest
from models import MusicLibrary, Track, Duration

class TestMusicLibrary(unittest.TestCase):
    def setUp(self):
        self.music_library = MusicLibrary()
        self.track1 = Track("Blinding Lights", "The Weeknd", "After Hours", Duration(minute=3, sec=20))
        self.track2 = Track("Watermelon Sugar", "Harry Styles", "Fine Line", Duration(minute=2, sec=6))
        self.music_library.insert(self.track1)
        self.music_library.insert(self.track2)

    def test_music_library_size(self):
        self.assertEqual(self.music_library.getSize(), 2)

    def test_get_track_by_index(self):
        track = self.music_library.getTrackbyIndex(self.music_library.inorder(self.music_library.getRoot()), 0)
        self.assertEqual(track.getTitle(), "Blinding Lights")
        self.assertEqual(track.getArtist(), "The Weeknd")

    def test_music_library_string_representation(self):
        self.assertIn("Blinding Lights", str(self.music_library))
        self.assertIn("Watermelon Sugar", str(self.music_library))

if __name__ == '__main__':
    unittest.main()