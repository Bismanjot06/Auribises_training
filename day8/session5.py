class user:
    def __init__(self, name='NA', email='NA', phone='NA', address='NA', age=18):
        print("constructor executed")
        print('self', self, id(self), type(self))
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.age = age
        
    def show(self):
        print("~~~~~~~~~~~~~~~~~~~")
        print(self.name, self.email, self.phone, self.address, self.age)
        print("~~~~~~~~~~~~~~~~~~~")
        print(vars(self))  # shows the attributes of the object with data in it

    
        
Jhon = user("Jhon", "chotu@gmail.com", "1234567890", "Delhi", 25)
Hari = user("Hari", "har@yahoo.com", "0987654321", "Mumbai", 30)        
'''
print('data in Jhon object')
print(vars(Jhon))  # shows the attributes of the object with data in it
print('data in Hari object')
print(vars(Hari))  # shows the attributes of the object with data in it
'''
Jhon.show ()
Hari.show ()