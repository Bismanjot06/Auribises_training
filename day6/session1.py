#when we dont kow how many arguments we are going to pass
#we can use *args and **kwargs

def add(*args):
    print("Adding numbers:", args) #args is a tuple
    print("Sum:", sum(args))

add(1, 2, 3)
add(4, 5, 6, 7, 8)  
add(10, 20, 30, 40, 50, 60, 70)
add(100, 200, 300, 400, 500, 600, 700, 800, 900)    



def registor_user(**user): #kwargs is a dictionary
    print("User details:", user)
    
registor_user(name="John", age=30, city="New York", email="chotu")    
