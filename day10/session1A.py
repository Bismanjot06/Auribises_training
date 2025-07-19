#class Circular Doubly Linked List:

class playlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
        
    def add(self,song):
        self.size+=1
        if self.head==None:
            self.head=song
            self.tail=song
          
        else:
            self.tail.next=song
            song.previous=self.tail
            song.next=self.head
            self.head.previous=song
            self.tail=song
            
    '''        
    def inteate_forward(self):
         song=self.head
         while song.next!=self.head:
             song.show()
             song=song.next

    def inteate_backward(self):
        song=self.tail
        while song.previous!=self.tail:
            song.show()
            song=song.previous
    '''        
    
    # rather than inteate_forward and inteate_backward, we can make a single function
    # to iterate in both the directions
    
    def iteration(self, direction=0):
         if  direction==0:
             song=self.head
             while True:
                 song.show()
                 song=song.next
                 if song==self.head:
                     break
         else:
             song=self.tail
             while True:
                 song.show()
                 song=song.previous
                 if song==self.tail:
                     break 

         