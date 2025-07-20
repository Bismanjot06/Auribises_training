flight1 ={
    'carrier': 'Air India',
    'flight_code': '6E340',
    'from': 'Chandigarh',
    'to': 'Mumbai',
    'departure_time': '5:50',
    'arrival_time': '8:20',
    'duration': 2.3,
    'price': 6499
}

flight2 = {
    'carrier': 'Air China',
    'flight_code': '62141',
    'from': 'Shangai',
    'to': 'Delhi',
    'departure_time': '10:30',
    'arrival_time': '13:00',
    'duration': 2.4,
    'price': 9499
}

flight3 ={
    'carrier': 'Indigo',
    'flight_code': '6E340',
    'from': 'Chandigarh',
    'to': 'Mumbai',
    'departure_time': '5:50',
    'arrival_time': '8:20',
    'duration': 2.3,
    'price': 6099
}

flight4 ={
    'carrier': 'Air India',
    'flight_code': 'A4F40',
    'from': 'Pune',
    'to': 'Chandigarh',
    'departure_time': '5:50',
    'arrival_time': '8:20',
    'duration': 2.3,
    'price': 8930
}

flight5 ={
    'carrier': 'Indigo',
    'flight_code': '2E3J0',
    'from': 'Chandigarh',
    'to': 'Bangalore',
    'departure_time': '13:50',
    'arrival_time': '17:20',
    'duration': 4.3,
    'price': 9357
}

flights = [flight1, flight2, flight3, flight4, flight5]


'''
source = input("Enter source location: ")
destination = input("Enter destination location: ")

#use linear search to find the flight from Chandigarh to Mumbai or Bengalore
for index in range(len(flights)):
    print(flights[index])
   
   #filtering 
for index in range(len(flights)):
    if flights[index]['from'] == source and flights[index]['to'] == destination:
        print(flights[index])
  '''      
      
   #implementation linear search on flight code     
def find_fight(flight_code): 
    flag = False    
    for index in range(len(flights)):
        if flights[index]['flight_code'] == flight_code:
            print(flights[index])
            flag = True
            break   
    
    if flag == False:
        print("Flight not found")
        