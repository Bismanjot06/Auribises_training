#create a class with example of youtube_channel
class youtube_channel:
    def __init__(self, name, description, subscribers=0, videos=None):
        print("youtube_channel class constructor executed")
        print('self', self, id(self), type(self))
        self.name = name
        self.description = description
        self.subscribers = subscribers
        self.videos = videos
        
    def show(self):
        print("~~~~~~~~~~~~~~~~~~~")
        print(self.name)
        print(self.description)
        print(self.subscribers)
        print(self.videos)
        print("~~~~~~~~~~~~~~~~~~~")
        print(vars(self))
        
MrBeast = youtube_channel("MrBeast", "Entertainment and philanthropy channel", 200000000,1342 )        
Ashish_Chanchlani = youtube_channel("Ashish Chanchlani", "Comedy channel", 35000000, 500)       
''' 
we can use this but using function is a better and an efficient way. eg-show()
print('data in MrBeast object')         
print(vars(MrBeast))
print('data in Ashish_Chanchlani object')      
print(vars(Ashish_Chanchlani))      
'''
Ashish_Chanchlani.show() 
MrBeast.show() 

#create a class with example of steam
class steam_games:
    def __init__(self, name, genre, description, price=0, rating=0.0 ):
        print("steam_games class constructor executed")
        print('self', self, id(self), type(self))
        self.name = name
        self.genre = genre
        self.description = description  
        self.price = price
        self.rating = rating
    def show(self):
        print("~~~~~~~~~~~~~~~~~~~")
        print(self.name)
        print(self.genre)  
        print(self.description)
        print(self.price)
        print(self.rating)
        print("~~~~~~~~~~~~~~~~~~~")
        print(vars(self))
        
GTA_V = steam_games("GTA V", "Action-Adventure", "Open world game", 2000, 4.5)        
Batman_Arkham_Knight = steam_games("Batman: Arkham Knight", "Action-Adventure", "Superhero game", 1500, 4.2)        
Detroit_Become_Human = steam_games("Detroit: Become Human", "Interactive Drama", "Narrative-driven game", 2500, 4.8)
Last_of_Us_Part_II = steam_games("The Last of Us Part II", "Action-Adventure", "Post-apocalyptic game", 3000, 4.9)

GTA_V.show()
Batman_Arkham_Knight.show() 
Detroit_Become_Human.show()
Last_of_Us_Part_II.show()