# oops
#1. think of an object
#2. create a class
#3. create a object
#4. use the object

class flights:
    def __init__(self, carrier, flight_code, source, destination, departure, arrival, duration, price):
        self.carrier = carrier
        self.flight_code = flight_code
        self.source = source
        self.destination = destination
        self.departure = departure
        self.arrival = arrival
        self.duration = duration
        self.price = price

    def show(self):
         print("--------------------")
         print("carrier:", self.carrier)
         print("flight_code:", self.flight_code)
         print("source:", self.source, "|destination:", self.destination)
         print("departure:", self.departure, "|arrival:", self.arrival)
         print("duration:", self.duration)
         print("price: \u20b9", self.price)
         
flight1= flights("Air India", "6E340", "Chandigarh", "Mumbai", "5:50", "8:20", 2.3, 6499)
flight2= flights("Air China", "62141", "Shangai", "Delhi", "10:30", "13:00", 2.4, 9499)
flight3= flights("Indigo", "6E340", "Chandigarh", "Mumbai", "3:50", "6:20", 2.3, 6099)
flight4= flights("Air India", "A4F40", "Pune", "Chandigarh", "5:50", "8:20", 2.3, 8930)
flight5= flights("Indigo", "2E3J0", "Chandigarh", "Bangalore", "13:50", "16:20", 2.5, 7499)


#list of flight objects
flights = [flight1, flight2, flight3, flight4, flight5]

#for index in range(len(flights)):
#    flights[index].show()
    
    