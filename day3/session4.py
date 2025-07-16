#view -> intrface
#interface is a one, with which user interacts with the system

location = input('Enter your location: ')
print('u entered: ', location)
print(type(location))

travellers = int(input('Enter numer of travellers: '))
print('u entered: ', travellers)
print( type(travellers))

feedback = float(input('Enter your feedback: '))
print('u entered:', feedback)
print(type(feedback))

flight_booking = {
    'from': location,
    travellers: travellers,
    'feedback': feedback
}

print(flight_booking)

# as the above program has more variables which will make the RAM use more space and reference
#  we can use the below syntax 
0
flight_booking = {
    'from': input('Enter From Location: '),
    'to': input('Enter To Location: '),
    'travelers': int(input('Enter Travelers: ')), 
    'feedback': float(input('Enter Feedback: ')) 
}

print(flight_booking)
