'''
creating stack data structure with the linked list reference
 
stack
  iterate
  push
  pop 
'''

class CarStack:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # add is going to add a car in the linked list
    def push(self, car):
        self.size += 1

        if self.head == None:
            self.head = car
            self.tail = car
        else:
            self.tail.next = car
            car.previous = self.tail
            car.next = self.head
            self.head.previous = car
            self.tail = car

    def iterate(self, direction=0):

        if direction == 0:
            car = self.head
            print(car)
            while car.next != self.head:
                car = car.next
                print(car)
        else:
            car = self.tail
            print(car)
            while car.previous != self.tail:
                car = car.previous
                print(car)
                
    def pop(self):
        # delete tail
        self.tail = self.tail.previous
        self.tail.next = self.head
        self.head.previous = self.tail
        self.size -= 1            