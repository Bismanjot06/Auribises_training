class user:
    def __init__(self):# constructor
        print("constructor executed")
        print('self', self, id(self), type(self))
        
        
class restaurant:
    def __init__(self):# constructor
        print("constructor executed")
        print('self', self, id(self), type(self))
                

#LHS: Is jhon a reference variable, they will the hashcodes
# RHS: user() is an object creation statement, which automatically executes the constructor of the class user.                
jhon = user() # object creation                
burger_king = restaurant() # object creation

print('jhon:',jhon, id(jhon), type(jhon))
print('burger_king:',burger_king, id(burger_king), type(burger_king))