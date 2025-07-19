from session1 import song
from session1A import playlist

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




songs_playlist=playlist()
songs_playlist.add(song=song1)
songs_playlist.add(song=song2)
songs_playlist.add(song=song3)

# songs_playlist.iterate_forward()
# songs_playlist.iterate_backward()

songs_playlist.iteration()