# Circular Doubly Linked List
class CarList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # add is going to add a car in the linked list
    def add(self, car):
        self.size += 1
        if self.head == None:
            self.head = car
            self.tail = car
        else:
             car.previous = self.tail
             car.next = self.head
             self.tail.next = car
             self.head.previous = car
             self.tail = car
    def iterate(self, direction=0):

       def add(self, car):
            self.size += 1
            if self.head is None:
                self.head = car
                self.tail = car
                # Point to self for circular link
                car.next = car
                car.previous = car
            else:
                car.previous = self.tail
                car.next = self.head
                self.tail.next = car
                self.head.previous = car
                self.tail = car



    def delete(self, car):
        pass

    def delete_head(self):
        pass

    def delete_tail(self):
        pass

    def bubble_sort(self):
        pass
    
    def add_in_front(self, car):
        pass
    
    def in_between(self, car1,car2, car):
        car.next = car2
        car.previous = car1
        car1.next = car
        car2.previous = car
        self.size += 1
        
        