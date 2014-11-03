
class Song:

    MAX_RATING = 5
    MIN_RATING = 1

    def __init__(self,title,artist,album,rating,length,bitrate):
        self.title = title
        self.artist = artist
        self.album = album
        self.rating = rating
        self.length = length
        self.bitrate = bitrate

    def rate(self, value):
        if value < Song.MIN_RATING or value > Song.MAX_RATING:

            raise ValueError
        self.rating = value

