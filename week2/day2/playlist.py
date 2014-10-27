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
        result = []
        for item in range(0, len(self.songlist)):
            if self.songlist[item].bitrate > Playlist.LOW_BITRATE:
                result.append(self.songlist[item])
            self.songlist = result
        return self.songlist

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


        d = {"name":"interpolator","children":[{'name':key,"size":value} for key,value in sample.items()]}
        j = json.dumps(d, indent=4)
        f = open('sample.json', 'w')
        print >> f, j
        f.close()
        song_dict = {}
        test_song.__dict__

        def load(self,file_name):







