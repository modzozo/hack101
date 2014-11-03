from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from song import Song
from playlist import Playlist
import os

#TODO
class MusicCrawler:

    def __init__(self, directory):
        self.directory = directory
        self.files = []

    def generate_playlist(self):
        playlist = Playlist("Playlist")
        for dirname in os.walk(self.directory):
            print (dirname)
            for file_name in fileList:
                if file_name.endswith("*.mp3"):

                    self.files.append(self.directory + file_name)
                    id3 = ID3(self.directory + file_name)
                    mp3 = MP3(self.directory + file_name)
                    song = Song(mp3['TIT2'],
                            mp3['TPE1'],
                            mp3['TALB'],
                            5,
                            int(mp3.info.length))
        print (song)
        playlist.add_song(song)
        return playlist


def main():
    music= MusicCrawler("/home/birdy/Music/")
    playlist = music.generate_playlist()



if __name__ == '__main__':
    main()
