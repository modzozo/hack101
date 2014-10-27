import unittest
from playlist import Playlist
from song import Song

class PlaylistTest(unittest.TestCase):
    def setUp(self):
        self.playlist = Playlist("Indie")
        self.song1 = Song(
            "Shelter", "Years & Years", "EP", 5, 320, 512)
        self.song2 = Song(
            "Shelter2", "Years & Years", "EP2", 5, 200, 64)


    def test_add_song(self):

        self.playlist.add_song(self.song1)
        self.playlist.add_song(self.song2)

        self.assertEqual(self.playlist.songlist[0],self.song1)
        self.assertEqual(self.playlist.songlist[1],self.song2)

    def test_remove_song(self):
        self.playlist.add_song(self.song1)
        song_name="Shelter2"
        self.playlist.remove_song(song_name)
        self.assertNotIn(song_name, self.playlist.songlist)


    def test_total_length(self):
        self.playlist.add_song(self.song1)
        self.playlist.add_song(self.song2)
        self.assertEqual(self.playlist.total_length(),520)


    def test_remove_bad_quality(self):
        self.playlist.add_song(self.song1)
        self.playlist.add_song(self.song2)
        self.playlist.remove_bad_quality()
        self.assertNotIn(self.song2,self.playlist.songlist)

    def test_save_file_with_json_output(self):






    def test_show_artist(self):
        pass


if __name__ == '__main__':
    unittest.main()
