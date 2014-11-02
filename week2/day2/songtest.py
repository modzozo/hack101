import unittest
from song import Song

class SongTest(unittest.TestCase):

    def setUp(self):
        self.song = Song("Shelter", "Years & Years","EP",4,"04:00",128)

    def test_init(self):
        self.assertEqual(self.song.title, "Shelter")
        self.assertEqual(self.song.artist, "Years & Years")
        self.assertEqual(self.song.album,"EP")
        self.assertEqual(self.song.rating,4)
        self.assertEqual(self.song.length,"04:00")
        self.assertEqual(self.song.bitrate,128)

    def test_rate_outofvalue(self):
        self.song.rate(4)
        self.assertEqual(self.song.rating, 4)
        with self.assertRaises(ValueError):
            self.song.rate(6)







if __name__ == '__main__':
    unittest.main()

