username= 'hemu','jaiveer','sahil','rakesh','raju'
search = input("Enter your username: ")

idx = 0
i = False
while idx <=4:
    if username[idx] == search:
        print("Username found")
        i = True
        break
    idx += 1
    
if i == False:
    print("Username not found")