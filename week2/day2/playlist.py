from song import Song
import json

class Playlist(Song):
    LOW_BITRATE = 128

    def __init__(self, name):
        self.name = name
        self.songlist = []

    def add_song(self, Song):
        self.songlist.append(Song)

    def remove_song(self, songname):
        for song in self.songlist:
            if song.title == songname:
                self.songlist.remove(song)

    def total_length(self):
        result = 0
        for song in self.songlist:
            result += song.length
        return result

    def remove_bad_quality(self):
        for song in self.songlist:
            if song.bitrate < Playlist.LOW_BITRATE:
                self.songlist.remove(song)

    def show_artists(self):
        result = []
        for song in self.songlist:
            if song.artist not in result:
                result.append(song.artist)
        return result

    def __str__(self):
        return '\n'.join("{} {} {}:{}".format(
        song.artist, song.title, song.length // 60,
        song.length % 60) for song in self.songlist)



    def save(self,file_name):
        songs = []
        with open(file_name,"w") as writeFile:
            for each_song in self.songlist:
                songs.append(each_song.__dict__)
                jsondata = {
                "name": self.name,
                "songs": songs
                }
            result = json.dumps(jsondata,indent=4)

            writeFile.write(result)
        writeFile.close()

    def load(self,file_name):
        with open(file_name, "r") as readFile:
            data = json.loads(readFile.read())
            playlist = Playlist(data["name"])
            for song in data["songs"]:
                playlist.add_song(Song(**song))
            return playlist


def main():
    playlist = Playlist("New")
    song = Song("Years and Years", "Years",
        "Shelter", 5, 360, 320)
    song1 = Song(
        "New2", "New", "New", 2, 306, 120)
    playlist.add_song(song)
    playlist.add_song(song1)
    playlist.save('myplaylist.json')
#rs = Playlist.load('myplaylist.json')
#print(rs)
if __name__ == '__main__':
    main()






