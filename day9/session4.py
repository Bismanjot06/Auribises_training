from session1 import dish
from session2 import menu
from session3 import restaurant


#list of dishes
#        0       1      2
# dishes=[dish1, dish2, dish3]
#print('dishes',dishes)
#print('hashcode of dishes:', id(dishes))


my_restaurant = restaurant(name='Yum_food',
                           address='Margpur',
                           email='chotu@gmail.com',
                           rating=4.5, 
                           menu=menu('Indian_menu', 
                                      dishes =[
                                                dish(),
                                                dish('Pizza', 500, 4.5),
                                                 dish('Burger', 200, 4.0)

                                               ], # here we done 1 to many mapping
                                     number_of_dishes=3
                                     )
)
my_restaurant.show()
