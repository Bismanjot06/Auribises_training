#applying bubble sort function on list of dictionaries

flight1 = {
    'carrier': 'indigo',
    'flight_code': '6e642',
    'from': 'chandigarh',
    'to': 'mumbai',
    'departure': '05:50',
    'arrival': '08:20',
    'duration': 2.3,
    'fare': 6499
}

flight2 = {
    'carrier': 'air india',
    'flight_code': 'ai2660',
    'from': 'chandigarh',
    'to': 'mumbai',
    'departure': '17:50',
    'arrival': '20:45',
    'duration': 2.5,
    'fare': 7260
}

flight3 = {
    'carrier': 'indigo',
    'flight_code': '6e5234',
    'from': 'chandigarh',
    'to': 'mumbai',
    'departure': '16:30',
    'arrival': '19:05',
    'duration': 2.3,
    'fare': 7649
}

flight4 = {
    'carrier': 'air india',
    'flight_code': 'ai522',
    'from': 'chandigarh',
    'to': 'bengaluru',
    'departure': '16:30',
    'arrival': '19:30',
    'duration': 3.0,
    'fare': 6606
}

flight5 = {
    'carrier': 'indigo',
    'flight_code': '6e6634',
    'from': 'chandigarh',
    'to': 'bengaluru',
    'departure': '08:25',
    'arrival': '11:30',
    'duration': 3.5,
    'fare': 6867
}

# List of Dictionary Objects
flights = [flight1, flight2, flight3, flight4, flight5]

def sort(flights, low_to_high=0):
    if low_to_high==0:
       for i in range(len(flights)-1):
            for j in range(len(flights)-i-1): 
                if flights[j]['fare']>flights[j+1]['fare']:
                    temp=flights[j]
                    flights[j]=flights[j+1]
                    flights[j+1]=temp
            
    else:
        for i in range(len(flights)-1):
            for j in range(len(flights)-i-1):
                if flights[j]['fare']<flights[j+1]['fare']:
                    temp=flights[j]
                    flights[j]=flights[j+1]
                    flights[j+1]=temp
 
 
for index in range(len(flights)):
    print(flights[index])                   
    sort(flights)
