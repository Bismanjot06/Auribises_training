'''
oops
   Has-A relationship between objects
   
   eg. zomato has a restaurant, zomato has a user, zomato has a review
   1 restaurant have 1 menu
   1 menu has many dishes
   
    ---------------------------------------
   eg. Instagram has a user, post, comment
   1 user can have many posts
   1 post has many comments
   
   user -> name, email, phone, address,post,comment,like
    post -> title, content, date,like,comment
    comment -> content, date, user_id
    -------------------------------------------
    
    1 user can book 1 cab
    1 user can have many bookings
    1 cab has 1 driver
   
   user -> name, email, phone, address, gender
   cab -> cab_number, driver_id, model, color
   driver -> name, phone, license_number, address
   booking -> user_id, cab_id, date, time, source, destination
   
'''

# restaurant and menu example

class dish:
    #construtor- it is use to create an object
    #self is the first inut parameter 
    def __init__(self, name='NA', price=0, rating=0.0):
        self.name = name
        self.price = price
        self.rating = rating
        
    def show(self):
        print("---------DISH----------")   
        print('name:',self.name)
        print('price:', self.price)
        print('rating:', self.rating)
        
  
'''       
#LHS: dish1 -> is a refernce variable, which holds the address/hashcode of the object
#RHS: dish() -> is a constructor, which is used to create an object
dish1 = dish()
dish2 = dish('Pizza', 500, 4.5)
dish3 = dish('Burger', 200, 4.0)

print(dish1)
print(dish2)
print(dish3)

dish1.show()
dish2.show()
dish3.show()
'''