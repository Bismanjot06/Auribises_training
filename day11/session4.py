# applying linear srearch on linked list

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
        self.next = None
        self.prev = None

    def show(self):
         print("--------------------")
         print("carrier:", self.carrier)
         print("flight_code:", self.flight_code)
         print("source:", self.source, "|destination:", self.destination)
         print("departure:", self.departure, "|arrival:", self.arrival)
         print("duration:", self.duration)
         print("price: \u20b9", self.price)