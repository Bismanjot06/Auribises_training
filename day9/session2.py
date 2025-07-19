class menu:
    def __init__(self, name='NA', dishes=[], number_of_dishes=0):
        self.name = name
        self.dishes = dishes
        self.number_of_dishes = number_of_dishes
        
    def show(self):
        print("---------MENU----------")
        print('name:',self.name)
        #print('dishes:', self.dishes)
        print('dishes')
        for index in range (len(self.dishes)):
            self.dishes[index].show()
        print('number of dishes:', self.number_of_dishes)
        print('---------------------')
        
        
