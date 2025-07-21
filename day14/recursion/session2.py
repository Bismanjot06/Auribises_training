# Car: name, brand, price, range, hp

class Car:
    
    # Init function
    # to create object with initial data
    def __init__(self, name=None, brand=None, price=None, range=None, hp=None):
        self.name = name
        self.brand = brand
        self.price = price
        self.range = range
        self.hp = hp

        # Internal usage to create linked list
        self.next = None
        self.previous = None

    # to write data in object as per user
    def user_input(self):
        self.name = input('Enter Car Name: ')
        self.brand = input('Enter Car Brand: ')
        self.price = float(input('Enter Car Price: '))
        self.range = int(input('Enter Car Range: '))
        self.hp = int(input('Enter Car Horse Power: '))


    # String Function
    # to show the data of object
    # you can directly print reference variable, which will 
    # automatically execute string function
    def __str__(self):

        car_string = """
~~~~~~~~~~~~~{}~~~~~~~~~~~~~
Brand: {}
Price: {}
Range: {}
HP: {}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""".format(self.name, self.brand, self.price, self.range, self.hp)

        return car_string
    

# car = Car(name='Harrier EV', brand='Tata', price=23.8, range=650, hp=390)
# # car = Car()
# # car.user_input()
# print(car) # car.__str__()