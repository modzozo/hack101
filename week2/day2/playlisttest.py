import unittest
from playlist import Playlist
from song import Song

class PlaylistTest(unittest.TestCase):
    def setUp(self):
        self.playlist = Playlist("Indie")
        self.song1 = Song(
            "Shelter", "Years & Years", "EP", 5, "04:00", 512)
        self.song2 = Song(
            "Shelter2", "Years & Years", "EP2", 5, "04:00", 512)


    def test_add_song(self):

        self.songlist.add_song(self.song1)
        self.songlist.add_song(self.song2)

        self.assertEqual(self.songlist[0],self.song1)
        self.assertEqual(self.songlist[1],self.song2)

    def test_remove_song(self):
        self.songlist.remove_song(self.song2)
        self.ass


    def test_total_length(self):
        pass

    def test_remove_bad_quality(self):
        pass


    def test_show_artist(self):
        pass










if __name__ == '__main__':
    unittest.main()
