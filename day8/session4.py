#1. Think of an object
'''
song -> title, artist, album, duration, genre, release_date etc
'''
#2. create its class
class Song:
    def __init__(self):
        print("Song class constructor executed")
        print('self', self, id(self), type(self))
        
#3. create object from the class defination
Mohit_Chauhan = Song() # object creation
print('Mohit_Chauhan:', Mohit_Chauhan, id(Mohit_Chauhan), type(Mohit_Chauhan))        

print('data in object referred ') # empty dictionary, no data in object
print(vars(Mohit_Chauhan)) # shows the attributes of the object, but no data in it

#4. write data in object
Mohit_Chauhan.title = "Naadaan Parindey"
Mohit_Chauhan.artist= "Mohit Chauhan, A.R. Rahman"
Mohit_Chauhan.album = "Rockstar"
Mohit_Chauhan.duration = "4:30"

print('data in object after writing data')
print(vars(Mohit_Chauhan)) # shows the attributes of the object with data in it