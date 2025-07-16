username= 'hemu','jaiveer','sahil','rakesh','raju'
search = input("Enter your username: ")

i=False
for index in range(0, 5):
    if username[index] == search:
        print("Username found")
        break
    
if i == False:
    print("Username not found")    