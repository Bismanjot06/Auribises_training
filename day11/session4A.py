class flight_list:
     def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
     
     def add_flight(self, flight):
        self.size += 1
        if self.head == None:
            self.head = flight
            self.tail = flight
        else:
            self.tail.next = flight
            flight.prev = self.tail
            flight.next = self.head
            self.head.previous = flight
            self.tail = flight
       
     def iterate(self, direction=0):

        if direction == 0:
            flight = self.head
            flight.show()
            while flight.next != self.head:
                flight = flight.next
                flight.show()
        else:
            flight = self.tail
            flight.show()
            while flight.previous != self.tail:
                flight = flight.previous
                flight.show()
                
                
        def search_flight(self, flight_code):
              
            flag = False

            flight = self.head
        
            if flight.flight_code == flight_code:
                print('Flight Code Matched. Flight Found..')
                flight.show()
                flag = True
                return
            else:
                while flight.next != self.head:
                    flight = flight.next
                        
                    if flight.flight_code == flight_code :
                        print('Flight Code Matched. Flight Found..')
                        flight.show()
                        flag = True
                        break
        
            if flag == False:
                print('No Flight Matching Found...')
            

   