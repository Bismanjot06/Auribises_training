from session2 import Car
from session2a import CarList

list = CarList() # head, tail and size
car1 = Car(name='Harrier EV', brand='Tata', price=23.8, range=650, hp=390)
car2 = Car(name='Kia EV6', brand='Kia', price=60.0, range=528, hp=325)
car3 = Car(name='Hyundai Ioniq 5', brand='Hyundai', price=50.0, range=480, hp=225)
car4 = Car(name='MG ZS EV', brand='MG', price=25.0, range=461, hp=174)
car5 = Car(name='Tata Nexon EV', brand='Tata', price=15.0, range=312, hp=127)

list.iterate()