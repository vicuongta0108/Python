class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = [] # initialize an empty list

    # Add new passenger to passengers list
    def add_passenger(self, name):
        if not self.open_seats(): # if self.open_seat() == 0
            return False # no open seat
        self.passengers.append(name) 
        return True
    
    # Check for availability
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight =  Flight(3) # 3 passengers

people  = ['Harry', 'Ron', 'Hermione', 'Ginny']
for person in people:
    if flight.add_passenger(person):
        print(f'Added {person} to flight successfully')
    else: 
        print(f'No available seats for {person}')
