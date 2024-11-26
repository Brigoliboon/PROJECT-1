import unittest
from models import Duration

class TestDuration(unittest.TestCase):
    def setUp(self):
        self.duration = Duration(hour=0, minute=3, sec=20)

    def test_duration_initialization(self):
        self.assertEqual(self.duration.getMinute(), 3)
        self.assertEqual(self.duration.getSecond(), 20)

    def test_duration_addition(self):
        duration2 = Duration(minute=2, sec=45)
        self.duration.addDuration(duration2)
        self.assertEqual(self.duration.getMinute(), 6)  # 3 + 2
        self.assertEqual(self.duration.getSecond(), 5)   # 20 + 45 = 65 seconds

if __name__ == '__main__':
    unittest.main()