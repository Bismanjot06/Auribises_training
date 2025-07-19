class song:
    def __init__(self, track='NA', artist='', album='', duration= 0, genre=''):
        self.track = track
        self.artist = artist
        self.album = album
        self.duration = duration
        self.genre = genre
        self.next=None
        self.previous=None
     
    def show(self):
        print('-----------------------')
        print('track:', self.track)
        print('artist:', self.artist)
        print('album:', self.album)
        print('duration:', self.duration)
        print('genre:', self.genre)