'''
song: track, artist, album, duration, genre
'''
class song:
    def __init__(self, track, artist, album, duration, genre):
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
        
        
song1=song(track='Nadaan Parindey',
           artist='Mohit Chouhan, A.R. Rehman',
           album='ROCKSTAR',
           duration='4.34s',
           genre='Rock')        
        
song2=song(track='Tum Ho',
           artist='Mohit Chouhan, A.R. Rehman',
           album='ROCKSTAR',
           duration='4.34s',
           genre='Rock, Rom')        
                
song3=song(track='Sadda Haq',
           artist='Mohit Chouhan, A.R. Rehman',
           album='ROCKSTAR',
           duration='4.34s',
           genre='Rock')        
  
#linking of objects with each other in next and previous form
#Hard code                
song1.next=song2
song2.next=song3 
song3.next=song1 

song1.previous=song3
song2.previous=song1
song3.previous=song2

song1.show()
song2.show()  
song3.show()              