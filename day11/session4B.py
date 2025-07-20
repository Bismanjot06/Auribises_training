from session4 import flights
from session4A import flight_list

flight1= flights("Air India", "6E340", "Chandigarh", "Mumbai", "5:50", "8:20", 2.3, 6499)
flight2= flights("Air China", "62141", "Shangai", "Delhi", "10:30", "13:00", 2.4, 9499)
flight3= flights("Indigo", "6E340", "Chandigarh", "Mumbai", "3:50", "6:20", 2.3, 6099)
flight4= flights("Air India", "A4F40", "Pune", "Chandigarh", "5:50", "8:20", 2.3, 8930)
flight5= flights("Indigo", "2E3J0", "Chandigarh", "Bangalore", "13:50", "16:20", 2.5, 7499)

flights= flight_list()
flights.add_flight(flight1)
flights.add_flight(flight2)
flights.add_flight(flight3)
flights.add_flight(flight4)
flights.add_flight(flight5)

