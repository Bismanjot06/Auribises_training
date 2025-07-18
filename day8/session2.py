#creating a class and object in python

class user:
    def __init__(self):# constructor
        print("constructor executed")
        print('self', self, id(self), type(self))
        
jhon = user()
Hari = user()

#reference copy variable        
jhonie = jhon 

print('jhon:', jhon, id(jhon), type(jhon))
print('jhonie:', jhonie, id(jhonie), type(jhonie))
print('Hari:', Hari, id(Hari), type(Hari))
# jhon and jhonie are same object, they are pointing to same memory location

jhon.name = "Jhon"
jhon.email = "chotu@gmail.com"
jhon.phone = "1234567890"
jhon.address = "Delhi"
jhonie.age = 25
Hari.name = "Hari"
Hari.email = "har@yahoo.com"
Hari.phone = "0987654321"
Hari.address = "Mumbai"


# On Object we can perfrom
# 1. Create/Write
# 2. Update
# 3. Delete
# 4. Read

# CRUD operations