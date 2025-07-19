class restaurant:
    def __init__(self, name='NA', address='NA', email="NA", rating='NA', menu=None):
        self.name = name
        self.address = address
        self.email = email
        self.rating = rating
        self.menu = menu  
        

    def show(self):
        print("--------RESTAURANT----------")
        print('name:',self.name)
        print('address:', self.address)
        print('email:', self.email)
        print('rating:', self.rating)
        print('menu:')
        self.menu.show()
        print()

