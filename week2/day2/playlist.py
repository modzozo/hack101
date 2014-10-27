from song import Song

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
        ##taken from
#http://stackoverflow.com/questions/7408647/convert-dynamic-python-object-to-json
        json_output=json_dump(self,default=lambda o:o.__dict__,
            sort_keys=True,indent=4)
        file=open(file_name,"w")
        list_of_songs_to_save = []
        for song in self.songlist:
            list_of_songs_to_save(song.__dict__)


        def load(self,file_name):
            pass







