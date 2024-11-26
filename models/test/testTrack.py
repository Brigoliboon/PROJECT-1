import unittest
from models import Track, Duration

class TestTrack(unittest.TestCase):
    def setUp(self):
        self.track = Track("Blinding Lights", "The Weeknd", "After Hours", Duration(minute=3, sec=20))

    def test_track_initialization(self):
        self.assertEqual(self.track.getTitle(), "Blinding Lights")
        self.assertEqual(self.track.getArtist(), "The Weeknd")
        self.assertEqual(self.track.getAlbum(), "After Hours")
        self.assertEqual(self.track.getDuration().durationSeconds(), 200)  # 3 minutes and 20 seconds

    def test_track_string_representation(self):
        self.assertEqual(str(self.track), "Blinding Lights - The Weeknd (After Hours) [03:20]")

if __name__ == '__main__':
    unittest.main()